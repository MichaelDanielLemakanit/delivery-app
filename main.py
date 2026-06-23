from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for flash messages and sessions
bcrypt = Bcrypt(app)

# --- MOCK DATABASE FOR TESTING ---
# We preload a test user so you can log in immediately.
# Password for Daniel is: admin123
MOCK_USERS_DB = {
    "daniel@mjdelivery.com": {
        "email": "daniel@mjdelivery.com",
        "password_hash": bcrypt.generate_password_hash("admin123").decode('utf-8')
    }
}

def query_user_from_db(email):
    # Checks if the email exists in our dictionary database
    return MOCK_USERS_DB.get(email) 


@app.route('/')
@app.route("/home")
def home():
    # If already logged in, skip the landing page and go straight to dashboard
    if 'email' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


# 1. Access Control Decorator
def login_required(f):
    @wraps(f)
    def protected(*args, **kwargs):
        if 'email' not in session:
            flash("Please log in or register first.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return protected


# 2. Login Route
@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'email' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = query_user_from_db(email) 
        
        # SCENARIO: Account was not found
        if user is None:
            flash("Account not found. Please register an account first!", "danger")
            return redirect(url_for('register'))
            
        # SCENARIO: Account found, verify password
        if bcrypt.check_password_hash(user['password_hash'], password):
            session['email'] = email
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Incorrect password. Please try again.", "danger")
            
    return render_template('login.html')


# 3. Registration Route
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email in MOCK_USERS_DB:
            flash("Email already registered!", "danger")
            return redirect(url_for('register'))
            
        # Hash the password and save it into our mock database
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        MOCK_USERS_DB[email] = {
            "email": email,
            "password_hash": hashed_pw
        }
        
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))
        
    return render_template('register.html')


# 4. Logout Route (NEW)
@app.route("/logout")
def logout():
    session.pop('email', None) # Clears user out of session tracking
    flash("You have been successfully logged out.", "info")
    return redirect(url_for('login'))


# --- Protected Routes ---
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route("/newdelivery")
@login_required  
def newdelivery():
    return render_template('newdelivery.html')

@app.route("/riders")
@login_required  
def riders():
    return render_template('riders.html')

@app.route("/seller")
@login_required  
def seller():
    return render_template('seller.html')

@app.route("/notification")
@login_required  
def notification():
    return render_template('notification.html')


if __name__ == '__main__':
    app.run(debug=True)