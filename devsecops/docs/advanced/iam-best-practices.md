# IAM Best Practices

*Concepts for designing and operating AWS Identity and Access Management: principals, policies, and operational hygiene—without procedural setup labs.*

---

## Introduction to IAM

**AWS Identity and Access Management (IAM)** controls **who** can do **what** in AWS. Core building blocks:

| Concept | Role |
|---------|------|
| **Users** | Long-lived identities for humans or legacy automation (prefer roles where possible). |
| **Groups** | Collections of users for attaching shared policies (groups cannot be assumed like roles). |
| **Roles** | Assumable identities with **trust policies**; deliver **temporary credentials** via STS. |
| **Policies** | JSON documents defining **Allow** / **Deny** for **actions** on **resources** under **conditions**. |

---

## Core features

| Feature | Benefit |
|---------|---------|
| **Fine-grained access** | Action-level and resource-level permissions (e.g., `s3:GetObject` on one bucket prefix). |
| **Federation** | SAML/OIDC integration with corporate IdP; no duplicate passwords in AWS for workforce users. |
| **MFA** | Second factor for console and programmatic high-risk operations. |
| **Temporary credentials** | **STS** sessions expire automatically; reduces blast radius of leaked credentials. |

---

## Policy types

| Type | Attached to | Purpose |
|------|-------------|---------|
| **Identity-based** | Users, groups, roles | What that identity may do. |
| **Resource-based** | S3 buckets, KMS keys, SNS topics, etc. | Who may access the resource (often cross-account). |
| **Service Control Policies (SCPs)** | AWS Organizations OUs / accounts | **Guardrails** that limit maximum permissions (never grant permissions by themselves). |
| **Permission boundaries** | IAM users or roles | Maximum permissions an identity can **effectively** have even if other policies allow more. |

Effective permissions combine **all applicable** policy types; **explicit Deny** wins.

---

## Best Practice 1: Enable MFA for all users (especially root)

- Require **MFA** for console access to production accounts.
- **Protect the account root** with MFA and **eliminate routine root use**; use **IAM roles** and **break-glass** procedures instead.
- Consider **MFA** for sensitive **API** operations via **condition keys** (`aws:MultiFactorAuthPresent`).

---

## Best Practice 2: Follow least privilege (use IAM Access Analyzer)

- Start with **minimum** permissions; expand only with evidence of need.
- Use **IAM Access Analyzer** for **external access** analysis and **policy generation** from **CloudTrail** activity (where available) to **tighten** policies safely over time.
- Prefer **managed policies** curated by your platform team over one-off admin policies.

---

## Best Practice 3: Use IAM roles instead of access keys

- **EC2, Lambda, ECS, EKS (IRSA)** should use **instance profiles** or **task/service roles**—not embedded keys.
- For CI/CD, use **OIDC federation** to AWS roles where possible instead of long-lived **access keys** in secrets.
- If keys are unavoidable, **scope**, **rotate**, and **monitor** them aggressively.

---

## Best Practice 4: Monitor with CloudTrail

- Enable organization- or account-level **CloudTrail**; protect logs from tampering (S3 bucket policy, MFA delete where appropriate).
- Alert on **`ConsoleLogin`**, **`AssumeRole`**, **IAM policy changes**, and spikes in **`AccessDenied`**.
- Logs underpin **audits** and **incident response**.

---

## Best Practice 5: Rotate credentials regularly

- Rotate **access keys** on a defined schedule or **eliminate** them in favor of roles.
- Rotate **database** and **application** secrets via **Secrets Manager** or **Parameter Store** with automation.
- Review **inactive users** and **unused roles** quarterly.

---

## Best Practice 6: Use policy conditions

Conditions reduce abuse when credentials leak:

| Condition idea | Example keys (conceptual) |
|----------------|---------------------------|
| **IP allowlist** | `aws:SourceIp`, `aws:VpcSourceIp` |
| **MFA required** | `aws:MultiFactorAuthPresent`, `aws:MultiFactorAuthAge` |
| **Time window** | `aws:CurrentTime`, `aws:EpochTime` |
| **TLS only** | `aws:SecureTransport` |

Combine conditions with **least privilege** actions and **resources** for defense in depth.

---

## Hands-On Labs

- [Lab 12: IAM User & Permissions](../labmanuals/lab12-iam-user-permissions.md)
- [Lab 13: IAM MFA Setup](../labmanuals/lab13-iam-mfa-setup.md)

---

Last updated: March 2026
