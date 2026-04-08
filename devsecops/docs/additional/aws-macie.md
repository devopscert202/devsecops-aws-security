# Amazon Macie

*Machine learning–assisted discovery of sensitive data in Amazon S3: findings, alerting, and Security Hub integration—reference material without a dedicated lab.*

---

## What is Amazon Macie?

**Amazon Macie** is a **data security** service focused on **discovering** and **classifying** **sensitive** data in **Amazon S3**. It uses **machine learning**, **pattern matching**, and **managed identifiers** to detect **PII**, **PHI**, **financial** data, and **credentials**—helping organizations **reduce** accidental **exposure** and **support** privacy programs.

Macie is **not** a replacement for **DLP** on endpoints or **database** activity monitoring; it **specializes** in **object storage** at scale.

---

## How Macie finds sensitive data

| Technique | Role |
|-----------|------|
| **Managed data identifiers** | Pre-built detectors for common **PII** and **financial** patterns (e.g., credit cards, government IDs—subject to Region and **identifier** availability). |
| **Custom data identifiers** | **Regex**-based patterns for **organization-specific** formats (internal IDs, proprietary tokens). |
| **ML-based classification** | **Contextual** analysis to **reduce** false positives compared to **regex** alone for some categories. |

**Scope** is driven by **S3** buckets you **include** in **Macie** jobs or **automated** discovery settings (product behavior evolves—see AWS docs).

---

## Findings and alerting

When Macie detects a **policy** or **content** risk, it creates **findings** with **severity**, **resource** (bucket, object **prefix** level depending on configuration), and **type** (e.g., **public** access, **unencrypted** bucket, **sensitive** data in an **unexpected** location).

**Findings** can drive:

- **Security Hub** **aggregation** for SOC **triage**.
- **EventBridge** rules for **email**, **Slack**, or **ticketing**.
- **Remediation** playbooks (tighten **bucket policy**, enable **encryption**, move data to **restricted** buckets).

---

## S3 bucket inventory and data security posture

Macie supports **inventory**-style visibility into **S3** **assets**:

- Which **buckets** exist and how they are **shared**.
- Whether **default encryption** and **public access** settings align to **policy**.
- Where **sensitive** **objects** **concentrate** for **targeted** **classification** and **access** reviews.

Pair Macie outcomes with **IAM**, **KMS**, and **organization** **SCPs** to **enforce** **preventive** controls—not only **detection**.

---

## Integration with AWS Security Hub

With **Security Hub** enabled, Macie findings **normalize** to **ASFF**, enabling:

- **Single** **dashboard** with **GuardDuty**, **Inspector**, and **Config** results.
- **Cross-correlation** (e.g., **public** bucket **finding** from **Config** plus **PII** **finding** from **Macie**).

---

## Hands-On Labs

There is **no dedicated hands-on lab** for Amazon Macie in this curriculum. Use this page as **reference** when studying **data protection** and **[Lab 11: AWS Security Hub](../labmanuals/lab11-aws-security-hub.md)** for **aggregated** **findings**.

---

*Last updated: March 2026*
