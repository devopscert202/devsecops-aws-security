# Threat Modeling

*A structured way to anticipate attacks, focus defenses, and align security with business risk.*

## Table of Contents

1. [What Is Threat Modeling?](#what-is-threat-modeling)
2. [Why Threat Modeling Matters in DevSecOps](#why-threat-modeling-matters-in-devsecops)
3. [Benefits](#benefits)
4. [The Four-Step Process](#the-four-step-process)
5. [Techniques and Frameworks](#techniques-and-frameworks)
6. [Tools](#tools)
7. [Banking and Finance Use Case](#banking-and-finance-use-case)
8. [Hands-On Labs](#hands-on-labs)

---

## What Is Threat Modeling?

**Threat modeling** is a disciplined method for identifying **what can go wrong** in a system—before attackers do. You document how the system works (data flows, trust boundaries, actors), enumerate credible **threats**, relate them to **vulnerabilities** and **controls**, and **prioritize** what to fix or monitor first.

Unlike ad-hoc “what if” discussions, threat modeling produces **repeatable** artifacts (diagrams, threat lists, risk ratings) that teams can revisit as architecture and features change.

Core ideas:

- **Asset-oriented**: What must we protect (data, accounts, money movement, availability)?
- **Attacker-oriented**: Who might attack, and with what motivation and capability?
- **Control-oriented**: What defenses exist, and where are the gaps?

---

## Why Threat Modeling Matters in DevSecOps

DevSecOps accelerates change. Without threat modeling, teams may ship quickly while **unknowingly** expanding attack surface—for example, new APIs, broader IAM roles, or additional data stores.

Threat modeling supports DevSecOps by:

- Informing **secure design** decisions during planning and architecture reviews.
- Guiding **test scope** (abuse cases, security tests, DAST scenarios).
- Aligning **pipeline rules** with actual risk (what must block a release vs. what can be tracked).
- Creating a **shared mental model** so developers, operations, and security speak the same language.

It is one of the clearest **shift-left** security practices: you address structural weaknesses before they are encoded in production.

---

## Benefits

| Benefit | Outcome |
|---------|---------|
| **Proactive risk reduction** | Weak spots are found in design, not only after exploitation. |
| **Cost-effective remediation** | Fixing architecture or code early avoids emergency patches and incidents. |
| **Prioritization** | Limited security capacity focuses on highest-impact threats. |
| **Compliance and audit support** | Demonstrates due diligence and risk-aware engineering. |
| **Better incident preparedness** | Teams anticipate failure modes and monitoring gaps. |

---

## The Four-Step Process

Many organizations adapt this **four-step** pattern (wording may vary; the intent is consistent):

### 1. Identify assets

List what attackers value and what the business must protect:

- Sensitive **data** (PII, credentials, payment data, trade secrets)
- **Functions** (authentication, authorization, transfers, admin actions)
- **Infrastructure** (keys, databases, message queues, APIs)

### 2. Identify threats

Ask how adversaries could abuse or disrupt the system. Common angles include spoofing identities, tampering with data, leaking information, denying service, or escalating privilege. Frameworks such as **STRIDE** help ensure breadth (see [STRIDE, DREAD, and PASTA](stride-dread-pasta.md)).

### 3. Identify vulnerabilities

Map threats to **weaknesses**: missing controls, misconfigurations, flawed assumptions, dependency risks, or process gaps. A threat is hypothetical until linked to something exploitable or impactful.

### 4. Prioritize countermeasures

Rank issues using **impact** and **likelihood** (or structured scoring such as **DREAD**). Choose mitigations: design changes, hardening, monitoring, acceptance with compensating controls, or transfer (e.g., insurance)—document decisions.

```
     +------------------+
     |  1. Assets       |
     +--------+---------+
              |
              v
     +------------------+
     |  2. Threats      |
     +--------+---------+
              |
              v
     +------------------+
     |  3. Vulnerabilities |
     +--------+---------+
              |
              v
     +------------------+
     |  4. Countermeasures |
     +------------------+
```

---

## Techniques and Frameworks

Threat modeling can be **diagram-driven** (data flow diagrams, trust boundaries) or **process-driven** (staged methodologies). Widely referenced techniques include:

| Technique | Role in practice |
|-----------|------------------|
| **STRIDE** | **Taxonomy** of threat types (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege). Helps teams brainstorm systematically. |
| **DREAD** | **Scoring** model (Damage, Reproducibility, Exploitability, Affected users, Discoverability) to prioritize risks—often used with STRIDE or other threat lists. |
| **PASTA** | **Risk-centric**, seven-stage process from business objectives through viable threats and countermeasures—strong for aligning security with enterprise risk. |

STRIDE, DREAD, and PASTA are explained in depth—with examples—in [STRIDE, DREAD, and PASTA](stride-dread-pasta.md).

---

## Tools

Tools accelerate diagramming, collaboration, and traceability. They do **not** replace skilled analysis.

| Tool | Notes |
|------|--------|
| **Microsoft Threat Modeling Tool** | Data-flow-centric modeling with STRIDE-style prompting; useful for structured workshops (primarily Windows-oriented historically). |
| **OWASP Threat Dragon** | Open-source, web and desktop options; integrates diagrams with threat elements; approachable for teams adopting OWASP-aligned practices. |
| **IriusRisk** | Enterprise-oriented platform for scalable, collaborative threat modeling with risk tracking and workflow integration. |

Selection depends on team size, integration needs, and whether modeling is **project-level** or **enterprise-wide**.

---

## Banking and Finance Use Case

Consider a **retail banking** feature: customers move money between accounts via a mobile app and API.

**Assets** might include customer identities, session tokens, account balances, transaction records, and backend integration with **core banking** or payment rails.

**Threats** could include:

- **Spoofing**: Stolen credentials or session hijacking to initiate transfers.
- **Tampering**: Altered payment amounts or beneficiary details in transit or in the API.
- **Repudiation**: Disputes over whether a user authorized a transaction—weak logging or non-repudiation controls.
- **Information disclosure**: Leakage of balances or PII through verbose errors or excessive API fields.
- **Denial of service**: Flooding transfer endpoints to harm availability or fraud-detection systems.
- **Elevation of privilege**: A user accessing another customer’s accounts via broken object-level authorization.

**Vulnerabilities** might map to missing **step-up authentication** for high-risk transfers, insufficient **idempotency** and replay protection, or **over-privileged** service accounts in the payment connector.

**Countermeasures** could include strong **MFA**, device binding, **transaction signing**, strict **authorization** checks per account, rate limiting, immutable **audit logs**, and **fraud analytics**—with priorities driven by regulatory requirements and DREAD-style scoring.

This example illustrates how threat modeling connects **business impact** (fraud, regulatory breach) to **concrete** engineering and operational controls.

---

## Hands-On Labs

Apply structured threat assessment in the lab environment:

- [Lab 01: DREAD Model](../labmanuals/lab01-threat-dread-model.md)
- [Lab 02: PASTA Model](../labmanuals/lab02-threat-pasta-model.md)

---

*Last updated: March 2026*
