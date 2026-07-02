from flask import Flask, render_template,redirect, url_for, session

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    # This links the URL '/' to your HTML file
    return render_template('index.html') 


# marchant/seller route
@app.route('/seller/login')
def seller_login():
    if 'user_id' in session:
        return redirect(url_for('dashboard.html'))
    else:
        return redirect(url_for('register.html'))
    return render_template('auth/seller/login.html')

# rider login route
@app.route('/rider/login')
def rider_login():
    # if 'user_id' in session:
    #     return redirect(url_for('home'))
    # else:
    #     return redirect(url_for('register.html'))
    return render_template('auth/rider/login.html')


# customers route
@app.route('/customer/login')
def customer_login():
    if 'user_id' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('register.html'))
    return render_template('auth/customer/login.html', login='customer_login')










if __name__ == '__main__':
    app.run(debug=True)