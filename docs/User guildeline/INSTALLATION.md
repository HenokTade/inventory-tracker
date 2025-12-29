# Installation Guide

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## Installation Steps

### 1. Clone the Repository
```bash
git clone <repository-url>
cd inventory-tracker
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
python src/app.py
```

The application will start on `http://localhost:5000`

## Default Credentials
- **Username**: admin
- **Password**: admin

> ⚠️ **Security Note**: Change these credentials in production environments!

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify the last line in `src/app.py`:
```python
app.run(debug=True, port=5001)
```

### Missing Dependencies
Ensure all dependencies are installed:
```bash
pip install flask
```

### Data File Issues
If `items.json` is corrupted, delete it and restart the application. A new file will be created automatically.
