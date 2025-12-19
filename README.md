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
- **Username**: `admin`
- **Password**: `admin`

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
│   └── static/
├── tests/             # 🧪 Unit tests
│   ├── test_app.py
│   └── README.md
├── releases/          # 📋 Release notes
│   └── v1.0.0.md
├── items.json         # 💾 Data storage
└── requirements.txt   # 📦 Dependencies
```

## ✨ Features

- ✅ **Secure Authentication** - Login system with session management
- ✅ **Inventory Dashboard** - View all items in organized table
- ✅ **Add Items** - Quick form to add new inventory items
- ✅ **Data Persistence** - Automatic JSON-based storage
- ✅ **Responsive Design** - Clean, modern UI

## 📖 Documentation

- **[Installation Guide](docs/INSTALLATION.md)** - Setup instructions
- **[User Guide](docs/USER_GUIDE.md)** - How to use the system
- **[Release Notes](releases/v1.0.0.md)** - Version history

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

## 👤 Author

**Henok Tade**
- GitHub: [@HenokTade](https://github.com/HenokTade)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

Made with ❤️ by Henok Tade
