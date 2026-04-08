# SAST, DAST, and SCA

*Three pillars of automated application security testing—and how to use them together.*

## Table of Contents

1. [Why These Categories Exist](#why-these-categories-exist)
2. [SAST (Static Application Security Testing)](#sast-static-application-security-testing)
3. [DAST (Dynamic Application Security Testing)](#dast-dynamic-application-security-testing)
4. [SCA (Software Composition Analysis)](#sca-software-composition-analysis)
5. [SAST vs DAST vs SCA](#sast-vs-dast-vs-sca)
6. [Hands-On Labs](#hands-on-labs)

---

## Why These Categories Exist

Modern applications combine **custom code**, **frameworks**, **open-source libraries**, **configuration**, and **runtime behavior**. No single tool sees everything:

- **SAST** inspects **source** before execution—fast feedback for developers, strong for many code-level bugs, weaker on deployment-specific issues.
- **DAST** exercises **running** systems—good for integration mistakes and environmental misconfigurations, blind to code not reachable via tests.
- **SCA** focuses on **third-party** components—essential for CVE and license risk, not a substitute for custom logic review.

Mature DevSecOps programs run **multiple** layers and **correlate** results to reduce noise and avoid gaps.

---

## SAST (Static Application Security Testing)

### What it is

**SAST** analyzes application **source code**, **bytecode**, or **IR** without executing the program in a realistic deployment. It models data and control flow to flag patterns associated with vulnerabilities (e.g., injection, path traversal, weak crypto usage).

### Features (typical)

- **Early feedback** in IDE or pull requests.
- **Line-of-code** pointers for remediation.
- **Custom rules** for organization-specific APIs or banned patterns.
- **Scale** across large repositories.

### Limitations (conceptual)

- **False positives** when context is missing (framework magic, runtime configuration).
- Cannot reliably find issues that depend on **live** data, **multi-service** flows, or **infrastructure** context alone.

### Common tools

| Tool | Notes |
|------|--------|
| **Semgrep** | Fast, rule-based scanning; strong for custom rule development and CI integration. |
| **SonarQube** | Broad quality + security rules; widely used for gating and dashboards. |
| **Checkmarx** | Enterprise SAST with workflow integration and language breadth. |
| **Fortify** (OpenText) | Enterprise SAST with extensive reporting and lifecycle integrations. |

### When to use

- On **every** meaningful code change (PR or mainline).
- For **security-sensitive** modules (auth, crypto, parsers) with stricter rule sets.
- Together with **developer training** to interpret and fix findings efficiently.

---

## DAST (Dynamic Application Security Testing)

### What it is

**DAST** sends **HTTP(S)** requests (and other protocols, depending on tool) to a **running** application to probe for weaknesses: input handling, authentication, session management, headers, and common web vulnerabilities.

### Features (typical)

- Sees the **assembled** system (app + server + WAF + config).
- Useful for **environment-specific** flaws (TLS settings, verbose errors, exposed debug endpoints).
- Can be driven **manually** (proxies) or **automated** (scanners, CI jobs).

### Limitations (conceptual)

- **Coverage** depends on crawl/spider quality and **test data**; hidden routes may be missed.
- Less precise **root cause** in code than SAST; may require correlation with developers.
- **Stateful** flows (modern SPAs, complex auth) need careful scripting.

### Common tools

| Tool | Notes |
|------|--------|
| **OWASP ZAP** | Open-source; widely used for automation and learning; strong community. |
| **Burp Suite** | Industry-standard manual testing with automation tiers; common in pentesting. |
| **Acunetix** | Commercial scanner focused on web vulnerabilities with automation features. |

### When to use

- Against **staging**, **preview**, or **test** environments that mirror production safely.
- Before major releases or after **significant** surface-area changes (new APIs, auth changes).
- Alongside **authenticated** scan profiles where applicable.

---

## SCA (Software Composition Analysis)

### What it is

**SCA** identifies **open-source** and third-party **dependencies** in your project, matches them to **known vulnerabilities** (e.g., CVE databases), and often reports **license** obligations and **outdated** versions.

### Features (typical)

- **Bill of materials**-style visibility (what you ship).
- **Upgrade** guidance and **transitive** dependency insight.
- **Policy** enforcement (block critical CVEs, disallowed licenses).

### Limitations (conceptual)

- **CVE** data lags or may not reflect **exploitability** in *your* context.
- In-house code and **custom** forks need additional review (SAST, review).
- **Reachability** of vulnerable code paths may require advanced tooling or triage.

### Common tools

| Tool | Notes |
|------|--------|
| **OWASP Dependency-Check** | Open-source; CVE correlation for many ecosystems; common in CI pipelines. |
| **Snyk** | Developer-centric workflows, monitoring, and policy across repos and containers. |
| **WhiteSource** (Mend) | Enterprise dependency and license governance with broad integrations. |

### When to use

- On **every** build that resolves dependencies (PR and release pipelines).
- With **version pinning** and **renovate/dependabot**-style hygiene for sustainable upgrades.

---

## SAST vs DAST vs SCA

### Comparison table

| Dimension | SAST | DAST | SCA |
|-----------|------|------|-----|
| **What is tested** | Your **source code** patterns and flows | **Running** application behavior over the network | **Third-party** libraries and versions |
| **Execution required** | No (static analysis) | Yes (live app + reachable routes) | Manifest/lockfile scan (no app run required) |
| **Typical strengths** | Early code defects, unsafe APIs, some injection patterns | Misconfigurations, session/header issues, exposed endpoints | Known CVEs, license risk, outdated deps |
| **Typical blind spots** | Runtime-only issues, infra context | Unreachable code paths, logic flaws without signals | Custom code vulnerabilities |
| **Feedback speed** | Fast in CI | Slower (env + crawl + scan) | Fast to moderate |
| **False positives** | Moderate–high (tool-dependent) | Moderate (config-dependent) | Moderate (severity vs exploitability debate) |
| **Developer workflow** | IDE + PR comments | Often security/QA-led automation + tuning | PR gating + dependency dashboards |

### Complementary use (mental model)

```
                    +-------------+
                    |  Your code  |
                    +------+------+
                           |
         +-----------------+-----------------+
         |                 |                 |
         v                 v                 v
    +---------+       +---------+       +-----------+
    |  SAST   |       |  DAST   |       |    SCA    |
    | (logic, |       | (live   |       | (deps,    |
    |  APIs)  |       |  env)   |       |  CVEs)    |
    +---------+       +---------+       +-----------+
```

---

## Hands-On Labs

Labs that reinforce these concepts in the pipeline and dependency space:

- [Lab 03: SAST Scan](../labmanuals/lab03-pipeline-sast-scan.md)
- [Lab 04: DAST with OWASP ZAP](../labmanuals/lab04-pipeline-dast-owasp-zap.md)
- [Lab 06: OWASP Dependency Check](../labmanuals/lab06-security-owasp-dependency-check.md)

---

*Last updated: March 2026*
