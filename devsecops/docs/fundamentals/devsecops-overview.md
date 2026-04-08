# DevSecOps Overview

*Integrating security into every phase of the software delivery lifecycle.*

## Table of Contents

1. [What Is DevSecOps?](#what-is-devsecops)
2. [Why DevSecOps Matters](#why-devsecops-matters)
3. [Benefits](#benefits)
4. [DevOps vs DevSecOps](#devops-vs-devsecops)
5. [Shift-Left Security](#shift-left-security)
6. [Culture, Automation, and Continuous Improvement](#culture-automation-and-continuous-improvement)
7. [Best Practices](#best-practices)
8. [Key Security Tool Categories](#key-security-tool-categories)
9. [Hands-On Labs](#hands-on-labs)

---

## What Is DevSecOps?

**DevSecOps** is the practice of embedding **security** into each stage of the **DevOps** lifecycle—planning, coding, building, testing, releasing, deploying, operating, and monitoring—so that security is a shared responsibility rather than a late-stage gate.

In traditional models, security teams often reviewed systems just before production. That approach creates bottlenecks, surprises, and expensive fixes. DevSecOps treats security as a **continuous** concern: developers, operations, and security specialists collaborate early and often, using **automation** to enforce policies and catch issues when they are cheapest to fix.

At a high level, DevSecOps answers: *How do we build and run software quickly **and** safely?*

---

## Why DevSecOps Matters

Modern applications depend on cloud infrastructure, APIs, third-party libraries, and rapid release cycles. Attackers target the **entire** supply chain—from misconfigured cloud resources to vulnerable dependencies to application logic flaws.

DevSecOps matters because:

- **Attack surface grows** with microservices, containers, and infrastructure-as-code.
- **Regulations and customer expectations** demand demonstrable security and auditability.
- **Speed without safety** increases the risk of breaches, downtime, and compliance failures.

Integrating security into DevOps aligns delivery speed with **risk reduction** and **accountability**.

---

## Benefits

| Benefit | Description |
|--------|-------------|
| **Earlier defect discovery** | Issues found in design or code cost less than fixes in production. |
| **Faster, safer releases** | Automated checks reduce manual review bottlenecks while raising the security bar. |
| **Shared ownership** | Security becomes part of “done,” not an external approval step. |
| **Better visibility** | Pipelines and monitoring surface vulnerabilities, misconfigurations, and policy drift. |
| **Compliance readiness** | Traceable controls and evidence support audits and frameworks (e.g., PCI, SOC 2). |

---

## DevOps vs DevSecOps

**DevOps** emphasizes collaboration between development and operations, automation, and fast feedback loops. **DevSecOps** extends that model by making **security** a first-class participant in the same workflows.

```
Traditional view (simplified):

  Dev --> Ops --> [Security review at the end]

DevOps:

  Dev <-----> Ops
       (CI/CD, automation, shared metrics)

DevSecOps:

  Dev <-----> Ops <-----> Security
       (security as code, automated gates, threat-informed design)
```

| Aspect | DevOps | DevSecOps |
|--------|--------|-----------|
| Primary focus | Velocity, reliability, collaboration | Same, **plus** security by design |
| Security timing | Often late or parallel | **Continuous**, from plan through operate |
| Feedback | App health, deployments | **Plus** vulnerabilities, policy violations, threats |
| Tooling emphasis | Build, test, deploy | **Plus** SAST, DAST, SCA, IaC scan, secrets detection |

DevSecOps does not replace DevOps—it **completes** it for environments where security risk is material.

---

## Shift-Left Security

**Shift-left** means moving security activities **earlier** in the lifecycle (to the “left” on a timeline from design to production).

Examples of shift-left activities:

- Threat modeling during **design**
- Secure coding standards and **pre-commit** checks
- **SAST** and **SCA** in pull requests
- **IaC scanning** before infrastructure is applied
- Security **unit tests** and abuse-case tests alongside functional tests

Shift-left does **not** mean “only early.” Mature programs also **shift right**: runtime protection, monitoring, incident response, and post-deployment validation (e.g., DAST, penetration tests) remain essential.

```
Lifecycle (conceptual):

  Plan ---- Code ---- Build ---- Test ---- Release ---- Deploy ---- Operate ---- Monitor
   ^                              ^                                              ^
   |                              |                                              |
 threat model                  SAST/SCA                                    SIEM, IR,
 secure design                 DAST (staged)                               threat intel
```

---

## Culture, Automation, and Continuous Improvement

### Culture

- **Shared responsibility**: Everyone considers security implications of their changes.
- **Psychological safety**: Teams report near-misses and findings without blame; focus on systems.
- **Education**: Regular training on secure coding, cloud security, and your organization’s threats.

### Automation

- Encode policies as **code** (lint rules, policy-as-code, pipeline gates).
- **Fail fast** on critical issues; **warn** or **ticket** on lower severities.
- Keep feedback **actionable** (clear findings, ownership, remediation paths).

### Continuous improvement

- Measure **mean time to remediate** (MTTR) for security findings.
- Review **false positives** and tune tools.
- Incorporate **post-incident** and **pentest** lessons into standards and training.

---

## Best Practices

1. **Start with risk**: Prioritize assets and threats; not every service needs identical controls.
2. **Integrate security into CI/CD**: Automated scans and policy checks on every meaningful change.
3. **Protect secrets**: Never commit credentials; use secret managers and short-lived credentials.
4. **Harden the pipeline**: The CI/CD system is a high-value target—lock down permissions and supply chain.
5. **Use least privilege**: For people, service accounts, and cloud IAM roles.
6. **Inventory dependencies and images**: Know what you ship; patch or replace vulnerable components.
7. **Validate infrastructure**: Scan IaC and cloud posture before and after deployment.
8. **Monitor and respond**: Correlate security signals with deployments and ownership.

---

## Key Security Tool Categories

These categories are **complementary**. Effective programs combine several of them.

| Category | What it does (conceptually) | Example focus |
|----------|----------------------------|---------------|
| **SAST** (Static Application Security Testing) | Analyzes **source code** without running the app | Injection flaws, unsafe APIs, logic errors |
| **DAST** (Dynamic Application Security Testing) | Tests **running** applications over the network | Auth/session issues, misconfigurations, XSS |
| **SCA** (Software Composition Analysis) | Identifies **open-source** components and known vulnerabilities | CVEs in libraries, license risk |
| **Container scanning** | Inspects **images** for OS/package CVEs and misconfigurations | Base image risk, malware, secrets in layers |
| **IaC scanning** | Checks **infrastructure-as-code** templates for unsafe settings | Public S3 buckets, overly broad security groups |

Detailed comparisons of SAST, DAST, and SCA appear in [SAST, DAST, and SCA](sast-dast-sca.md). Pipeline placement is covered in [DevSecOps Pipeline](devsecops-pipeline.md).

---

## Hands-On Labs

This module is a **conceptual foundation**. Step-by-step exercises for Lesson 1 appear in the course lab manuals linked from other fundamentals documents (for example, threat modeling and pipeline security labs).

---

*Last updated: March 2026*
