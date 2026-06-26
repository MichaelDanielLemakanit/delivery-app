from flask import Flask, render_template, request, redirect, url_scheduler, flash

app = Flask(__name__)
# Secret key is required for session management and flashing validation messages
app.secret_key = 'nairobi_delivery_app_secret_key_2026'

# ==========================================
# 🏠 1. MAIN LANDING GATEWAY
# ==========================================
@app.route('/')
def index():
    return render_template('index.html')


# ==========================================
# 🛒 2. CUSTOMER / RECEIVER ROUTES
# ==========================================
@app.route('/auth/customer/login', methods=['GET', 'POST'])
def customer_login():
    if request.method == 'POST':
        delivery_id = request.form.get('delivery_id')
        customer_phone = request.form.get('customer_phone')
        
        # TODO: Connect database query here to validate order
        # For now, let's pretend ID '1024' is a valid order matching any phone
        if delivery_id == '1024':
            return redirect('/auth/customer/order_details')
        else:
            flash('Invalid Tracking ID or Phone Number. Please try again.', 'error')
            return redirect('/auth/customer/login')
            
    return render_template('auth/customer/login.html')

@app.route('/auth/customer/order_details')
def customer_order_details():
    return render_template('auth/customer/order_details.html')


# ==========================================
# 🏢 3. SELLER / MERCHANT ROUTES
# ==========================================
@app.route('/auth/seller/login', methods=['GET', 'POST'])
def seller_login():
    if request.method == 'POST':
        return redirect('/auth/seller/dashboard')
    return render_template('auth/seller/login.html')

@app.route('/auth/seller/dashboard')
def seller_dashboard():
    return render_template('auth/seller/dashboard.html')


# ==========================================
# 🏍️ 4. RIDER ROUTES
# ==========================================
@app.route('/auth/rider/login', methods=['GET', 'POST'])
def rider_login():
    if request.method == 'POST':
        return redirect('/auth/rider/dashboard')
    return render_template('auth/rider/login.html')

@app.route('/auth/rider/dashboard')
def rider_dashboard():
    return render_template('auth/rider/dashboard.html')


# ==========================================
# 🚀 SERVER STARTUP ENGINE
# ==========================================
if __name__ == '__main__':
    # debug=True automatically updates the page when you save code changes
    app.run(debug=True, port=5000)