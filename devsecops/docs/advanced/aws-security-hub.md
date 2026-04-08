# AWS Security Hub

*Centralized security posture management across AWS accounts: findings, standards, and integrations—without console lab steps.*

---

## What is AWS Security Hub?

**AWS Security Hub** provides a **single place** to view **security findings** and **compliance status** across AWS accounts (and optionally **multi-account** via Organizations). It **aggregates**, **deduplicates**, and **prioritizes** signals from AWS services and partner products so security and platform teams can **triage** and **remediate** faster.

---

## Key functionalities

| Functionality | Description |
|---------------|-------------|
| **Automated compliance checks** | Runs or ingests checks against **security standards** (e.g., CIS AWS Foundations, AWS Foundational Security Best Practices). |
| **Findings aggregation** | Normalizes diverse sources into a **common format** (ASFF—see below). |
| **Security score / insights** | Highlights **critical** issues and trends (exact presentation evolves in the console and APIs). |
| **Workflow integration** | Feeds ticketing, chat, and SOAR via **EventBridge**, **APIs**, and partner tools. |

---

## Supported standards (examples)

Security Hub can evaluate or organize findings against frameworks such as:

| Standard / framework (examples) | Notes |
|---------------------------------|-------|
| **AWS Foundational Security Best Practices** | AWS-curated controls mapped to AWS services and resources. |
| **CIS AWS Foundations Benchmark** | Industry benchmark aligned with CIS guidance for AWS. |
| **PCI DSS** | Control mapping useful when cardholder environments run on AWS (organizational scope and responsibility still apply). |

Enable only the **standards** your governance team has approved; each may create **findings** and **cost** considerations.

---

## Integrations

Security Hub consumes findings from native AWS services and **third-party** products:

| Category | Examples |
|----------|----------|
| **Threat & vulnerability** | **Amazon GuardDuty**, **Amazon Inspector**, **AWS Firewall Manager** (related protections). |
| **Data protection** | **Amazon Macie** (sensitive data in S3). |
| **Configuration** | **AWS Config** (non-compliant resources). |
| **Partners** | ISV integrations that publish **ASFF** findings into Security Hub. |

Unified ingestion supports **cross-service** correlation (e.g., GuardDuty finding on an instance plus Inspector findings on the same resource).

---

## How it works (conceptual flow)

```
  [ Data sources: GuardDuty, Inspector, Macie, Config, IAM Access Analyzer, partners, custom ]
                                        |
                                        v
                           Normalize to ASFF (finding format)
                                        |
                                        v
              Enrich, deduplicate, severity, standards mapping
                                        |
                                        v
            Prioritize -> dashboards, insights, EventBridge, remediation playbooks
```

**ASFF** (**AWS Security Finding Format**) is the **common schema** for title, severity, resources, types, and remediation links. Consistent fields enable **search**, **automation**, and **reporting** across tools.

---

## Benefits

- **Single pane of glass** for high-volume AWS security signals.
- **Automated checks** against **documented** security standards.
- **Cross-account visibility** when integrated with **AWS Organizations**.
- **Faster handoff** from detection to ticketing and owner assignment via integrations.

---

## Hands-On Labs

- [Lab 11: AWS Security Hub](../labmanuals/lab11-aws-security-hub.md)

---

Last updated: March 2026
