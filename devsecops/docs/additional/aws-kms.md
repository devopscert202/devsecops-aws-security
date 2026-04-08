# AWS Key Management Service (KMS)

*Concepts for encryption key lifecycle, policies, envelope encryption, and service integrations—including CodePipeline artifact protection.*

---

## What is AWS KMS?

**AWS Key Management Service (KMS)** is a **managed** service to **create**, **use**, and **audit** **cryptographic keys** in AWS. It underpins **encryption at rest** and **signing** for many AWS services and your applications via **APIs** and **SDKs**.

---

## Key types

| Type | Typical use |
|------|-------------|
| **Symmetric (AES-256)** | Encrypt and decrypt the **same** data key or small payloads; most AWS service encryption uses symmetric keys. |
| **Asymmetric (RSA / ECC)** | **Sign/verify** or **encrypt/decrypt** with public/private key pairs; common for **TLS**, **code signing**, or **off-platform** verification. |
| **HMAC keys** | Generate and verify **message authentication codes** for **integrity** checks in applications. |

Keys can be **AWS-managed** (service-created, limited customer control) or **customer-managed** (**CMKs**) with full **key policy** ownership.

---

## Key policies and grants

| Mechanism | Purpose |
|-----------|---------|
| **Key policy** | **Resource-based** policy on the **KMS key** itself—**required** for CMKs; defines **who** can use and **administer** the key. |
| **IAM policies** | **Identity-based** permissions to call **KMS APIs** (e.g., `kms:Decrypt`) **if** the key policy also allows it. |
| **Grants** | Temporary, scoped **delegations** for other principals—useful for **cross-account** or **short-lived** access patterns. |

**Both** key policy **and** IAM must allow the operation (unless key policy fully delegates to IAM for specific cases as documented).

---

## Envelope encryption

**Envelope encryption** is the standard pattern for large data:

1. Generate a **data key** from KMS (`GenerateDataKey`).
2. Use the **plaintext data key** locally to encrypt **payload** (fast, AES).
3. Store the **encrypted data key** alongside the ciphertext (or in metadata).
4. Discard the **plaintext** data key from memory after use.
5. To decrypt, call KMS to **unwrap** the data key, then decrypt locally.

This minimizes **KMS API** calls and **latency** while keeping **master keys** in **HSM-backed** KMS.

---

## Integration examples

| Service | How KMS is used (conceptually) |
|---------|--------------------------------|
| **Amazon S3** | **SSE-KMS** encrypts objects with a **data key** protected by a **KMS key** you choose. |
| **Amazon EBS** | **Volume encryption** uses KMS keys for **data keys** per volume. |
| **Amazon RDS** | **Encryption at rest** for databases and snapshots uses KMS-backed keys. |
| **AWS Lambda** | **Environment variables** can be encrypted with a **KMS key**; decrypt at runtime with the **function role**. |
| **AWS CodePipeline / CodeBuild** | **Artifact** buckets and **logs** can require **SSE-KMS**; pipeline and build **roles** need **`kms:Decrypt`/`Encrypt`** on the **CMK**. |

Misconfigured **key policies** are a **frequent** cause of **pipeline** and **batch job** failures—always align **service roles** with **least privilege** on the **key**.

---

## Key rotation

| Rotation mode | Notes |
|---------------|-------|
| **Automatic rotation (CMK)** | KMS can **rotate key material** annually for **symmetric** CMKs while preserving **logical** key ID (behavior documented by AWS). |
| **Manual rotation** | Create a **new** key and **re-encrypt** or **re-wrap** data keys depending on migration strategy. |
| **Alias repointing** | **Aliases** can be moved to **new** key versions or keys during controlled **cutovers**. |

Rotation strategy must account for **replication**, **backups**, and **multi-Region** keys if used.

---

## Audit and compliance

- **CloudTrail** logs **KMS API** usage (who decrypted what **key**, subject to **data** logging options).
- **Separation of duties:** restrict **`kms:Admin`** to **security** roles; **`kms:Encrypt/Decrypt`** to **application** roles.

---

## Hands-On Labs

- [Lab 07: CodePipeline Encryption](../labmanuals/lab07-aws-codepipeline-encryption.md)

---

Last updated: March 2026
