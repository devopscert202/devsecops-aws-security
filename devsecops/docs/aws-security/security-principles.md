# Security Principles in DevSecOps

Conceptual overview of foundational security ideas used when designing, building, and operating secure software delivery and cloud workloads.

**Last updated:** March 2026

---

## What Are Security Principles?

Security principles are durable guidelines—patterns of thinking and design—that help teams make consistent decisions under uncertainty. They do not replace tools or checklists; they explain *why* controls exist and how to trade off cost, usability, and risk.

**Example:** Choosing to store secrets in a vault instead of in source code follows the principle of *defense in depth* (limiting blast radius) and *least privilege* (only runtime components retrieve secrets).

---

## Fundamental Principles in DevSecOps Security

DevSecOps extends classic security ideas into the software lifecycle: planning, coding, building, testing, deploying, and operating. Common themes include:

- **Shift-left:** Address security early (design and code) rather than only at release.
- **Automate assurance:** Use policy-as-code, scanners, and pipelines so security checks are repeatable.
- **Observable systems:** Log, metric, and trace enough to detect misuse and prove compliance.
- **Shared ownership:** Developers, platform, and security collaborate on threat models and guardrails.

---

## Defense in Depth

**Definition:** Layer multiple independent controls so that failure of one layer does not equal total compromise.

Think in terms of **layers** that an attacker must cross:

| Layer | Examples |
|--------|----------|
| **Network** | Segmentation, security groups / NACLs, WAF, private subnets, VPC endpoints |
| **Host** | Hardened AMIs, patching, endpoint protection, immutable infrastructure |
| **Application** | Input validation, authn/authz, rate limiting, secure session handling |
| **Data** | Encryption at rest and in transit, key management, classification, backups |

**Example:** A public-facing API might sit behind a WAF (network), run on patched instances in a private subnet (host), enforce OAuth2 and RBAC (application), and persist customer records in an encrypted database with KMS (data). Breaching the API alone should not automatically expose raw backups or admin networks.

---

## Least Privilege

**Definition:** Grant only the **minimum** access required for a **specific** task, for the **shortest** time that makes sense.

**Examples:**

- A CI role that can deploy to staging but not production unless a separate approval or role assumption is used.
- A database user used by an application that can `SELECT`/`INSERT` on one schema but cannot `DROP` tables or read other tenants’ data.
- Temporary credentials (e.g., role chaining, short-lived tokens) instead of long-lived admin keys on laptops.

Least privilege applies to humans, workloads, and automation equally.

---

## Authentication vs Authorization

| | **Authentication (AuthN)** | **Authorization (AuthZ)** |
|---|------------------------------|----------------------------|
| **Question** | *Who are you?* | *What may you do?* |
| **Proves** | Identity (often via credentials, MFA, SSO) | Permissions for resources or actions |
| **Typical artifacts** | Login, JWT *subject*, API keys tied to an identity | IAM policies, RBAC roles, OAuth scopes, row-level security |

**Examples:**

- **AuthN:** A user signs in with SSO and MFA; the system issues a session or token identifying `user@example.com`.
- **AuthZ:** The same user may *read* reports but not *approve* wire transfers; the application checks roles or policies after AuthN succeeds.

A system can authenticate successfully and still be denied by authorization—a normal and desired outcome when accessing another team’s resources.

---

## Hands-On Labs

For practice that applies dependency and supply-chain security concepts in a pipeline context, see:

- [Lab 06: OWASP Dependency Check](../labmanuals/lab06-security-owasp-dependency-check.md)
