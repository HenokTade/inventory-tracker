# Tests Directory

## Overview
This directory contains unit tests for the Inventory Tracker application.

## Running Tests

### Run All Tests
```bash
python -m pytest tests/
```

Or using unittest:
```bash
python -m unittest discover tests/
```

### Run Specific Test File
```bash
python -m pytest tests/test_app.py
```

### Run with Coverage
```bash
python -m pytest --cov=src tests/
```

## Test Structure

### test_app.py
Contains unit tests for the main application functionality:
- **Authentication Tests**: Login/logout functionality
- **Route Tests**: Endpoint accessibility and redirects
- **Data Tests**: Item loading and saving operations

## Test Coverage
Current test coverage includes:
- ✅ Login page rendering
- ✅ Valid/invalid authentication
- ✅ Dashboard access control
- ✅ Data persistence (load/save)
- ✅ Logout functionality
- ✅ Route redirects

## Adding New Tests
When adding new features, please add corresponding tests:
1. Create test methods in `test_app.py`
2. Follow naming convention: `test_<feature_name>`
3. Use descriptive docstrings
4. Ensure tests are independent

## Dependencies
Tests require:
- `unittest` (built-in)
- `pytest` (optional, for better output)
- `pytest-cov` (optional, for coverage reports)

Install test dependencies:
```bash
pip install pytest pytest-cov
```
