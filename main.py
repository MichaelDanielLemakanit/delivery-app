from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/newdelivery")
def newdelivery():
    return render_template('newdelivery.html')

@app.route("/riders")
def riders():
    return render_template('riders.html')

@app.route("/seller")
def seller():
    return render_template('seller.html')

@app.route("/payments")
def payments():
    return render_template('payments.html')


@app.route("/notification")
def notification():
    return render_template('notification.html')

@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)