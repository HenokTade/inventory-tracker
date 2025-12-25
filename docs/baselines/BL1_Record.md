# Baseline 1 (BL1) Record

**Baseline ID**: BL1  
**Date Established**: December 15, 2024  
**Status**: Approved  
**Purpose**: Repository Setup + Initial Documents + CI List

## Overview
This baseline establishes the foundational structure of the Inventory Tracker System, including the initial repository setup, core documentation, and Configuration Item (CI) register.

## Baseline Contents

### 1. Repository Structure
- Git repository initialized
- `.gitignore` configured for Python projects
- Virtual environment setup (`.venv/`)
- Project directory structure established

### 2. Documentation
- **README.md**: Project overview and quick start guide
- **docs/INSTALLATION.md**: Installation instructions
- **docs/USER_GUIDE.md**: User documentation
- **docs/CI_REGISTER.md**: Configuration Items register
- **docs/SCMP.md**: Software Configuration Management Plan

### 3. Configuration Items (CI)
All items documented in `docs/CI_REGISTER.md`:
- Source code files
- Documentation files
- Configuration files
- Test files
- Data storage files

### 4. Initial Source Code
- `src/app.py`: Flask application entry point
- `src/templates/`: HTML templates (login, dashboard, add_item)
- `src/static/`: CSS stylesheets
- `items.json`: Data storage file

### 5. Development Environment
- `requirements.txt`: Python dependencies
- Virtual environment configuration
- Flask development server setup

## Configuration Management
- **Version Control**: Git
- **Branch Strategy**: Main branch for stable code
- **Access Control**: Repository owner and authorized contributors
- **Change Control**: All changes require documentation and approval

## Verification
- ✅ All files committed to Git repository
- ✅ CI Register complete and accurate
- ✅ Documentation reviewed and approved
- ✅ Repository structure follows standards

## Authorized By
Development Team  
Date: December 15, 2024

---

**Tag**: `BL1`  
**Commit**: Initial repository setup
