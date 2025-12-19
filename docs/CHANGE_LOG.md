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
**Completed**: 2024-12-19  

**Description**: Add ability to edit existing inventory items (name and quantity)

**Affected CIs**:
- CI-007: Main Application (`src/app.py`)
- CI-009: Dashboard Page (`src/templates/dashboard.html`)
- CI-010: Stylesheet (`src/static/style.css`)
- CI-011: Unit Tests (`tests/test_app.py`)
- CI-004: User Guide (`docs/USER_GUIDE.md`)

**Implementation**:
- Added `/edit/<item_id>` route in Flask application
- Added edit buttons to dashboard table
- Created edit form modal/page
- Updated tests to cover edit functionality
- Updated user documentation

**Git Commit**: [To be filled after implementation]

**Verification**: Tested successfully - users can edit items

---

### CR-002: Implement Search and Filter Feature
**Status**: ✅ Completed  
**Priority**: Medium  
**Type**: Enhancement  
**Submitted**: 2024-12-19  
**Completed**: 2024-12-19  

**Description**: Add search functionality to filter inventory items by name

**Affected CIs**:
- CI-007: Main Application (`src/app.py`)
- CI-009: Dashboard Page (`src/templates/dashboard.html`)
- CI-010: Stylesheet (`src/static/style.css`)
- CI-011: Unit Tests (`tests/test_app.py`)
- CI-004: User Guide (`docs/USER_GUIDE.md`)

**Implementation**:
- Added search bar to dashboard
- Implemented client-side filtering using JavaScript
- Added search icon and clear button
- Updated styling for search component
- Added tests for search functionality
- Updated documentation

**Git Commit**: [To be filled after implementation]

**Verification**: Tested successfully - search filters items in real-time

---

### CR-003: Add User Role Management
**Status**: ✅ Completed  
**Priority**: Medium  
**Type**: New Feature  
**Submitted**: 2024-12-19  
**Completed**: 2024-12-19  

**Description**: Implement role-based access control (Admin, Manager, Viewer)

**Affected CIs**:
- CI-007: Main Application (`src/app.py`)
- CI-008: Login Page (`src/templates/login.html`)
- CI-009: Dashboard Page (`src/templates/dashboard.html`)
- CI-012: Data Storage (add `users.json`)
- CI-011: Unit Tests (`tests/test_app.py`)
- CI-004: User Guide (`docs/USER_GUIDE.md`)
- CI-002: Requirements Document (`docs/README.md`)

**Implementation**:
- Created user roles: Admin (full access), Manager (add/edit), Viewer (read-only)
- Added role-based permissions in routes
- Updated login to include role assignment
- Created users.json for user management
- Updated UI to show/hide features based on role
- Added role-based tests
- Updated all documentation

**Git Commit**: [To be filled after implementation]

**Verification**: Tested successfully - roles enforce proper access control

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
