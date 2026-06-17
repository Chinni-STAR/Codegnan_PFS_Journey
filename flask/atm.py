from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# =========================================
# ATM CLASS (Core Business Logic)
# =========================================

class ATM:
    def __init__(self, name, mobile, pin, balance):
        self.user_info = {
            "Name": name,
            "Mobile Number": mobile,
            "ATM PIN": pin,
            "Balance": balance,
            "Transaction History": []
        }

    def validate_pin(self, user_pin):
        return user_pin == self.user_info["ATM PIN"]

    def deposit(self, amount):
        if amount >= 1000 and amount % 100 == 0:
            self.user_info["Balance"] += amount
            self.user_info["Transaction History"].append(f"💰 Deposited: ₹{amount:,}")
            return "Amount Deposited Successfully"
        return "Minimum deposit is ₹1000 and must be multiples of 100 only"

    def withdraw(self, amount):
        if amount <= 0:
            return "Please enter a valid positive amount"
        if amount % 100 != 0:
            return "Withdrawal amount must be a multiple of 100"
        if amount <= self.user_info["Balance"]:
            self.user_info["Balance"] -= amount
            self.user_info["Transaction History"].append(f"💸 Withdrawn: ₹{amount:,}")
            return "Please collect your cash"
        return "Insufficient balance for this withdrawal"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.user_info["ATM PIN"]:
            if len(new_pin) == 4 and new_pin.isdigit():
                self.user_info["ATM PIN"] = new_pin
                self.user_info["Transaction History"].append("🔒 Security PIN Changed")
                return "PIN changed successfully"
            return "PIN must be exactly 4 digits"
        return "Incorrect old PIN"


# Global Instantiation of the ATM Object
atm = ATM(name="Bhanu Teja", mobile="9876543210", pin="6600", balance=47238)

