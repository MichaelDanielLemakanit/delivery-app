from flask import Flask, flash, render_template, request, redirect, url_for, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)
app.secret_key = '12345678'

ALLOWED_SELLER_PAGES = {
    'home': 'seller/home.html',
    'dashboard': 'seller/dashboard.html',
    'login': 'seller/login.html',
    'register': 'seller/register.html',
    'new-delivery': 'seller/new_delivery.html',
    'delivery-details': 'seller/delivery_details.html',
}
CUSTOMER_PAGES = {
    'dashboard': 'customer/dashboard.html',
    'login': 'customer/login.html',
    'payment_upload': 'customer/payment_upload.html',
    'order_details': 'customer/order_details.html',
    'return_order': 'customer/return_order.html',
}
RIDER_PAGES = {
    'dashboard': 'rider/dashboard.html',
    'login': 'rider/login.html',
    'register': 'rider/register.html'
}


@app.route('/')
def home():
    return render_template('index.html')

# seller/ marchant routes
@app.route('/seller/', defaults={'page_name': 'home'}, methods=['GET', 'POST'])
@app.route('/seller/<page_name>')
def seller_pages(page_name):
    # Check if requested page exists in allowed list
    if page_name in ALLOWED_SELLER_PAGES:
        return render_template(ALLOWED_SELLER_PAGES[page_name])
    
    # Return 404 error page if the page name isn't valid
    abort(404)

# customer routes
@app.route('/customer/', defaults={'page_name': 'dashboard'}, methods=['GET', 'POST'])
@app.route('/customer/<page_name>')
def customer_pages(page_name):
    clean_name = page_name.replace('.html', '')
    if clean_name in CUSTOMER_PAGES:
        flash("Your return request has been submitted successfully!", "success")
        return render_template(CUSTOMER_PAGES[clean_name])
    abort(404)

# rider routes
@app.route('/rider/', defaults={'page_name': 'dashboard'}, methods=['GET', 'POST'])
@app.route('/rider/<page_name>')
def rider_pages(page_name):
    if page_name in RIDER_PAGES:
        return render_template(RIDER_PAGES[page_name])
    
    # Return 404 error page if the page name isn't valid
    abort(404)
                                                        

# if __name__ == "__main__":
#     app.run(debug=True)
app = app