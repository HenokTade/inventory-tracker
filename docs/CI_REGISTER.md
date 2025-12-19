# Configuration Item (CI) Register
## Inventory Tracker System - v1.0.0

**Project**: Inventory Tracker System  
**Date**: December 19, 2024  
**Prepared By**: Henok Tade  
**Document Version**: 1.0

---

## CI Register

| CI ID | CI Name | Version | Owner | Category | Status | Location | Description |
|-------|---------|---------|-------|----------|--------|----------|-------------|
| CI-001 | Project README | 1.0.0 | Haileyesus Asrat | Documentation | Approved | `/README.md` | Main project documentation with overview, quick start guide, and structure |
| CI-002 | Requirements Document | 1.0.0 | Haileyesus Asrat | Documentation | Approved | `/docs/README.md` | Project requirements and feature specifications |
| CI-003 | Installation Guide | 1.0.0 | Haileyesus Asrat | Documentation | Approved | `/docs/INSTALLATION.md` | Setup and installation instructions |
| CI-004 | User Guide | 1.0.0 | Haileyesus Asrat | Documentation | Approved | `/docs/USER_GUIDE.md` | End-user documentation and usage instructions |
| CI-005 | Release Notes | 1.0.0 | Haileab Tesfaye | Documentation | Approved | `/releases/v1.0.0.md` | Version 1.0.0 release documentation |
| CI-006 | Test Documentation | 1.0.0 | Ephrem Mandefro | Documentation | Approved | `/tests/README.md` | Testing procedures and guidelines |
| CI-007 | Main Application | 1.0.0 | Haileab Tesfaye | Source Code | Approved | `/src/app.py` | Flask application backend (Python) |
| CI-008 | Login Page | 1.0.0 | Haileab Tesfaye | UI/Frontend | Approved | `/src/templates/login.html` | User authentication interface (HTML) |
| CI-009 | Dashboard Page | 1.0.0 | Haileab Tesfaye | UI/Frontend | Approved | `/src/templates/dashboard.html` | Main inventory dashboard interface (HTML) |
| CI-010 | Stylesheet | 1.0.0 | Henok Tademe | UI/Frontend | Approved | `/src/static/style.css` | Application styling (CSS) |
| CI-011 | Unit Tests | 1.0.0 | Ephrem Mandefro | Test Code | Approved | `/tests/test_app.py` | Automated test suite (Python) |
| CI-012 | Data Storage | 1.0.0 | Henok Tademe | Database | Active | `/items.json` | JSON-based inventory database |
| CI-013 | Dependencies | 1.0.0 | Haileab Tesfaye | Configuration | Approved | `/requirements.txt` | Python package dependencies |
| CI-014 | Git Ignore | 1.0.0 | Haileab Tesfaye | Configuration | Approved | `/.gitignore` | Version control exclusions |
| CI-015 | SCMP Document | 1.0.0 | Haileyesus Asrat | Documentation | Approved | `/docs/SCMP.md` | Software Configuration Management Plan |
| CI-016 | CI Register | 1.0.0 | Haileyesus Asrat | Documentation | Approved | `/docs/CI_REGISTER.md` | Configuration Item tracking register |
| CI-017 | Change Log | 1.0.0 | Ephrem Mandefro | Documentation | Approved | `/docs/CHANGE_LOG.md` | Change Request tracking log |

---

## CI Categories

### Documentation
- Project README (CI-001)
- Requirements Document (CI-002)
- Installation Guide (CI-003)
- User Guide (CI-004)
- Release Notes (CI-005)
- Test Documentation (CI-006)
- SCMP Document (CI-015)

### Source Code
- Main Application (CI-007)

### UI/Frontend
- Login Page (CI-008)
- Dashboard Page (CI-009)
- Stylesheet (CI-010)

### Test Code
- Unit Tests (CI-011)

### Database
- Data Storage (CI-012)

### Configuration
- Dependencies (CI-013)
- Git Ignore (CI-014)

---

## CI Status Definitions

| Status | Description |
|--------|-------------|
| **Draft** | CI is under development, not yet reviewed |
| **Under Review** | CI is complete and awaiting approval |
| **Approved** | CI has been reviewed and approved for use |
| **Active** | CI is currently in use in production |
| **Deprecated** | CI is no longer recommended for use |
| **Archived** | CI has been retired and archived |

---

## Version Control

All Configuration Items are tracked in Git repository:
- **Repository**: https://github.com/HenokTade/inventory-tracker
- **Branch**: main
- **Latest Commit**: 30151a8

### Commit History
1. `1544d3c` - Initial commit: Inventory Tracker application
2. `dcead60` - Initial project structure with docs, src, tests, and releases directories
3. `2517f38` - Move application code to src directory
4. `5b39c23` - Add release notes and update gitignore
5. `30151a8` - Add main README file

---

## Change Control Process

1. **Identification**: All CIs must be registered in this document
2. **Version Control**: All changes tracked via Git commits
3. **Review**: Changes require review before approval
4. **Approval**: Owner approves changes to CIs
5. **Release**: Approved CIs are released with version tags

---

## CI Ownership

### Team-Based Ownership

**SCM Manager & Lead Developer**: Haileab Tesfaye (ETS0714/14)
- Owns: Source code CIs, configuration files, release notes
- Approves: Merges, baselines, and releases

**Tester & Change Controller**: Ephrem Mandefro (ETS0536/14)
- Owns: Test code, test documentation, change log
- Approves: Change requests and test completions

**Documenter & Auditor**: Haileyesus Asrat (ETS0718/14)
- Owns: Documentation CIs, CI Register, SCMP
- Approves: Documentation updates and audit reports

**Reviewer & Developer**: Henok Tademe (ETS0775/14)
- Owns: UI/Frontend styling, data storage
- Approves: Code reviews and minor updates

---

## Notes

- All source code CIs are version-controlled using Git
- Database file (items.json) is dynamically updated during runtime
- Configuration items follow semantic versioning (MAJOR.MINOR.PATCH)
- SCMP document (CI-015) is currently in draft status and requires completion

---

**Document Control**
- **Created**: December 19, 2024
- **Last Updated**: December 19, 2024
- **Next Review**: As needed with new releases
