from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = '12345678'


@app.route('/')
def home():
    return render_template('index.html')


#seller routes
@app.route('/seller/home')
def seller_home():
    return render_template('seller/home.html')


@app.route('/rider/dashboard')
# @login_required
def rider_dashboard():
    return render_template('rider/dashboard.html')

@app.route('/customer/dashboard')
# @login_required
def customer_dashboard():
    return render_template('customer/dashboard.html')



app.run(debug = True)