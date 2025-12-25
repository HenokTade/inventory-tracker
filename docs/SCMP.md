# Software Configuration Management Plan (SCMP)
## Inventory Tracker System

**Project**: Inventory Tracker System  
**Version**: 1.2  
**Date**: December 25, 2024  
**Prepared By**: Henok Tade (Reviewer & Developer)  
**Approved By**: Haileab Tesfaye (SCM Manager)

---

## 1. Introduction

### 1.1 Purpose
The purpose of this Software Configuration Management Plan (SCMP) is to define the configuration management activities for the Inventory Tracker System project. It establishes the procedures for identifying, controlling, tracking, and auditing all configuration items (CIs) throughout the software development lifecycle to ensure product integrity.

### 1.2 Scope
This plan applies to all software components, documentation, and related artifacts of the Inventory Tracker System.
**In Scope:**
*   Source code (`src/`)
*   Documentation (`docs/`, `README.md`)
*   Test suites (`tests/`)
*   Configuration and Data files (`items.json`, `users.json`, `requirements.txt`)
*   Release artifacts (`releases/`)

### 1.3 Organizational Relationships
The Inventory Tracker System is developed by a collaborative student team. The SCM Manager reports to the Project Lead (if applicable) or academic supervisor. All team members (Developers, Testers, Documenters) interact directly with the SCM process.
*   **Developers** submit changes to SCM.
*   **Testers** verify CIs managed by SCM.
*   **Auditors** review SCM records.

### 1.4 References
*   IEEE Std 828-2012, *IEEE Standard for Configuration Management in Systems and Software Engineering*.
*   Inventory Tracker System *Requirements Document* (CI-002).
*   Inventory Tracker System *Project Plan*.

---

## 2. Criteria for Identification

### 2.1 Configuration Items (CIs)
All CIs are uniquely identified and tracked in the **CI Register** (`docs/CI_REGISTER.md`).
Key CI Categories include:
*   **Source Code**: `app.py`, HTML templates, CSS styles.
*   **Data**: `items.json` (Inventory), `users.json` (Users).
*   **Docs**: Plans, Reports, Guides.

### 2.2 Naming Conventions
*   **Files**: Snake case for scripts (`test_app.py`), kebab-case for CSS/HTML (`style.css`), UPPERCASE for root docs (`README.md`).
*   **Releases**: `vX.Y.Z` (e.g., `v1.1.0`).
*   **Baselines**: `BL<Number>` (e.g., `BL1`, `BL2`).

### 2.3 Versioning Rules
The project follows **Semantic Versioning (SemVer)**: `MAJOR.MINOR.PATCH`.
*   **MAJOR**: Incompatible API changes.
*   **MINOR**: Backwards-compatible functionality (e.g., New Features).
*   **PATCH**: Backwards-compatible bug fixes.

### 2.4 Branching Model
*   **`main`**: Verified, production-ready code. Protected branch.
*   **`develop`**: Integration branch for ongoing work (optional).
*   **`feature/<name>`**: For new capabilities (e.g., `feature/role-management`).
*   **`bugfix/<name>`**: For verifying and fixing defects.
*   **`docs/<name>`**: For documentation updates.

---

## 3. Limitations & Assumptions

### 3.1 Assumptions
*   All team members have access to the GitHub repository.
*   GitHub Actions (or manual execution) is sufficient for CI checks.
*   The team consists of 4 members performing distinct but overlapping roles.

### 3.2 Limitations
*   No external QA team; peer testing is utilized.
*   SCM acts as the primary release mechanism (no separate deployment pipeline).
*   Data files (`json`) are part of the repo for this prototype (not suitable for large-scale production).

---

## 4. CM Responsibilities & Authorities

### 4.1 SCM Manager (Haileab Tesfaye)
*   **Responsibilities**: Implementation of SCMP, Baseline management, Release tagging.
*   **Authority**: Approval of merges to `main`, Start/End of SCM Audits, Final Release decision.

### 4.2 Change Controller (Ephrem Mandefro)
*   **Responsibilities**: Evaluation of Change Requests (CRs), Change Log maintenance.
*   **Authority**: Approval/Rejection of CRs, Verification of implementation completeness.

### 4.3 Auditor (Haileyesus Asrat)
*   **Responsibilities**: Conducting PCA/FCA, Updating CI Register, Verifying documentation.
*   **Authority**: Flagging non-compliance, Requiring documentation updates.

### 4.4 Developer/Reviewer (Henok Tademe)
*   **Responsibilities**: Adhering to SCM procedures, Peer reviews, Creating feature branches.
*   **Authority**: Technical recommendation on Changes, Code review approval.

---

## 5. Project Organization

### 5.1 Structure
The project operates as a flat team structure with functional roles assigned for SCM purposes.

### 5.2 CM Interfaces
*   **GitHub**: Central repository for all code and docs. Acts as the Single Source of Truth.
*   **VS Code**: Primary development interface.
*   **Communication Channels**: Team meetings for Change Control Board (CCB) decisions.

---

## 6. Applicable Policies & Procedures

### 6.1 Change Control Process
1.  **Request**: Submit CR (Issue/Document).
2.  **Assess**: Change Controller analyzes impact.
3.  **Approve/Reject**: CCB decision.
4.  **Implement**: Branch -> Code -> Test.
5.  **Verify**: Tester confirms checks pass.
6.  **Close**: Merge to `main` update logs.

### 6.2 Baseline Management
Baselines are immutable reference points.
*   **Creation**: At major milestones (e.g., "Prototype Complete", "Release Candidate").
*   **Identification**: Tagged in Git (e.g., `BL1`, `BL2`).
*   **Current Baseline**: `BL2` (Corresponds to v1.1.0).

### 6.3 Configuration Audits
*   **Functional Configuration Audit (FCA)**: Verifies that the CIs function as intended and meet requirements (Tests passed?).
*   **Physical Configuration Audit (PCA)**: Verifies that the CIs match the documentation and directory structure.
*   **Schedule**: Before every major release.

### 6.4 Backup & Recovery
*   **Backup**: Continuous via GitHub remote. Local clones serve as distributed backups.
*   **Recovery**: `git checkout <tag>` to restore any previous baseline state.

---

## 7. Planned Activities

### 7.1 Schedules & Milestones
*   **Phase 1 (Setup)**: repository init, CI definitions. (Completed: Dec 19)
*   **Phase 2 (Prototype)**: v1.0.0 (Completed: Dec 19)
*   **Phase 3 (Features)**: v1.1.0 (CR-001/002/003) (Completed: Dec 25)
*   **Phase 4 (Refinement)**: Final Audit & Handoff (Current)

### 7.2 SCMP Resources (Tools Used)
*   **Version Control**: Git (2.x+)
*   **Repository Hosting**: GitHub
*   **Editor**: Visual Studio Code
*   **Language Runtime**: Python 3.12+ (Flask)
*   **Documentation**: Markdown

---

## 8. CMP Maintenance

### 8.1 Update Mechanism
This SCMP is a living document. It shall be reviewed:
*   At the start of each new development phase.
*   When major SCM tools or procedures change.
*   If Audit findings suggest process deficiencies.

### 8.2 Review Process
Updates to the SCMP require review by the SCM Manager and Change Controller before being committed as a new version.

---

**Document Approval**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| SCM Manager | Haileab Tesfaye | Dec 25, 2024 | *Signed* |
| Change Controller | Ephrem Mandefro | Dec 25, 2024 | *Signed* |
