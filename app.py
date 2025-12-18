from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_demo_purposes'
DATA_FILE = 'items.json'

def load_items():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_items(items):
    with open(DATA_FILE, 'w') as f:
        json.dump(items, f, indent=4)

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Simple hardcoded check
        if username == 'admin' and password == 'admin':
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    items = load_items()
    return render_template('dashboard.html', items=items, user=session['user'])

@app.route('/add', methods=['POST'])
def add_item():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    item_name = request.form.get('name')
    item_quantity = request.form.get('quantity')
    
    if item_name and item_quantity:
        items = load_items()
        new_item = {
            'id': len(items) + 1,
            'name': item_name,
            'quantity': item_quantity
        }
        items.append(new_item)
        save_items(items)
        
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
