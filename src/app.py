from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os
import datetime

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_demo_purposes'
DATA_FILE = 'items.json'

# User Data File
USER_DATA_FILE = 'users.json'

def load_users():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    try:
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_users(users):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# Initialize default users if file is empty
if not os.path.exists(USER_DATA_FILE) or os.stat(USER_DATA_FILE).st_size <= 2:
    default_users = {
        'admin': {'password': 'admin', 'role': 'Admin'},
        'manager': {'password': 'manager', 'role': 'Manager'},
        'viewer': {'password': 'viewer', 'role': 'Viewer'}
    }
    save_users(default_users)

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
        
        users = load_users()
        
        if username in users and users[username]['password'] == password:
            session['user'] = username
            session['role'] = users[username]['role']
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid Credentials. Defaults: admin/admin, manager/manager, viewer/viewer'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    items = load_items()
    
    # CR-002: Search and Filter
    query = request.args.get('search', '').lower()
    min_qty = request.args.get('min_qty')
    max_qty = request.args.get('max_qty')
    
    filtered_items = []
    
    for item in items:
        # Search Filter
        if query and query not in item['name'].lower():
            continue
            
        # Quantity Filter
        try:
            qty = int(item['quantity'])
            if min_qty and qty < int(min_qty):
                continue
            if max_qty and qty > int(max_qty):
                continue
        except ValueError:
            pass # Ignore INVALID quantity data for filtering
            
        filtered_items.append(item)
        
    return render_template('dashboard.html', 
                           items=filtered_items, 
                           user=session['user'],
                           role=session['role'],
                           search_query=query)

@app.route('/add', methods=['POST'])
def add_item():
    if 'user' not in session:
        return redirect(url_for('login'))
        
    # Permission Check (Viewer cannot add)
    if session.get('role') == 'Viewer':
        return redirect(url_for('dashboard'))
    
    item_name = request.form.get('name')
    item_quantity = request.form.get('quantity')
    
    if item_name and item_quantity:
        items = load_items()
        new_item = {
            'id': len(items) + 1, # Simple ID generation
            'name': item_name,
            'quantity': item_quantity,
            'last_modified': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'modified_by': session['user']
        }
        items.append(new_item)
        save_items(items)
        
    return redirect(url_for('dashboard'))

# CR-001: Edit Item Route
@app.route('/edit/<int:item_id>', methods=['POST'])
def edit_item(item_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    # Permission Check (Viewer cannot edit)
    if session.get('role') == 'Viewer':
        return redirect(url_for('dashboard'))

    item_name = request.form.get('name')
    item_quantity = request.form.get('quantity')

    if item_name and item_quantity:
        items = load_items()
        for item in items:
            if item.get('id') == item_id:
                item['name'] = item_name
                item['quantity'] = item_quantity
                item['last_modified'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['modified_by'] = session['user']
                break
        save_items(items)

    return redirect(url_for('dashboard'))

# CR-001: Delete Item Route (Admin Only)
@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    # Permission Check (Only Admin can delete)
    if session.get('role') != 'Admin':
        return redirect(url_for('dashboard'))

    items = load_items()
    # Create new list excluding the item to delete
    items = [item for item in items if item.get('id') != item_id]
    save_items(items)

    return redirect(url_for('dashboard'))

# CR-003: User Management Routes (Admin Only)
@app.route('/users')
def manage_users():
    if 'user' not in session:
        return redirect(url_for('login'))
        
    # Strict Permission Check
    if session.get('role') != 'Admin':
        return redirect(url_for('dashboard'))
        
    users = load_users()
    return render_template('users.html', users=users, user=session['user'], role=session['role'])

@app.route('/users/add', methods=['POST'])
def add_user():
    if 'user' not in session or session.get('role') != 'Admin':
        return redirect(url_for('login'))
        
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    
    if username and password and role:
        users = load_users()
        if username not in users:
            users[username] = {'password': password, 'role': role}
            save_users(users)
            
    return redirect(url_for('manage_users'))

@app.route('/users/delete/<username>', methods=['POST'])
def delete_user(username):
    if 'user' not in session or session.get('role') != 'Admin':
        return redirect(url_for('login'))
        
    # Prevent deleting yourself
    if username == session['user']:
        return redirect(url_for('manage_users'))
        
    users = load_users()
    if username in users:
        del users[username]
        save_users(users)
        
    return redirect(url_for('manage_users'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
