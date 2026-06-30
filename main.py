from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    # This links the URL '/' to your HTML file
    return render_template('index.html') 

@app.route('/customer/login', methods=['GET', 'POST'])
def customer_login():
    # Tell Flask to look inside the auth and customer subfolders
    return render_template('auth/customer/login.html', login='customer_login')










if __name__ == '__main__':
    app.run(debug=True)