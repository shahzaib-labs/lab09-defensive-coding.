# Sprint Backlog – Experiment 9
## Defensive Coding and Automated SAST Pipeline

### Sprint Item 1: Safe Memory Boundaries

**User Story:**

As a software developer, I want to replace unsafe fixed-size character arrays with secure string handling and explicit input length validation so that buffer overflow vulnerabilities can be prevented.

**Security Tasks:**
- Replace unsafe `char[]` input handling with `std::string`.
- Implement explicit input length validation.
- Prevent unauthorized memory access.
- Compare vulnerable and secure C++ implementations.

### Sprint Item 2: Dynamic Execution Elimination and Privilege Control

**User Story:**

As a security engineer, I want to eliminate unsafe dynamic code execution and enforce least privilege so that remote code execution and privilege escalation risks can be reduced.

**Security Tasks:**
- Identify and eliminate unsafe `eval()` usage.
- Implement strict numeric input parsing.
- Prevent scripts from running with unnecessary root privileges.
- Apply generic error handling.
- Compare vulnerable and secure Python implementations.