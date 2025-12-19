# Software Configuration Management Plan (SCMP)
## Inventory Tracker System

**Project**: Inventory Tracker System  
**Version**: 1.0  
**Date**: December 19, 2024  
**Prepared By**: Henok Tade

---

## 1. Introduction

### 1.1 Purpose
This Software Configuration Management Plan (SCMP) defines the configuration management activities for the Inventory Tracker System project. It establishes the procedures for identifying, controlling, tracking, and auditing all configuration items throughout the software development lifecycle.

### 1.2 Scope
This plan applies to all software components, documentation, and related artifacts of the Inventory Tracker System, including:
- Source code files
- Documentation
- Test files
- Configuration files
- Database files
- UI mockups and designs

### 1.3 Definitions
- **CI (Configuration Item)**: Any artifact that is placed under configuration management
- **Baseline**: A formally approved version of a configuration item
- **Version**: A specific state of a configuration item
- **Repository**: Git-based version control system

---

## 2. Configuration Management Organization

### 2.1 Team Structure

**Project**: Inventory Tracker System  
**Team Size**: 4 Members  
**Organization**: Collaborative development with defined roles

### 2.2 Roles and Responsibilities

#### SCM Manager & Lead Developer
**Name**: Haileab Tesfaye  
**ID**: ETS0714/14  
**Responsibilities**:
- Oversee SCMP implementation and compliance
- Manage baselines and version releases
- Lead coding efforts (app.py, frontend files)
- Coordinate team activities
- Ensure configuration management procedures are followed

**Authority**:
- Approve merges to main branch
- Resolve merge conflicts
- Tag baselines and releases
- Final approval on major architectural decisions

---

#### Tester & Change Controller
**Name**: Ephrem Mandefro  
**ID**: ETS0536/14  
**Responsibilities**:
- Test changes for functionality and quality
- Process and track Change Requests (CRs)
- Maintain Change Log documentation
- Verify implementations meet requirements
- Conduct functional testing

**Authority**:
- Review and approve/reject Change Requests
- Verify implementations before merges
- Sign off on test completion
- Request changes or improvements

---

#### Documenter & Auditor
**Name**: Haileyesus Asrat  
**ID**: ETS0718/14  
**Responsibilities**:
- Prepare and update all documentation
- Maintain CI Register
- Conduct configuration audits
- Generate audit reports
- Ensure documentation accuracy and completeness

**Authority**:
- Update documentation Configuration Items
- Report audit findings to team
- Request documentation improvements
- Approve documentation changes

---

#### Reviewer & Developer
**Name**: Henok Tademe  
**ID**: ETS0775/14  
**Responsibilities**:
- Review pull requests and code changes
- Review documentation for accuracy
- Assist in development (JSON handling, CSS styling)
- Provide technical feedback
- Support testing activities

**Authority**:
- Provide feedback on pull requests
- Commit to feature branches
- Request code improvements
- Approve minor documentation updates

---

## 3. Configuration Identification

### 3.1 Configuration Items
All CIs are documented in the CI Register (`docs/CI_REGISTER.md`), including:
- CI name and unique identifier
- Version number
- Owner
- Category (Documentation, Source Code, UI/Frontend, Test Code, Database, Configuration)
- Status (Draft, Under Review, Approved, Active, Deprecated, Archived)

### 3.2 Naming Conventions

#### Files
- Use lowercase with underscores for Python files: `test_app.py`
- Use descriptive names for HTML templates: `login.html`, `dashboard.html`
- Use UPPERCASE for documentation: `README.md`, `INSTALLATION.md`

#### Versions
- Follow semantic versioning: `MAJOR.MINOR.PATCH`
- Example: `1.0.0`, `1.1.0`, `2.0.0`

#### Git Branches
- `main` - Production-ready code
- `develop` - Development branch (if needed)
- `feature/*` - Feature branches
- `bugfix/*` - Bug fix branches

---

## 4. Configuration Control

### 4.1 Change Control Process

1. **Change Request**
   - Identify the need for change
   - Document the change requirement

2. **Impact Analysis**
   - Assess impact on existing CIs
   - Identify affected components

3. **Approval**
   - Configuration Manager reviews change
   - Approve or reject the change request

4. **Implementation**
   - Developer implements approved changes
   - Update version numbers as needed
   - Commit changes with descriptive messages

5. **Verification**
   - Run automated tests
   - Verify functionality
   - Update documentation

6. **Release**
   - Merge to main branch
   - Tag release version
   - Update CI Register

### 4.2 Version Control

