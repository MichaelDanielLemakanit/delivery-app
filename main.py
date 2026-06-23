from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for flash messages and sessions
bcrypt = Bcrypt(app)

# Mock database for demonstration purposes
# In your real app, this will be a database query (e.g., SQLite, PostgreSQL)
def query_user_from_db(email):
    # return user_object or None
    return None 

@app.route('/')
@app.route("/home")
def home():
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

# 2. Updated Login Route handling GET and POST
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Look up user in your database
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Your registration logic here (hash password, save to DB)
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))
        
    return render_template('register.html')

# Protected Routes
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route("/newdelivery")
@login_required  # <-- Protected
def newdelivery():
    return render_template('newdelivery.html')

@app.route("/riders")
@login_required  # <-- Protected
def riders():
    return render_template('riders.html')

@app.route("/seller")
@login_required  # <-- Protected
def seller():
    return render_template('seller.html')

@app.route("/notification")
@login_required  # <-- Protected
def notification():
    return render_template('notification.html')



if __name__ == '__main__':
    app.run(debug=True)