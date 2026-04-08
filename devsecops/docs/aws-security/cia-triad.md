# CIA Triad, OWASP Top 10, and CIS Controls

*Conceptual reference linking classic security objectives (CIA), common application risks (OWASP Top 10, 2021), and organizational control frameworks (CIS Controls v8)—without step-by-step lab procedures.*

---

## The CIA triad

The **CIA triad** names three properties that security controls aim to preserve for information and systems: **confidentiality**, **integrity**, and **availability**. Most real incidents violate one or more of these; defense in depth addresses all three.

### Confidentiality

**Confidentiality** means only authorized people and systems can read or otherwise disclose information.

| Real-world example | Why it matters |
|--------------------|----------------|
| A hospital chart is visible only to treating staff, not to random visitors. | Prevents harm, legal breach, and loss of trust. |
| Salary spreadsheets are restricted to HR and payroll systems. | Reduces insider fraud and workplace conflict. |
| API responses omit fields a given user is not allowed to see. | Stops broken access control from turning into data leaks. |

**Cloud-oriented examples:** encryption at rest and in transit; private subnets; least-privilege IAM; secrets managers; field-level encryption in applications.

### Integrity

**Integrity** means data and systems are not altered, corrupted, or replaced in an unauthorized way—and that unauthorized change is detectable when it happens.

| Real-world example | Why it matters |
|--------------------|----------------|
| Bank transfers cannot be silently changed in transit. | Protects money and auditability. |
| Software updates are signed so users know they came from the vendor. | Reduces supply-chain compromise. |
| Logs cannot be edited by attackers after the fact (or tampering is obvious). | Supports investigations and compliance. |

**Cloud-oriented examples:** object versioning and immutability; code signing; signed container images; configuration drift detection; cryptographic hashing and KMS-backed signing.

### Availability

**Availability** means authorized users can use services when needed, and the system resists outages and attacks that deny access.

| Real-world example | Why it matters |
|--------------------|----------------|
| Emergency services dispatch stays online during peak load. | Public safety depends on uptime. |
| A retailer’s checkout works on Black Friday. | Direct revenue impact. |
| DDoS mitigation keeps APIs reachable for legitimate clients. | Prevents extortion and reputational damage. |

**Cloud-oriented examples:** multi-AZ design, auto scaling, DDoS protection services, resilient DNS, backup and restore, chaos testing.

---

## OWASP Top 10 (2021 edition)

The **OWASP Top 10** highlights the most critical **web application** security risks. Use it to prioritize design reviews, testing, and controls in CI/CD.

| ID | Risk | Brief description |
|----|------|-------------------|
| **A01** | Broken Access Control | Users can act outside their intended permissions (IDOR, forced browsing, missing authorization on APIs). |
| **A02** | Cryptographic Failures | Weak or missing crypto exposes data at rest or in transit (TLS misconfig, weak algorithms, keys in code). |
| **A03** | Injection | Untrusted input is interpreted as code or commands (SQL, OS, LDAP, etc.). |
| **A04** | Insecure Design | Flaws in threat modeling and architecture—not patchable as a single bug (unsafe business flows, missing rate limits). |
| **A05** | Security Misconfiguration | Default credentials, verbose errors, open cloud storage, unnecessary features enabled. |
| **A06** | Vulnerable and Outdated Components | Unpatched libraries, frameworks, and OS packages with known CVEs. |
| **A07** | Identification and Authentication Failures | Weak passwords, missing MFA, session fixation, poor credential recovery. |
| **A08** | Software and Data Integrity Failures | Unsafe deserialization, unsigned updates, compromised CI/CD or dependencies. |
| **A09** | Security Logging and Monitoring Failures | Insufficient detection and response due to missing or ignored logs and alerts. |
| **A10** | Server-Side Request Forgery (SSRF) | The server is tricked into issuing requests to unintended internal or external targets, often bypassing network boundaries. |

---

## CIS Controls v8 — Top 18 controls and Implementation Groups

**CIS Controls** are a prioritized set of actions to improve cyber defense. **Version 8** organizes **18 control areas**. Each control contains **safeguards** tagged for **Implementation Group 1 (IG1)**, **IG2**, or **IG3**. Groups are **cumulative**: IG2 includes IG1; IG3 includes IG2.

