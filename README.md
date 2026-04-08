# DevSecOps Principles & AWS Cloud Security

> Interactive learning resource for DevSecOps fundamentals, threat modeling, pipeline security, and AWS cloud security best practices.

Last updated: March 2026

## What's Inside

| Resource | Count | Description |
|----------|-------|-------------|
| Concept Docs | 18 | In-depth markdown guides covering DevSecOps and AWS security concepts |
| Lab Manuals | 13 | Step-by-step hands-on labs with validated instructions |
| Interactive Pages | 28 | Self-contained HTML explainers with diagrams and visual learning |
| Lab Files | 10 | Python scripts, GitHub Actions workflows, AWS configs |
| Projects | 5 | Lesson-end and course-end projects |

## Quick Start

### 1. Read the Concepts

Start with the concept docs in `devsecops/docs/` to understand the theory:

- [DevSecOps Fundamentals](devsecops/docs/fundamentals/) — What is DevSecOps, threat modeling, pipeline security
- [AWS Cloud Security](devsecops/docs/aws-security/) — Security principles, shared responsibility, CodePipeline, debugging
- [Advanced Topics](devsecops/docs/advanced/) — EKS security, Security Hub, IAM best practices
- [Additional References](devsecops/docs/additional/) — GuardDuty, Config, KMS, Inspector, Macie

### 2. Practice with Labs

Follow the 13 hands-on labs in `devsecops/labmanuals/`:

**Lesson 1 — DevSecOps Fundamentals**

- Lab 01: [DREAD Risk Assessment Model](devsecops/labmanuals/lab01-threat-dread-model.md)
- Lab 02: [PASTA Threat Modeling](devsecops/labmanuals/lab02-threat-pasta-model.md)
- Lab 03: [SAST Scan with Semgrep](devsecops/labmanuals/lab03-pipeline-sast-scan.md)
- Lab 04: [DAST with OWASP ZAP](devsecops/labmanuals/lab04-pipeline-dast-owasp-zap.md)
- Lab 05: [Penetration Testing](devsecops/labmanuals/lab05-pipeline-penetration-testing.md)

**Lesson 2 — AWS Cloud Security Fundamentals**

- Lab 06: [OWASP Dependency Check](devsecops/labmanuals/lab06-security-owasp-dependency-check.md)
- Lab 07: [CodePipeline Encryption](devsecops/labmanuals/lab07-aws-codepipeline-encryption.md)
- Lab 08: [Security Group Validation](devsecops/labmanuals/lab08-aws-security-group-validation.md)
- Lab 09: [CloudTrail Debugging](devsecops/labmanuals/lab09-aws-cloudtrail-debugging.md)

**Lesson 3 — Advanced AWS Security**

- Lab 10: [Secure EKS Cluster](devsecops/labmanuals/lab10-eks-secure-cluster.md)
- Lab 11: [AWS Security Hub](devsecops/labmanuals/lab11-aws-security-hub.md)
- Lab 12: [IAM User & Permissions](devsecops/labmanuals/lab12-iam-user-permissions.md)
- Lab 13: [IAM MFA Setup](devsecops/labmanuals/lab13-iam-mfa-setup.md)

### 3. Explore Interactive Pages

Browse visual explainers: [Open Interactive Catalog](https://devopscert202.github.io/devsecops-aws-security/devsecops/html/index.html)

### 4. Apply Your Knowledge

Complete the projects in `devsecops/projects/`:

- [Project 01: Penetration Testing & SQL Injection](devsecops/projects/project01-pentest-sql-injection.md)
- [Project 02: IAM Monitoring Automation](devsecops/projects/project02-iam-monitoring-automation.md)
- [Project 03: Vulnerability Dashboard](devsecops/projects/project03-vulnerability-dashboard.md)

**Course-end capstones**

- [Course Project 01](devsecops/projects/course-project01.md)
- [Course Project 02](devsecops/projects/course-project02.md)

## Repository Structure

```text
devsecops-aws-security/
├── README.md
├── _config.yml                    # GitHub Pages (Jekyll) site config
├── .gitattributes
├── .gitignore
└── devsecops/
    ├── docs/                      # Concept documentation (Markdown)
    │   ├── fundamentals/
    │   ├── aws-security/
    │   ├── advanced/
    │   └── additional/
    ├── html/                      # Interactive HTML explainers + catalog (index.html)
    ├── labmanuals/                # Step-by-step lab guides (+ README.md)
    ├── labs/                      # Lab assets (scripts, pipelines, AWS samples)
    │   ├── aws/
    │   ├── eks/
    │   ├── pipelines/
    │   └── scripts/
    └── projects/                  # Lesson-end and course-end projects
```

## Course Overview

- **Duration**: 8 hours (2 days)
- **Lessons**: 3
- **Assisted Practices**: 13
- **Projects**: 3 lesson-end + 2 course-end

### Day 1 (4 hours): Conceptualizing DevSecOps

- DevSecOps overview and principles
- Threat modeling (STRIDE, DREAD, PASTA)
- Pipeline security (SAST, DAST, SCA, pen testing)
- Debugging in DevSecOps

### Day 2 (4 hours): AWS Cloud Security

- Security principles (Defense in Depth, Least Privilege, CIA Triad)
- AWS Shared Responsibility Model
- AWS CodePipeline security and encryption
- Debugging in AWS (CloudTrail, Security Groups)
- Amazon EKS security
- AWS Security Hub
- IAM best practices (MFA, least privilege, roles)

## Prerequisites

- Basic understanding of software development and operations
- Familiarity with AWS Console
- GitHub account for CI/CD labs
- Smartphone for MFA lab (Google Authenticator)

## License

This material is for educational purposes.
