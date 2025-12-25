# Change Request (CR) Form
## Inventory Tracker System

---

### CR Information

**CR ID**: CR-003  
**Date Submitted**: 2024-12-19  
**Submitted By**: Haileab Tesfaye (Lead Developer)  
**Priority**: [ ] Critical  [X] High  [ ] Medium  [ ] Low  
**Type**: [ ] Bug Fix  [ ] Enhancement  [X] New Feature  [ ] Documentation  

---

### Change Description

**Title**: Add User Role Management (RBAC)

**Current Situation**:
The system currently has a single hardcoded user (admin/admin) with full access to all features. There is no differentiation between user types, meaning anyone with login credentials has complete control over the inventory. This poses security risks and doesn't reflect real-world organizational hierarchies where different users need different levels of access.

**Proposed Change**:
Implement Role-Based Access Control (RBAC) with three distinct user roles:

1. **Admin**: Full access - can add, edit, delete items, and manage users
2. **Manager**: Can add and edit items, but cannot delete or manage users
3. **Viewer**: Read-only access - can only view inventory items

Users should be stored in a separate JSON file with their credentials and assigned roles. The UI should adapt based on the logged-in user's role, hiding features they don't have permission to use.

**Justification/Benefits**:
- **Security**: Prevents unauthorized modifications by limiting access
- **Accountability**: Track who can make changes
- **Compliance**: Meets basic access control requirements
- **Organizational Alignment**: Reflects real-world organizational structures
- **Risk Mitigation**: Reduces risk of accidental or malicious data changes
- **Professional Feature**: Expected in enterprise inventory systems

---

### Impact Analysis

**Affected Configuration Items**:
- [X] CI-007: Main Application (`src/app.py`)
- [X] CI-002: Requirements Document
- [ ] CI-003: Installation Guide
- [X] CI-004: User Guide
- [ ] CI-005: Release Notes
- [ ] CI-006: Test Documentation
- [X] CI-008: Login Page
- [X] CI-009: Dashboard Page
- [X] CI-010: Stylesheet
- [X] CI-011: Unit Tests
- [X] CI-012: Data Storage (new users.json file)
- [ ] CI-013: Dependencies
- [ ] CI-014: Git Ignore
- [ ] CI-015: SCMP Document

**Estimated Effort**: 8-10 hours

**Risk Assessment**: [ ] Low  [X] Medium  [ ] High

**Dependencies**:
- Existing authentication system
- Session management
- Current CRUD operations must be functional
- May require password hashing library (werkzeug.security)

---

### Technical Details

**Implementation Approach**:

1. **Data Layer**:
   - Create `users.json` file with structure:
     ```json
     [
       {
         "id": 1,
         "username": "admin",
         "password": "hashed_password",
         "role": "admin"
       }
     ]
     ```
   - Implement password hashing for security
   - Add user management functions

2. **Backend (Flask)**:
   - Update login route to check users.json
   - Store user role in session
   - Create decorator for role-based route protection
   - Add permission checks to edit/delete routes
   - Add user management routes (admin only)

3. **Frontend**:
   - Update dashboard to show/hide buttons based on role
   - Add visual indicators for user role
   - Disable forms for viewers
   - Add user management interface for admins

4. **Security**:
   - Hash passwords using werkzeug.security
   - Validate role on server-side (not just UI)
   - Prevent privilege escalation

**Testing Requirements**:
- Test each role's permissions
- Test unauthorized access attempts
- Test role-based UI rendering
- Test password hashing
- Test session management with roles
- Test admin user management features
- Security testing for privilege escalation

**Documentation Updates Required**:
- [X] User Guide (add "User Roles" section)
- [ ] Installation Guide (default users setup)
- [ ] API Documentation
- [X] README (mention RBAC feature)
- [X] Requirements Document

---

### Review and Approval

**Reviewed By**: Ephrem Mandefro (Change Controller)  
**Review Date**: 2024-12-19  
**Review Comments**:
Critical security and usability enhancement. Implementation is more complex than previous CRs but well-defined. Medium risk due to authentication changes - must ensure existing functionality isn't broken. Requires thorough testing. Benefits outweigh risks. Approved with emphasis on security testing.

**Decision**: [X] Approved  [ ] Rejected  [ ] Deferred  [ ] Needs More Info

**Approved By**: Ephrem Mandefro  
**Approval Date**: 2024-12-19  
**Approval Signature**: E. Mandefro

---

### Implementation

**Assigned To**: Haileab Tesfaye (Lead Developer)  
**Target Completion Date**: 2024-12-21  
**Actual Completion Date**: 2024-12-25  

**Implementation Notes**:
Implemented full RBAC system. Created `users.json` for storage. Added `/users` route for Admin management of users. Updated `app.py` with decorators/checks to enforce Admin/Manager/Viewer permissions strictly. Updated UI to conditionally render elements based on role.

**Git Commit Reference**: `f130c33`

---

### Verification

**Tested By**: Ephrem Mandefro (Tester)  
**Test Date**: 2024-12-25  
**Test Results**: [X] Pass  [ ] Fail

**Verification Notes**:
Verified using `tests/test_cr_implementation.py` (test_cr003_role_access). Confirmed that Viewers cannot access add/edit/delete routes, Managers can add/edit but not delete, and Admins have full access including user management.

---

### Closure

**Status**: [ ] Open  [ ] In Progress  [X] Completed  [ ] Rejected  [ ] Cancelled

**Closed By**: Ephrem Mandefro  
**Closure Date**: 2024-12-25  

**Final Comments**:
[To be filled upon completion]

---

**Document Control**
- **Form Version**: 1.0
- **Last Updated**: December 19, 2024
