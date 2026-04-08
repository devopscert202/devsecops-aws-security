# AWS Config

*Continuous resource inventory, configuration history, and compliance rules—conceptual overview without a dedicated lab.*

---

## What is AWS Config?

**AWS Config** tracks **configuration** of supported **AWS resources** over time. It answers: **What is deployed?** **What changed?** **Does it still match policy?** It is foundational for **governance**, **audit**, and **security** workflows when combined with **remediation** and **aggregation** in **Security Hub**.

---

## Core concepts

| Concept | Description |
|---------|-------------|
| **Configuration recorder** | Continuously records **configuration items** for selected **resource types** in a **Region**. |
| **Delivery channel** | Stores snapshots and history (typically **S3**); defines where **Config** delivers data. |
| **Configuration history** | Point-in-time and **timeline** views of **attribute** changes on resources. |
| **Resource inventory** | A queryable view of **existing** resources that Config knows about. |

Recorders can be **single-account** or **organization-wide** with **aggregation** for centralized visibility.

---

## Rules: managed and custom

**Rules** evaluate whether a **resource** complies with a desired state.

| Rule type | Description |
|-----------|-------------|
| **Managed rules** | AWS-authored templates for common checks (e.g., S3 bucket **public read** prohibited, **CloudTrail** enabled). |
| **Custom rules** | Implemented with **AWS Lambda** (or **CloudFormation Guard**-style policies in some flows) to encode **organization-specific** logic. |

When a rule **evaluates** non-compliance, Config emits a **compliance** result you can **report**, **alert** on, or **remediate**.

---

## Conformance packs

A **conformance pack** is a **bundle** of **rules** and **remediation** artifacts (often **YAML**-defined) aligned to a **framework** or **internal standard** (e.g., operational security baseline). Packs simplify **consistent** rollout across **many accounts**.

---

## Remediation actions

**AWS Config** can trigger **automatic remediation** using **SSM Automation** documents or **Lambda** (depending on setup):

- **Correct** misconfigurations (e.g., remove public ACL).
- **Open tickets** via **EventBridge** integrations instead of auto-fix when **human approval** is required.

Remediation should be paired with **change management** and **blast-radius** analysis—auto-remediation in **production** can disrupt legitimate **temporary** changes if poorly scoped.

---

## Integration with AWS Security Hub

**Security Hub** can treat **Config** rule findings as **security** or **compliance** signals:

- **Config** evaluates resources; **non-compliant** results flow into **Security Hub** when the integration is enabled.
- **ASFF** normalization allows **single** dashboarding next to **GuardDuty**, **Inspector**, and **Macie**.

This pattern supports **continuous compliance** rather than **annual** snapshot audits alone.

---

## Typical use cases

| Use case | How Config helps |
|----------|------------------|
| **Detect public exposure** | Rules on **S3**, **security groups**, **RDS** snapshots. |
| **Prove change control** | **Timeline** of who changed what (with **CloudTrail** correlation). |
| **Drift detection** | Compare **actual** vs **approved** **CloudFormation** or **desired-state** definitions. |
| **Offboarding** | Verify **resources** were **deleted** or **encrypted** after project end. |

---

## Hands-On Labs

There is **no dedicated hands-on lab** for AWS Config in this curriculum. Use this page as **reference** alongside **[Lab 11: AWS Security Hub](../labmanuals/lab11-aws-security-hub.md)**, where aggregated findings often include **Config**-driven compliance results.

---

Last updated: March 2026