#### Git Repository
- **Platform**: GitHub
- **Repository URL**: https://github.com/HenokTade/inventory-tracker
- **Primary Branch**: `main`

#### Commit Message Format
```
<type>: <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions or modifications
- `refactor`: Code refactoring
- `style`: Code style changes (formatting)
- `chore`: Maintenance tasks

**Example**:
```
feat: Add user authentication system

Implemented login functionality with session management.
Added login.html template and authentication routes.

Closes #123
```

### 4.3 Baseline Management

#### Baselines
- **Initial Baseline**: v1.0.0 (Commit: 30151a8)
- **Future Baselines**: Tagged releases (v1.1.0, v2.0.0, etc.)

#### Baseline Approval
- All baselines require Configuration Manager approval
- Baselines are tagged in Git with version numbers
- Release notes document each baseline

---

## 5. Configuration Status Accounting

### 5.1 Tracking
- All changes tracked via Git commit history
- CI Register maintained in `docs/CI_REGISTER.md`
- Release notes in `releases/` directory

### 5.2 Reporting
- **Weekly**: Review commit activity
- **Monthly**: Update CI Register
- **Per Release**: Create release notes

### 5.3 Metrics
- Number of commits per week
- Number of CIs under management
- Number of open/closed issues
- Test coverage percentage

---

## 6. Configuration Audits

### 6.1 Physical Audit
- Verify all CIs exist in repository
- Check file integrity
- Validate directory structure

### 6.2 Functional Audit
- Verify functionality matches documentation
- Run automated test suite
- Validate user acceptance criteria

### 6.3 Audit Schedule
- **Pre-Release**: Before each version release
- **Quarterly**: Every 3 months
- **Ad-hoc**: As needed for major changes

---

## 7. Tools and Infrastructure

### 7.1 Version Control
- **Tool**: Git
- **Platform**: GitHub
- **Access**: Repository owner and authorized contributors

### 7.2 Development Tools
- **IDE**: Visual Studio Code (or equivalent)
- **Language**: Python 3.7+
- **Framework**: Flask 2.0+
- **Testing**: pytest, unittest

### 7.3 Documentation Tools
- **Format**: Markdown (.md)
- **Storage**: Git repository (`/docs` directory)

---

## 8. Backup and Recovery

### 8.1 Backup Strategy
- **Primary**: Git repository on GitHub (cloud-based)
- **Local**: Developer workstation clones
- **Frequency**: Continuous (with each push)

### 8.2 Recovery Procedures
1. Clone repository from GitHub
2. Checkout specific version/tag if needed
3. Restore dependencies: `pip install -r requirements.txt`
4. Verify functionality with test suite

---

## 9. Training and Resources

### 9.1 Training Requirements
- Git version control basics
- Python and Flask development
- Testing procedures
- Documentation standards

### 9.2 Resources
- Git documentation: https://git-scm.com/doc
- Flask documentation: https://flask.palletsprojects.com/
- Project documentation: `/docs` directory

---

## 10. Compliance and Standards

### 10.1 Standards
- PEP 8 for Python code style
- Semantic versioning for releases
- Markdown for documentation

### 10.2 Quality Assurance
- Code reviews before merging
- Automated testing required
- Documentation updates mandatory

---

## 11. Appendices

### Appendix A: CI Register
See `docs/CI_REGISTER.md` for complete CI listing

### Appendix B: Directory Structure
```
inventory-tracker/
├── docs/              # Documentation
├── src/               # Source code
├── tests/             # Test files
├── releases/          # Release notes
├── .gitignore         # Git exclusions
├── README.md          # Project overview
├── requirements.txt   # Dependencies
└── items.json         # Database
```

### Appendix C: Contact Information

**SCM Manager**: Haileab Tesfaye (ETS0714/14)  
**Change Controller**: Ephrem Mandefro (ETS0536/14)  
**Documenter**: Haileyesus Asrat (ETS0718/14)  
**Reviewer**: Henok Tademe (ETS0775/14)  
**GitHub Repository**: https://github.com/HenokTade/inventory-tracker

---

**Document Approval**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| SCM Manager | Haileab Tesfaye | _________ | Dec 19, 2024 |
| Change Controller | Ephrem Mandefro | _________ | Dec 19, 2024 |
| Documenter | Haileyesus Asrat | _________ | Dec 19, 2024 |
| Reviewer | Henok Tademe | _________ | Dec 19, 2024 |

---

**Document Control**
- **Version**: 1.0
- **Status**: Draft
- **Created**: December 19, 2024
- **Last Updated**: December 19, 2024
- **Next Review**: January 19, 2025
