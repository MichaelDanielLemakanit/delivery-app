from flask import Flask, render_template,redirect, request, url_for, session

app = Flask(__name__)

app.secret_key = 'a_secure_and_random_secret_key'

# # dummy username and password for testing
USERNAME = "admin@example.com"
PASSWORD = "password"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reset_password')
def reset_password():
    return render_template('auth/reset_password.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('auth/forgot_password.html')

# # marchant/seller route
@app.route('/seller/login', methods=['GET', 'POST'])
def seller_login():
   if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['user_id'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('auth/seller/index.html', error='Invalid username or password')
   return render_template('auth/seller/login.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# # rider login route
# @app.route('/rider/login', methods = ['GET', 'POST'])
# def rider_login():
#     # if 'user_id' in session:
#     #     return redirect(url_for('home'))
#     # else:
#     #     return redirect(url_for('register.html'))
#     return render_template('auth/rider/login.html')


# # customers route
# @app.route('/customer/login', methods = ['GET', 'POST'])
# def customer_login():
#     # if 'user_id' in session:
#     #     return redirect(url_for('home'))
#     # else:
#     #     return redirect(url_for('register.html'))
#     return render_template('auth/customer/login.html', login='customer_login')










if __name__ == '__main__':
    app.run(debug=True)