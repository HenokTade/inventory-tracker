# Change Log
## Inventory Tracker System

**Project**: Inventory Tracker System  
**Maintained By**: Ephrem Mandefro (Change Controller)  
**Team**: Haileab Tesfaye, Ephrem Mandefro, Haileyesus Asrat, Henok Tademe  
**Last Updated**: December 19, 2024

---

## Summary

| Status | Count |
|--------|-------|
| Open | 0 |
| In Progress | 0 |
| Completed | 3 |
| Rejected | 0 |
| **Total** | **3** |

---

## Change Requests

### CR-001: Add Item Editing Functionality
**Status**: ✅ Completed  
**Priority**: High  
**Type**: New Feature  
**Submitted**: 2024-12-19  
**Completed**: 2024-12-25  

**Description**: Add ability to edit existing inventory items (name and quantity)

**Affected CIs**:
- CI-007: Main Application (`src/app.py`)
- CI-009: Dashboard Page (`src/templates/dashboard.html`)
- CI-010: Stylesheet (`src/static/style.css`)
- CI-020: CR Tests (`tests/test_cr_implementation.py`)
- CI-004: User Guide (`docs/USER_GUIDE.md`)

**Implementation**:
- Added `/edit/<item_id>` route in Flask application
- Added edit buttons to dashboard table
- Created edit form modal
- Added audit trail (last_modified, modified_by)
- Updated tests to cover edit functionality

**Git Commit**: `f130c33`

**Verification**: Verified via unit tests (`test_cr001_edit_item`) and manual testing.

---

### CR-002: Implement Search and Filter Feature
**Status**: ✅ Completed  
**Priority**: Medium  
**Type**: Enhancement  
**Submitted**: 2024-12-19  
**Completed**: 2024-12-25  

**Description**: Add search functionality to filter inventory items by name and quantity

**Affected CIs**:
- CI-007: Main Application (`src/app.py`)
- CI-009: Dashboard Page (`src/templates/dashboard.html`)
- CI-020: CR Tests (`tests/test_cr_implementation.py`)
- CI-004: User Guide (`docs/USER_GUIDE.md`)

**Implementation**:
- Added search bar and quantity filter to dashboard
- Implemented real-time search with JavaScript auto-submit
- Updated backend to handle search query params
- Added tests for search functionality

**Git Commit**: `f130c33`

**Verification**: Verified via unit tests (`test_cr002_search_filter`) and manual testing.

---

### CR-003: Add User Role Management
**Status**: ✅ Completed  
**Priority**: Medium  
**Type**: New Feature  
**Submitted**: 2024-12-19  
**Completed**: 2024-12-25  

**Description**: Implement role-based access control (Admin, Manager, Viewer)

**Affected CIs**:
- CI-007: Main Application (`src/app.py`)
- CI-008: Login Page (`src/templates/login.html`)
- CI-009: Dashboard Page (`src/templates/dashboard.html`)
- CI-018: User Management Page (`src/templates/users.html`)
- CI-019: User Data (`users.json`)
- CI-020: CR Tests (`tests/test_cr_implementation.py`)

**Implementation**:
- Created user roles: Admin (full access), Manager (add/edit), Viewer (read-only)
- Added strict permission checks in all routes
- Implemented `users.json` for persistent user storage
- Added User Management interface for Admins
- Updated UI to adapt to user roles

**Git Commit**: `f130c33`

**Verification**: Verified via unit tests (`test_cr003_role_access`) and manual testing.

---

## Change Request Statistics

### By Priority
- **Critical**: 0
- **High**: 1 (CR-001)
- **Medium**: 2 (CR-002, CR-003)
- **Low**: 0

### By Type
- **New Feature**: 2 (CR-001, CR-003)
- **Enhancement**: 1 (CR-002)
- **Bug Fix**: 0
- **Documentation**: 0

### By Status
- **Completed**: 3
- **In Progress**: 0
- **Open**: 0
- **Rejected**: 0

---

## Approval History

| CR ID | Submitted By | Reviewed By | Approved By | Approval Date | Status |
|-------|--------------|-------------|-------------|---------------|--------|
| CR-001 | Haileab Tesfaye | Ephrem Mandefro | Ephrem Mandefro | 2024-12-19 | Approved |
| CR-002 | Henok Tademe | Ephrem Mandefro | Ephrem Mandefro | 2024-12-19 | Approved |
| CR-003 | Haileab Tesfaye | Ephrem Mandefro | Ephrem Mandefro | 2024-12-19 | Approved |

---

## Implementation Timeline

```
Dec 19, 2024
├── CR-001: Item Editing - Submitted & Approved
├── CR-002: Search/Filter - Submitted & Approved
└── CR-003: Role Management - Submitted & Approved
```

---

## Notes

- All change requests follow the standard CR form template
- Each CR undergoes impact analysis before approval
- Implementation includes code, tests, and documentation updates
- All changes are tracked in Git version control
- Change requests are linked to affected Configuration Items

---

**Document Control**
- **Version**: 1.0
- **Created**: December 19, 2024
- **Last Updated**: December 19, 2024
- **Next Review**: With each new CR submission