# =========================================
# CENTRALIZED DESIGN SYSTEM (Bank of India Glass)
# =========================================
SHARED_STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: 'Poppins', sans-serif;
    }
    
    body {
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        /* Bank of India Corporate Color Shifting Gradient (Deep Blue to Premium Amber) */
        background: linear-gradient(135deg, #05163a, #0a2f7c, #1e4f9e, #f37022, #b74f11);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        overflow: hidden;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glassmorphism Card Frame with Blue Tint tint */
    .card {
        background: rgba(10, 47, 124, 0.25);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(243, 112, 34, 0.4); /* BOI Orange Outline border */
        padding: 40px;
        border-radius: 24px;
        width: 450px;
        text-align: center;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(255, 255, 255, 0.05);
        color: #fff;
        animation: smoothSlideIn 0.5s cubic-bezier(0.1, 0.8, 0.3, 1);
    }

    @keyframes smoothSlideIn {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    h1 {
        font-size: 28px;
        font-weight: 600;
        margin-bottom: 4px;
        letter-spacing: 1px;
        color: blue;
    }

    h2 {
        font-size: 20px;
        margin-bottom: 25px;
        color: #f37022; /* BOI Vibrant Orange */
        text-shadow: 0 0 10px rgba(243, 112, 34, 0.3);
        font-weight: 600;
    }

    p {
        font-size: 15px;
        opacity: 0.9;
        margin-bottom: 20px;
    }

    /* Input Customization */
    input[type="password"], input[type="number"] {
        width: 100%;
        padding: 14px 20px;
        margin: 10px 0 20px 0;
        border: 2px solid rgba(255, 255, 255, 0.2);
        background: rgba(5, 22, 58, 0.5);
        border-radius: 12px; /* Professional semi-sharp edges */
        color: white;
        font-size: 18px;
        outline: none;
        transition: all 0.3s ease;
        text-align: center;
    }

    input:focus {
        border-color: #f37022;
        box-shadow: 0 0 15px rgba(243, 112, 34, 0.5);
        background: rgba(5, 22, 58, 0.7);
    }

    /* Core Action Buttons - BOI Signature Orange Gradient */
    button, .btn {
        display: inline-block;
        width: 100%;
        padding: 14px;
        border: none;
        border-radius: 12px;
        background: linear-gradient(45deg, #f37022, #ff8c42);
        color: white;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        margin-top: 10px;
        box-shadow: 0 4px 15px rgba(243, 112, 34, 0.3);
        letter-spacing: 0.5px;
    }

    button:hover, .btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(243, 112, 34, 0.6);
        background: linear-gradient(45deg, #ff8c42, #f37022);
    }

    /* Navigation Menu Container */
    .menu-container {
        margin: 20px 0;
    }

    .menu-link {
        display: block;
        padding: 14px 20px;
        margin: 12px 0;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        color: #fff;
        text-decoration: none;
        border-radius: 12px;
        text-align: left;
        font-size: 16px;
        transition: all 0.25s ease;
        border-left: 4px solid #ffcc00; /* Gold Brand Accents */
    }

    .menu-link:hover {
        background: #ffffff;
        color: #0a2f7c; /* Changes to BOI Blue on Hover */
        transform: translateX(6px);
        font-weight: 600;
        border-left: 4px solid #f37022;
    }

    .display-amt {
        font-size: 40px;
        font-weight: 600;
        color: #ffcc00; /* Gold representation for currency */
        margin: 20px 0;
        text-shadow: 0 0 15px rgba(255, 204, 0, 0.4);
    }

    /* List styling for historical feed */
    ul {
        list-style: none;
        max-height: 220px;
        overflow-y: auto;
        margin-bottom: 25px;
        padding-right: 5px;
    }

    li {
        background: rgba(0, 0, 0, 0.25);
        padding: 12px;
        margin-bottom: 10px;
        border-radius: 8px;
        font-size: 14px;
        text-align: left;
        border-left: 4px solid #f37022;
    }

    ul::-webkit-scrollbar { width: 6px; }
    ul::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.20); border-radius: 10px; }

    /* Alternate Back/Exit Buttons (BOI Corporate Blue) */
    .btn-back {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: none;
    }
    .btn-back:hover {
        background: rgba(255, 255, 255, 0.2);
        box-shadow: none;
        color: #fff;
    }

    .btn-exit {
        background: linear-gradient(45deg, #0a2f7c, #1e4f9e);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 15px rgba(10, 47, 124, 0.3);
    }
    .btn-exit:hover {
        background: linear-gradient(45deg, #1e4f9e, #0a2f7c);
        box-shadow: 0 6px 20px rgba(10, 47, 124, 0.5);
    }
</style>
"""


@app.route("/")
def home():
    return render_template_string(f"""
    {SHARED_STYLE}
    <div class="card">
        <div style="font-size: 40px; margin-bottom: 5px;">⭐</div>
        <h1>BANK OF INDIA</h1>
        <p style="color: #ffcc00; font-size: 13px; margin-bottom: 35px; letter-spacing: 1px; font-weight: 600;">Relationship beyond banking</p>
        <a href='/login' class="btn">Touch to Start / self-service</a>
    </div>
    """)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pin = request.form["pin"]
        if atm.validate_pin(pin):
            return redirect(url_for("menu"))
        else:
            return render_template_string(f"""
            {SHARED_STYLE}
            <div class="card">
                <h2 style="color: #ff4a4a;">❌ Transaction Declined</h2>
                <p>The security ATM PIN entered is incorrect.</p>
                <a href='/login' class="btn">Re-enter PIN</a>
            </div>
            """)

    return render_template_string(f"""
    {SHARED_STYLE}
    <div class="card">
        <h1>Welcome to BOI ATM</h1>
        <h2>Please Enter Your PIN</h2>
        <form method="POST">
            <p style="text-align: left; margin-bottom: 5px; font-size: 14px; opacity: 0.8;">Enter 4-Digit Secret Code:</p>
            <input type="password" name="pin" maxlength="4" placeholder="••••" required autofocus>
            <button type="submit">Verify & Proceed</button>
        </form>
        <a href="/" class="btn btn-back" style="margin-top: 15px;">Exit Card</a>
    </div>
    """)


@app.route("/menu")
def menu():
    return render_template_string(f"""
    {SHARED_STYLE}
    <div class="card">
        <h1>Main Menu</h1>
        <h2>A/C Holder: {atm.user_info['Name']}</h2>
        
        <div class="menu-container">
            <a href='/deposit' class="menu-link">📥 Cash Deposit</a>
            <a href='/withdraw' class="menu-link">💸 Withdrawal</a>
            <a href='/balance' class="menu-link">🏦 Balance Enquiry</a>
            <a href='/change_pin' class="menu-link">🔒 PIN Change</a>
            <a href='/history' class="menu-link">📜 Transaction Statement</a>
        </div>
        
        <a href='/' class="btn btn-exit">🚪 Cancel & Return Card</a>
    </div>
    """)


@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        try:
            amount = int(request.form["amount"])
            message = atm.deposit(amount)
        except ValueError:
            message = "Please enter a valid numeric amount."

        return render_template_string(f"""
        {SHARED_STYLE}
        <div class="card">
            <h2>Transaction Status</h2>
            <p style="font-size: 18px; margin: 25px 0;">{message}</p>
            <a href='/menu' class="btn btn-back">Go to Main Menu</a>
        </div>
        """)

    return render_template_string(f"""
    {SHARED_STYLE}
    <div class="card">
        <h1>BOI Cash Deposit</h1>
        <form method="POST">
            <p style="text-align: left; font-size:14px; margin-bottom: 0;">Enter Amount (Multiples of 100, Min ₹1000):</p>
            <input type="number" name="amount" placeholder="Enter Cash Amount" required>
            <button type="submit">Confirm Deposit</button>
        </form>
        <a href='/menu' class="btn btn-back" style="margin-top: 15px;">Cancel</a>
    </div>
    """)


@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        try:
            amount = int(request.form["amount"])
            message = atm.withdraw(amount)
        except ValueError:
            message = "Please enter a valid numeric amount."

        return render_template_string(f"""
        {SHARED_STYLE}
        <div class="card">
            <h2>Transaction Status</h2>
            <p style="font-size: 18px; margin: 25px 0;">{message}</p>
            <a href='/menu' class="btn btn-back">Go to Main Menu</a>
        </div>
        """)

    return render_template_string(f"""
    {SHARED_STYLE}
    <div class="card">
        <h1>Cash Withdrawal</h1>
        <form method="POST">
            <p style="text-align: left; font-size:14px; margin-bottom: 0;">Please Enter Amount (Multiples of 100):</p>
            <input type="number" name="amount" placeholder="Enter Amount" required>
            <button type="submit">Withdraw Cash</button>
        </form>
        <a href='/menu' class="btn btn-back" style="margin-top: 15px;">Cancel</a>
    </div>
    """)


@app.route("/balance")
def balance():
    return render_template_string(f"""
    {SHARED_STYLE}
    <div class="card">
        <h1>Available Balance</h1>
        <div class="display-amt">
            ₹{atm.user_info['Balance']:,}
        </div>
        <p style="font-size: 13px; opacity:0.7; margin-bottom: 25px;">Savings Account Ledger Balance</p>
        <a href='/menu' class="btn btn-back">Go to Main Menu</a>
    </div>
    """)


@app.route("/change_pin", methods=["GET", "POST"])
def change_pin():
    if request.method == "POST":
        old_pin = request.form["old_pin"]
        new_pin = request.form["new_pin"]
        message = atm.change_pin(old_pin, new_pin)

        return render_template_string(f"""
        {SHARED_STYLE}
        <div class="card">
            <h2>PIN Change Status</h2>
            <p style="font-size: 18px; margin: 25px 0;">{message}</p>
            <a href='/menu' class="btn btn-back">Go to Main Menu</a>
        </div>
        """)

    return render_template_string(f"""
    {SHARED_STYLE}
    <div class="card">
        <h1>PIN Management</h1>
        <form method="POST">
            <p style="text-align: left; font-size:14px; margin-bottom:0;">Enter Existing PIN:</p>
            <input type="password" name="old_pin" maxlength="4" placeholder="••••" required>
            
            <p style="text-align: left; font-size:14px; margin-bottom:0;">Enter New 4-Digit PIN:</p>
            <input type="password" name="new_pin" maxlength="4" placeholder="••••" required>
            
            <button type="submit">Update New PIN</button>
        </form>
        <a href='/menu' class="btn btn-back" style="margin-top: 15px;">Cancel</a>
    </div>
    """)


@app.route("/history")
def history():
    history_data = ""
    tx_list = atm.user_info["Transaction History"]
    
    if not tx_list:
        history_data = "<p style='opacity:0.5; padding: 20px 0;'>No recent transactions on this card.</p>"
    else:
        for txn in reversed(tx_list):  
            history_data += f"<li>{txn}</li>"

    return render_template_string(f"""
    {SHARED_STYLE}
    <div class="card">
        <h1>Transaction Statement</h1>
        <p style="font-size: 13px; color: #ffcc00; margin-bottom: 15px;">Your Last Terminal Activities</p>
        <ul>
            {history_data}
        </ul>
        <a href='/menu' class="btn btn-back">Go to Main Menu</a>
    </div>
    """)


if __name__ == "__main__":
    app.run(debug=True)
