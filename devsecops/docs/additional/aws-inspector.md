# Amazon Inspector

*Automated vulnerability assessment for workloads and artifacts: concepts, coverage, severities, and Security Hub integration.*

---

## What is Amazon Inspector?

**Amazon Inspector** is an **automated vulnerability management** service that **finds** software **vulnerabilities** and **network exposure** (depending on feature and target). It helps teams **prioritize** patching and **reduce** attack surface by **continuously** or **on-demand** assessing **EC2** instances, **container images** in **Amazon ECR**, and **Lambda** functions (exact scanners and features evolve—consult current AWS documentation for your Region).

Inspector is a **preventive/detective hybrid**: it does not block traffic but **surfaces risk** early in the lifecycle (CI **image** scans) or **continuously** on **running** workloads.

---

## Assessment scope (conceptual)

| Target | What Inspector evaluates (high level) |
|--------|----------------------------------------|
| **Amazon EC2** | Instance software **CVEs** via **SSM** agent integration and **network reachability** where supported—identifies **vulnerable** packages on **reachable** hosts. |
| **Container images (ECR)** | **Image** layers for **known** vulnerabilities; often integrated into **push** or **CI** pipelines. |
| **AWS Lambda** | **Function** **code** and **dependencies** for **CVEs** (language/runtime dependent). |

Coverage depends on **agent** presence, **registry** permissions, and **supported** **OS** and **runtime** versions.

---

## Finding severity

Inspector classifies findings using **severity** levels (names may display as **Critical**, **High**, **Medium**, **Low**, **Informational**). Use severity for **SLA** routing:

| Severity | Typical response expectation |
|----------|------------------------------|
| **Critical / High** | **Emergency** patch path or **isolation** if exploit is **network-accessible**. |
| **Medium** | Scheduled **patch** within **standard** windows; verify **compensating** controls. |
| **Low / Informational** | **Backlog** grooming; may be **accepted** risk with **documented** rationale. |

Always read **finding details** for **CVSS**, **exploitability**, and **reachability** context—not only the **label**.

---

## Integration with AWS Security Hub

When integrated, Inspector findings are **imported** into **Security Hub** as **ASFF** findings:

- **Centralized** triage with **GuardDuty** and **Macie** signals on the **same** resources where applicable.
- **Automation** via **EventBridge** to open **tickets** or trigger **remediation** runbooks (e.g., block **deploy** if **critical** CVE in **ECR**).

---

## Relationship to other services

| Service | Distinction |
|---------|-------------|
| **GuardDuty** | **Behavioral** threat detection—not a **CVE** scanner. |
| **AWS Config** | **Configuration** compliance—not **vulnerability** depth for packages. |
| **Security Hub** | **Aggregation** layer for **Inspector** and other tools. |

---

## Hands-On Labs

- [Project 03: Vulnerability Dashboard](../projects/project03-vulnerability-dashboard.md)

---

*Last updated: March 2026*
