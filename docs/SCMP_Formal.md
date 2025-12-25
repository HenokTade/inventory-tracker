<div align="center">

# SOFTWARE CONFIGURATION MANAGEMENT PLAN (SCMP)

## INVENTORY TRACKER SYSTEM

<br>
<br>

**Document Version:** 1.2  
**Date:** December 25, 2024  
**Project ID:** ITS-2024-001  

<br>
<br>
<br>

**Prepared By:**  
Henok Tade  
*Reviewer & Developer*

<br>

**Approved By:**  
Haileab Tesfaye  
*SCM Manager*

</div>
<div style="page-break-after: always;"></div>

## TABLE OF CONTENTS

1. [Introduction](#1-introduction)
    1.1 Purpose
    1.2 Scope
    1.3 Definitions and Acronyms
    1.4 References
2. [SCM Management](#2-scm-management)
    2.1 Organization
    2.2 SCM Responsibilities
    2.3 Applicable Policies
3. [SCM Activities](#3-scm-activities)
    3.1 Configuration Identification
    3.2 Configuration Control
    3.3 Configuration Status Accounting
    3.4 Configuration Audits
4. [Release Management](#4-release-management)
    4.1 Release Process
    4.2 Backup and Recovery
5. [Tools and Resources](#5-tools-and-resources)
6. [Maintenance](#6-maintenance)

<div style="page-break-after: always;"></div>

## 1. INTRODUCTION

### 1.1 Purpose
The purpose of this Software Configuration Management Plan (SCMP) is to establish a structured and disciplined methodology for managing the evolution of the **Inventory Tracker System**. This plan defines the processes for identifying, controlling, tracking, and auditing all software artifacts to ensure system integrity, reproducibility, and traceability throughout the development lifecycle.

This document serves as the central reference for all configuration management activities, adhering to the standards outlined in **IEEE Std 828-2012**.

### 1.2 Scope
This SCMP applies to the entire Inventory Tracker System project, covering all phases from initial development to final release and maintenance.

The scope includes the management of the following artifacts:
*   **Source Code**: All Python scripts, HTML templates, CSS stylesheets, and JavaScript files.
*   **Documentation**: Project plans, requirement specifications, user guides, and installation manuals.
*   **Test Artifacts**: Test scripts, test data, and test reports.
*   **Data Files**: Initial database schemas and default configuration data (`items.json`, `users.json`).
*   **Build & Release Artifacts**: Executables, distribution packages, and release notes.

**Out of Scope:**
*   Hardware configuration management.
*   Personal development environments (except where they impact the shared repository).

### 1.3 Definitions and Acronyms
*   **CCB (Change Control Board)**: The group responsible for approving or rejecting changes.
*   **CI (Configuration Item)**: An aggregation of hardware, software, or both, that is designated for configuration management and treated as a single entity in the configuration management process.
*   **CM (Configuration Management)**: A discipline applying technical and administrative direction and surveillance to identify and document the functional and physical characteristics of a configuration item, control changes to those characteristics, record and report change processing and implementation status, and verify compliance with specified requirements.
*   **FCA (Functional Configuration Audit)**: An audit conducted to verify that the development of a configuration item has been completed satisfactorily, that the item has achieved the performance and functional characteristics specified in the functional or allocated configuration identification, and that its operational and support documents are complete and satisfactory.
*   **PCA (Physical Configuration Audit)**: An audit conducted to verify that a configuration item, as built, conforms to the technical documentation that defines it.

### 1.4 References
1.  IEEE Std 828-2012, *IEEE Standard for Configuration Management in Systems and Software Engineering*.
2.  *Inventory Tracker System Requirements Specification*, Version 1.1.
3.  *Inventory Tracker System Project Management Plan*, Version 1.0.

<div style="page-break-after: always;"></div>

## 2. SCM MANAGEMENT

### 2.1 Organization
The SCM function is integrated directly into the development team structure. Due to the agile nature of the project and the team size (4 members), SCM roles are assigned to specific team members to ensure accountability without creating excessive bureaucracy.

The **Change Control Board (CCB)** consists of the SCM Manager and the Change Controller. For critical changes affecting the core architecture, the entire team participates in the CCB.

### 2.2 SCM Responsibilities

| Role | Assigned To | Responsibilities | Authority |
| :--- | :--- | :--- | :--- |
| **SCM Manager** | **Haileab Tesfaye** | • Planning and execution of SCMP<br>• Managing the main repository<br>• Creating official baselines<br>• Chairing the CCB | • Approve/Reject Merges to `main`<br>• Final Decision on Releases<br>• Approving SCM Audits |
| **Change Controller** | **Ephrem Mandefro** | • Receiving and logging CRs<br>• Tracking change status<br>• verifying implementation completeness | • Approve/Reject Change Requests<br>• Request rework on changes |
| **Auditor** | **Haileyesus Asrat** | • Conducting FCA and PCA<br>• Maintaining the CI Register<br>• Verifying documentation consistency | • Flag non-compliance issues<br>• Halt release if audit fails |
| **Reviewer** | **Henok Tade** | • Technical code review<br>• Creating feature branches<br>• Merging safe changes | • Recommend technical approaches<br>• Reject poor quality code |

### 2.3 Applicable Policies
*   **Single Source of Truth**: The GitHub repository’s `main` branch is the only official source of valid code.
*   **No Direct Commits**: All changes must be made via Pull Requests (PRs) originating from Feature or Bugfix branches. Direct commits to `main` are strictly prohibited.
*   **Review Requirement**: Every PR requires at least one approval from a designated Reviewer before merging.
*   **Test-Driven Integration**: No code shall be merged unless corresponding unit tests (where applicable) pass successfully.

<div style="page-break-after: always;"></div>

## 3. SCM ACTIVITIES

### 3.1 Configuration Identification

#### 3.1.1 Configuration Items (CIs)
The following artifacts are identified as CIs and tracked in the CI Register:

| CI Category | Description | Naming Convention | Example |
| :--- | :--- | :--- | :--- |
| **Source Code** | Implementation files | `snake_case.ext` | `app.py`, `utils.py` |
| **Templates** | HTML UI files | `descriptive_name.html` | `login.html`, `dashboard.html` |
| **Documentation** | Reports & Guides | `UPPER_CASE.md` | `README.md`, `SCMP.md` |
| **Test Code** | Test scripts | `test_subject.py` | `test_app.py` |
| **Data Schemas** | JSON structures | `snake_case.json` | `items.json`, `users.json` |

#### 3.1.2 Versioning
The project utilizes **Semantic Versioning (SemVer 2.0.0)** in the format `MAJOR.MINOR.PATCH`:
*   **MAJOR**: Incremented for incompatible API changes or architectural overhauls.
*   **MINOR**: Incremented for new features that are backward compatible.
*   **PATCH**: Incremented for backward-compatible bug fixes.

#### 3.1.3 Baselines
A baseline is a snapshot of the project at a specific point in time.
*   **Development Baseline**: The head of the `develop` branch (if used) or active feature branches.
*   **Product Baseline**: The tagged version on the `main` branch (e.g., `v1.0.0`, `v1.1.0`).

### 3.2 Configuration Control

The Configuration Control process ensures that changes are managed systematically.

**Step 1: Request**
*   A Change Request (CR) is submitted via the project issue tracker or documentation.
*   Details include: Description, Priority, Type (Feature/Bug), and Justification.

**Step 2: Assessment**
*   The Change Controller analyzes the request for technical feasibility and impact.
*   Impacted CIs are identified.

**Step 3: Decision**
*   The CCB (SCM Manager + Change Controller) approves or rejects the CR.
*   Approved CRs are assigned to a Developer.

**Step 4: Implementation**
*   Developer creates a new branch (`feature/xyz` or `bugfix/abc`).
*   Code is modified, and tests are updated.

**Step 5: Verification**
*   Automated tests are executed.
*   A Pull Request is opened for Peer Review.

**Step 6: Integration**
*   Upon approval, the code is merged into `main`.
*   The Change Log is updated, and the CR is marked as "Closed".

### 3.3 Configuration Status Accounting
Status accounting provides visibility into the state of the system.
*   **Registration**: All new CIs are recorded in the `documents/CI_REGISTER.md` upon creation.
*   **Tracking**: The status of Change Requests (Open, In Progress, Verified, Closed) is maintained in `documents/CHANGE_LOG.md`.
*   **Reporting**: Status reports are generated prior to every major release to summarize changes.

### 3.4 Configuration Audits
Audits are conducted to verify compliance with this SCMP.

#### 3.4.1 Functional Configuration Audit (FCA)
**Objective**: To verify that the configuration item's actual performance complies with its requirements.
*   **Checklist**:
    *   Have all requirements associated with the release been implemented?
    *   Do automated tests pass?
    *   Does the feature work as described in the User Guide?

#### 3.4.2 Physical Configuration Audit (PCA)
**Objective**: To verify that the "as-built" configuration item conforms to the technical documentation.
*   **Checklist**:
    *   Do all file names match the CI Register?
    *   Are version numbers consistent across documentation and code?
    *   Is the directory structure correct?

<div style="page-break-after: always;"></div>

## 4. RELEASE MANAGEMENT

### 4.1 Release Process
1.  **Code Freeze**: No new features are accepted into `main`.
2.  **Audit**: Conduct FCA and PCA audits.
3.  **Tagging**: The SCM Manager creates a Git tag (e.g., `v1.1.0`).
4.  **Documentation**: Release notes are finalized and published in `releases/`.
5.  **Distribution**: The code is packaged (zip/tar) and made available on GitHub Releases.

### 4.2 Backup and Recovery
*   **Repository Backup**: The GitHub cloud repository acts as the primary off-site backup.
*   **Local Redundancy**: Each developer maintains a full clone of the repository history.
*   **Recovery Plan**: In the event of data corruption, the SCM Manager will restore the repository from the latest valid Baseline tag (`git reset --hard <tag>`).

## 5. TOOLS AND RESOURCES

The following tools are authorized for use in the SCM process:

| Category | Tool | Purpose |
| :--- | :--- | :--- |
| **Version Control** | **Git** | Distributed version control system for tracking changes. |
| **Repository Hosting** | **GitHub** | Centralized storage, issue tracking, and PR management. |
| **Editor** | **VS Code** | Integrated Development Environment for code editing. |
| **Language** | **Python 3.12** | Core programming language for the application. |
| **Framework** | **Flask** | Web framework used for the application. |
| **Testing** | **unittest** | Python’s built-in framework for automated testing. |
| **Documentation** | **Markdown** | Lightweight markup language for all project docs. |

## 6. MAINTENANCE

This SCMP is a living document. It is reviewed:
1.  At the beginning of each major release cycle.
2.  Whenever a significant change in tools or team structure occurs.
3.  If a Configuration Audit identifies drastic process failures.

**Maintenance Responsibility**: The **SCM Manager** is responsible for maintaining this plan.

---
**End of Document**
