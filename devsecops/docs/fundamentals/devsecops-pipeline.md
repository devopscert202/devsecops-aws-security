# DevSecOps Pipeline

*Where security checks, policies, and feedback live across continuous delivery.*

## Table of Contents

1. [What Is a DevSecOps Pipeline?](#what-is-a-devsecops-pipeline)
2. [Pipeline Phases and Security Touchpoints](#pipeline-phases-and-security-touchpoints)
3. [SAST, DAST, and SCA (Overview)](#sast-dast-and-sca-overview)
4. [Penetration Testing](#penetration-testing)
5. [Vulnerability Management](#vulnerability-management)
6. [Secure Coding (Overview)](#secure-coding-overview)
7. [Hands-On Labs](#hands-on-labs)

---

## What Is a DevSecOps Pipeline?

A **DevSecOps pipeline** is a **continuous integration and delivery (CI/CD)** workflow that **embeds security** at each meaningful step: automated scanning, policy enforcement, secrets protection, artifact signing, configuration checks, and observability hooks.

Rather than a single “security stage,” the pipeline expresses **security as code**—rules and tools run automatically when developers commit, when artifacts are built, and when releases progress toward production.

```
Developer --> Source control --> Build --> Test --> Artifact --> Deploy --> Operate
                |               |        |          |            |
           secrets scan    SAST/SCA   DAST/IAST   sign/prov   runtime policy
                              IaC scan  config      approve     monitor/SIEM
```

Goals include **fast feedback**, **consistent gates**, and **traceability** from commit to deployment.

---

## Pipeline Phases and Security Touchpoints

Common lifecycle phases (naming varies by organization) and **where security fits**:

### Plan

- **Threat modeling**, security requirements, abuse cases.
- Data classification and **compliance** constraints (retention, regions, logging).

### Code

- **Secure coding** standards, peer review with security checklist.
- **Pre-commit** hooks: secrets detection, linting, formatting with security rules.
- **Dependency** policy (approved licenses, allowed registries).

### Build

- **SAST** on source; **SCA** on manifests; **IaC scanning** on Terraform/CloudFormation, etc.
- Hardened **build agents**, pinned tool versions, **SBOM** generation (conceptually: inventory of what was built).

### Test

- **DAST** against staging or ephemeral environments; **API security** tests.
- **Unit/integration** tests for authorization and input validation.
- **Fuzzing** or specialized tests for critical parsers (where applicable).

### Release

- **Change management** evidence, **approval** gates for high-risk environments.
- **Artifact signing**, provenance attestation (supply-chain security).
- Configuration checks for **release** parameters (feature flags, secrets references).

### Deploy

- **Policy-as-code** (e.g., admission control) preventing non-compliant workloads.
- **Least-privilege** deployment roles; **secrets** injected from vaults, not configs.
- **Blue/green or canary** with automated rollback on security SLO violations (where defined).

### Operate

- **Patching** cadence, **configuration drift** detection.
- **Incident response** playbooks; break-glass procedures with audit.

### Monitor

- **SIEM**, **EDR**, **CSPM** alerts correlated with deployments.
- **Vulnerability** feeds for running images and hosts; **threat intelligence** for exposed services.

The following table summarizes **typical** placement (your toolchain may differ):

| Phase | Example security activities |
|-------|-----------------------------|
| Plan | Threat model, requirements, data flow review |
| Code | Secure review, secrets scan, branch protection |
| Build | SAST, SCA, IaC scan, container image scan |
| Test | DAST, authz tests, contract tests for security headers |
| Release | Sign artifacts, policy checks, approvals |
| Deploy | Admission policies, KMS/IAM boundaries |
| Operate | Hardening baselines, patch management |
| Monitor | Detection rules, IR, post-deployment assessments |

---

## SAST, DAST, and SCA (Overview)

These three categories form the backbone of many application security programs. They are **complementary**: each sees different classes of issues.

| Type | Runs on | Catches (examples) |
|------|---------|---------------------|
| **SAST** | Source code (static) | SQL injection patterns, unsafe APIs, hardcoded secrets in repo |
| **DAST** | Running app (dynamic) | Session issues, misconfigured headers, exposed admin paths |
| **SCA** | Dependencies | Known CVEs, risky licenses, outdated libraries |

Deep dive: [SAST, DAST, and SCA](sast-dast-sca.md).

**When they run in the pipeline**

- **SAST / SCA**: Commonly on every pull request or nightly mainline build.
- **DAST**: Often against **staging** or **dynamic preview** environments after deploy; may be scheduled rather than per-commit due to runtime cost.

---

## Penetration Testing

**Penetration testing** (pentesting) simulates **realistic adversary** techniques against systems in scope to validate defenses and discover exploitable paths that scanners miss (especially **logic** and **chain** attacks).

### Common types (conceptual)

| Type | Description |
|------|-------------|
| **Black-box** | Testers have minimal internal knowledge—like an external attacker. |
| **Gray-box** | Partial knowledge (e.g., user accounts, architecture diagrams). |
| **White-box** | Full source and design access—strong for depth and root-cause insight. |
| **External / internal** | Whether the assumed attacker position is outside or inside the perimeter. |
| **Red team** | Broader simulation with objectives beyond a single app (often includes social engineering—governed by strict rules of engagement). |

### Features of a mature pentest program

- **Clear scope** and **rules of engagement** (no production data exfiltration without approval).
- **Remediation** tracking and **retest** of critical findings.
- **Findings fed back** into threat models, standards, and **pipeline** rules where possible.

Pentesting **does not replace** continuous scanning; it **validates** overall resilience periodically or for major releases.

---

## Vulnerability Management

**Vulnerability management** is the **lifecycle** of finding, assessing, remediating, and verifying security weaknesses across code, dependencies, infrastructure, and runtime.

### Typical lifecycle stages

```
Discover --> Triage --> Prioritize --> Remediate --> Verify --> Report / Improve
    ^                                                      |
    |______________________________________________________|
                    (continuous discovery)
```

- **Discover**: Scanners, pentests, bug bounty, cloud posture tools, threat intel.
- **Triage**: Confirm validity, severity, exploitability, **business context**.
- **Prioritize**: SLA by severity; consider **exposure** and **asset criticality**.
- **Remediate**: Patch, upgrade, isolate, or **compensating control**.
- **Verify**: Rescan, retest, confirm deployment.
- **Report / improve**: Metrics (MTTR), trend analysis, toolchain tuning.

Strong vulnerability management connects **pipeline findings** (SCA/SAST) with **production** exposure (what is actually deployed and reachable).

---

## Secure Coding (Overview)

**Secure coding** is a set of **disciplines** and **habits** that reduce vulnerability introduction at the source.

### Representative techniques

| Technique | Intent |
|-----------|--------|
| **Input validation** | Reject or normalize untrusted data at boundaries. |
| **Parameterized queries** | Avoid SQL injection by separating code from data. |
| **Output encoding** | Mitigate XSS when rendering untrusted content. |
| **Authentication / session hardening** | MFA where appropriate, secure cookies, rotation. |
| **Authorization** | Enforce **least privilege** and **object-level** checks consistently. |
| **Cryptography** | Use vetted libraries; avoid custom crypto; manage keys properly. |
| **Error handling** | Fail safely; avoid leaking internals to users or logs. |
| **Secrets hygiene** | No credentials in code; short-lived tokens where possible. |

Secure coding is reinforced by **training**, **libraries and frameworks** with safe defaults, and **automated** checks in the pipeline.

---

## Hands-On Labs

Pipeline-focused labs in this course:

- [Lab 03: SAST Scan](../labmanuals/lab03-pipeline-sast-scan.md)
- [Lab 04: DAST with OWASP ZAP](../labmanuals/lab04-pipeline-dast-owasp-zap.md)
- [Lab 05: Penetration Testing](../labmanuals/lab05-pipeline-penetration-testing.md)

---

*Last updated: March 2026*
