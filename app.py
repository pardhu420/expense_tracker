from flask import Flask, render_template, request, redirect, session
import json
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

DATA_FILE = "expenses.json"
USERS_FILE = "users.json"

# --- Utility Functions ---
def load_expenses():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            f.write("[]")
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            return json.loads(content) if content else []
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump([{"username":"admin","password":"admin"}], f)
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def check_login(username, password):
    users = load_users()
    for u in users:
        if u["username"] == username and u["password"] == password:
            return True
    return False

# --- Routes ---

# Login Page
@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        if check_login(username, password):
            session['username'] = username
            return redirect('/home')
        else:
            return render_template("login.html", error="Invalid credentials!")
    return render_template("login.html")

# Register Page
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        if not username or not password:
            return render_template("register.html", error="All fields are required!")
        users = load_users()
        for u in users:
            if u["username"] == username:
                return render_template("register.html", error="Username already exists!")
        users.append({"username": username, "password": password})
        save_users(users)
        return redirect('/')
    return render_template("register.html")

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

# Home Page
@app.route('/home')
def home():
    if 'username' not in session:
        return redirect('/')
    expenses = load_expenses()
    user_expenses = [e for e in expenses if e['username'] == session['username']]
    total = sum([float(e['amount']) for e in user_expenses])
    category_summary = {}
    for e in user_expenses:
        category_summary[e['category']] = category_summary.get(e['category'], 0) + float(e['amount'])
    return render_template("index.html", expenses=user_expenses, total=total, category_summary=category_summary, username=session['username'])

# Add Expense
@app.route('/add', methods=['POST'])
def add():
    if 'username' not in session:
        return redirect('/')
    date = request.form.get('date')
    amount = request.form.get('amount')
    category = request.form.get('category')
    description = request.form.get('description')

    if not date or not amount or not category:
        return "Date, Amount, and Category are required!", 400
    try:
        amount = float(amount)
        if amount <= 0:
            return "Amount must be greater than 0!", 400
    except ValueError:
        return "Amount must be a number!", 400

    expense = {
        "username": session['username'],
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    return redirect('/home')

# Delete Expense
@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if 'username' not in session:
        return redirect('/')
    expenses = load_expenses()
    user_expenses = [e for e in expenses if e['username'] == session['username']]
    if 0 <= index < len(user_expenses):
        exp_to_delete = user_expenses[index]
        expenses.remove(exp_to_delete)
        save_expenses(expenses)
    return redirect('/home')

if __name__ == '__main__':
    app.run(debug=True)
