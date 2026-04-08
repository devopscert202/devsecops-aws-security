# AWS Shared Responsibility Model

*How AWS and the customer split security work in the cloud—and how that boundary shifts by service model.*

---

## Overview

Under the **shared responsibility model**, **AWS** operates **security *of* the cloud** (the platform AWS builds and runs). The **customer** operates **security *in* the cloud** (how services are configured and used). Both sides must meet their obligations for a defensible, compliant workload.

---

## ASCII diagram — AWS vs customer

```
+---------------------------  CUSTOMER: "Security IN the cloud"  ---------------------------+
|  Data classification & encryption choices, IAM policies, OS patching (where you manage |
|  the OS), network controls (security groups, NACLs, firewalls), application code,       |
|  client-side encryption, access policies, compliance tasks you own in shared regimes    |
+----------------------------------------||------------------------------------------------+
                                         ||
                    =======================||=======================
                    ||  Boundary shifts   ||  by service (IaaS vs PaaS vs SaaS)
                    =======================||=======================
                                         ||
+----------------------------------------||------------------------------------------------+
|  AWS: "Security OF the cloud"                                                            |
|  Physical data centers & hardware, global infrastructure, virtualization layer where |
|  AWS operates it, managed control planes, foundational patching of AWS-managed stacks    |
+------------------------------------------------------------------------------------------+
```

---

## AWS: Security *of* the cloud

AWS is responsible for protecting the **global infrastructure** that runs all offered services. Conceptually, this includes:

| Area | AWS responsibility (summary) |
|------|------------------------------|
| **Physical security** | Facilities, perimeter controls, asset disposal, environmental protections. |
| **Network infrastructure** | AWS-operated backbone and data-center networking that underpins services. |
| **Hypervisor & host stack** | Where AWS provides virtualization, AWS secures the hypervisor and host OS **for services it defines as AWS-managed** at that layer. |
| **Managed service planes** | Operation and hardening of the **managed** components (e.g., RDS database engine management, Lambda service infrastructure, S3 storage layer). |

Exact split is **service-specific**; see AWS documentation for each service.

---

## Customer: Security *in* the cloud

The customer configures and uses cloud resources responsibly. Typical customer-owned areas include:

| Area | Customer responsibility (summary) |
|------|-------------------------------------|
| **Guest OS & middleware** | For EC2 and similar, patching and hardening the **guest** OS and installed software. |
| **Network security configuration** | Security groups, NACLs, routing, VPC design, TLS on endpoints you expose. |
| **Encryption & keys** | Choosing encryption, managing CMKs (where customer-managed), rotating application secrets. |
| **IAM** | Who can invoke APIs, assume roles, access data—policies, boundaries, and federation. |
| **Data** | Classification, access policies, backups, and retention aligned to regulation and risk. |

---

## Service-specific examples

| Service | AWS tends to manage | Customer tends to manage |
|---------|---------------------|---------------------------|
| **EC2** | Physical host, hypervisor (Nitro), underlying network fabric | Guest OS, application, security groups, IAM to the instance, data on volumes, encryption choices (e.g., EBS encryption with customer or AWS keys). |
| **RDS** | Database **engine** patching for managed RDS, underlying storage and failover infrastructure | **Data**, DB user accounts, parameter groups that affect security, VPC placement, encryption options, IAM/database auth integration, backup/restore policy choices. |
| **Lambda** | Runtime execution environment **platform**, patching of the managed runtime **as AWS defines** | **Function code**, dependencies, IAM **execution role**, environment variables (secrets handling), VPC configuration when used, data accessed by the function. |
| **S3** | Durability and availability of the object store; service-side enforcement mechanisms | **Bucket policies, ACLs (if used), IAM**, encryption settings (SSE-S3 vs SSE-KMS), public access blocks, object ownership, logging, lifecycle and versioning choices. |

These examples simplify; always read the **official shared responsibility** page for the exact service.

---

## Benefits of the model

- **Clarity:** Reduces ambiguity about who patches what and who configures access.
- **Scale:** Customers inherit world-class physical and network protections without building data centers.
- **Flexibility:** Customers retain control over data, identities, and application security where regulations require it.
- **Shared innovation:** AWS improves the platform; customers adopt new security features (e.g., encryption options) through configuration.

---

## Hands-On Labs

- [Lab 08: Security Group Validation](../labmanuals/lab08-aws-security-group-validation.md)

---

Last updated: March 2026