- **IG1 — Essential cyber hygiene:** Baseline safeguards suitable for every organization; focuses on stopping common, untargeted attacks.
- **IG2 — Managed enterprise:** Additional safeguards for organizations handling more sensitive data or operating at larger scale.
- **IG3 — High-sensitivity / advanced threats:** The most stringent safeguards, including mature testing and response capabilities.

### The 18 CIS Controls (v8)

| # | Control | One-line summary |
|---|---------|------------------|
| 1 | Inventory and Control of Enterprise Assets | Know what hardware and endpoints you have; remove unauthorized assets. |
| 2 | Inventory and Control of Software Assets | Know what software is installed and allowed; prevent unapproved software. |
| 3 | Data Protection | Classify, encrypt, segment, and handle data according to sensitivity. |
| 4 | Secure Configuration of Enterprise Assets and Software | Harden defaults; track and remediate misconfiguration. |
| 5 | Account Management | Lifecycle management for human and non-human accounts. |
| 6 | Access Control Management | Grant minimum access; review permissions regularly. |
| 7 | Continuous Vulnerability Management | Find, prioritize, and remediate vulnerabilities on an ongoing basis. |
| 8 | Audit Log Management | Collect, protect, and review logs needed for detection and investigation. |
| 9 | Email and Web Browser Protections | Reduce phishing and web-borne malware. |
| 10 | Malware Defenses | Prevent, detect, and respond to malicious code. |
| 11 | Data Recovery | Backups and recovery tested for critical data and systems. |
| 12 | Network Infrastructure Management | Secure design, configuration, and lifecycle of network gear. |
| 13 | Network Monitoring and Defense | Detect and contain malicious network activity. |
| 14 | Security Awareness and Skills Training | Build a workforce that recognizes and reports threats. |
| 15 | Service Provider Management | Security requirements and monitoring for vendors and cloud/SaaS. |
| 16 | Application Software Security | Secure SDLC practices for custom and configured applications. |
| 17 | Incident Response Management | Prepared playbooks, communications, and improvement after events. |
| 18 | Penetration Testing | Authorized testing to validate defenses and find weaknesses. |

### IG1 — Essential cyber hygiene (baseline)

Organizations at **IG1** implement the **IG1-tagged safeguards** across the framework—focused on stopping common, opportunistic attacks. Study and planning often anchor on **control areas 1–12**:

| # | Control |
|---|---------|
| 1 | Inventory and Control of Enterprise Assets |
| 2 | Inventory and Control of Software Assets |
| 3 | Data Protection |
| 4 | Secure Configuration of Enterprise Assets and Software |
| 5 | Account Management |
| 6 | Access Control Management |
| 7 | Continuous Vulnerability Management |
| 8 | Audit Log Management |
| 9 | Email and Web Browser Protections |
| 10 | Malware Defenses |
| 11 | Data Recovery |
| 12 | Network Infrastructure Management |

### IG2 — Managed enterprise (builds on IG1)

**IG2** adds **IG2-tagged safeguards** (IG2 is **cumulative** with IG1). Maturity increases in areas such as **deeper vulnerability management**, **network monitoring**, **security awareness**, **application security**, and **stronger** data and access governance. Control areas commonly **extended** at this level include **3, 4, 5, 6, 7, 12–14, 16**—alongside full execution of everything required for **IG1**.

### IG3 — High-sensitivity / advanced threats (builds on IG2)

**IG3** implements the **most stringent** safeguards for data sensitivity or adversary model. Emphasis grows in **advanced network monitoring and defense (13)**, **service provider management (15)**, **incident response (17)**, **penetration testing (18)**, and **rigorous** treatment of **application software security (16)** and **awareness (14)**. Many **IG3** safeguards are **stricter variants** of practices already started under **IG1** and **IG2**.

### Important note on CIS tagging

Individual **safeguards** (sub-requirements), not entire control **titles**, carry **IG1 / IG2 / IG3** labels in the official CIS Controls v8 specification. For audits and roadmaps, always use the **published safeguard list**; the IG sections above are a **conceptual** study map aligned with how teams usually roll out the **top 18** control areas.

---

## Hands-On Labs

- [Lab 06: OWASP Dependency Check](../labmanuals/lab06-security-owasp-dependency-check.md)

---

Last updated: March 2026
