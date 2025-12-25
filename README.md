# 📦 Inventory Tracker System

A simple, elegant web-based inventory management system built with Flask.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/HenokTade/inventory-tracker.git
cd inventory-tracker

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/app.py
```

Visit `http://localhost:5000` and login with:
- **Admin**: `admin` / `admin` (Full Access)
- **Manager**: `manager` / `manager` (Edit Access)
- **Viewer**: `viewer` / `viewer` (Read Only)

## 📁 Project Structure

```
inventory-tracker/
├── docs/              # 📚 Documentation
│   ├── README.md
│   ├── INSTALLATION.md
│   └── USER_GUIDE.md
├── src/               # 💻 Source code
│   ├── app.py
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   └── users.html
│   └── static/
├── tests/             # 🧪 Unit tests
├── releases/          # 📋 Release notes
├── items.json         # 💾 Inventory Data
├── users.json         # 👥 User Data
└── requirements.txt   # 📦 Dependencies
```

## ✨ Features

- ✅ **Secure Authentication** - Login system with role-based access
- ✅ **Role Management** - Admin, Manager, and Viewer roles
- ✅ **Inventory Dashboard** - View all items with real-time updates
- ✅ **Search & Filter** - Instant search and quantity filtering
- ✅ **Item Management** - Add, edit, and delete inventory items
- ✅ **User Management** - Admin interface to manage users
- ✅ **Audit Trail** - Track modifications and timestamps
- ✅ **Data Persistence** - Automatic JSON-based storage
- ✅ **Responsive Design** - Clean, modern UI

## 📖 Documentation

- **[Installation Guide](docs/INSTALLATION.md)** - Setup instructions
- **[User Guide](docs/USER_GUIDE.md)** - How to use the system
- **[Release Notes](releases/v1.1.0.md)** - Version history

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

See [tests/README.md](tests/README.md) for more details.

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3
- **Storage**: JSON
- **Testing**: unittest, pytest

## 📝 License

This project is licensed under the MIT License.

## 👥 Team

**Development Team**:
- **Haileab Tesfaye** (ETS0714/14) - SCM Manager & Lead Developer
- **Ephrem Mandefro** (ETS0536/14) - Tester & Change Controller
- **Haileyesus Asrat** (ETS0718/14) - Documenter & Auditor
- **Henok Tademe** (ETS0775/14) - Reviewer & Developer

**GitHub**: [@HenokTade](https://github.com/HenokTade)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

Made with ❤️ by Team: Haileab Tesfaye, Ephrem Mandefro, Haileyesus Asrat, Henok Tademe
