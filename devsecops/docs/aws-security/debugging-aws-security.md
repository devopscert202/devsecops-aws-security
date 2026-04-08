# Debugging in AWS Cloud Security

*Concepts for systematic troubleshooting of access, networking, and CI/CD issues using AWS observability and IAM tools—without procedural lab steps.*

---

## What is debugging in the AWS context?

**Debugging** in AWS means **narrowing down** why something failed or behaved unexpectedly: an API call denied, a resource unreachable, a pipeline stage red, or a compliance check failing. It blends **cloud knowledge** (how IAM, VPC, and services interact) with **evidence** from logs and tools.

---

## Why it matters

| Benefit | Explanation |
|---------|-------------|
| **Faster incident response** | Clear hypotheses reduce mean time to resolve (MTTR) when production is impacted. |
| **Compliance** | Demonstrating that you **investigate** and **document** access and configuration issues supports audits. |
| **Root cause analysis** | Fixes stick when you address policy, architecture, or process—not only symptoms. |
| **Security culture** | Teams learn recurring mistake patterns (overly broad SGs, missing conditions, stale keys). |

---

## Tools commonly used for security debugging

| Tool | Typical use |
|------|-------------|
| **AWS CloudTrail** | Who called which API, from where, success or failure; essential for IAM and configuration changes. |
| **Amazon CloudWatch** | Metrics and logs for services, Lambda, CodeBuild, custom application logs; alarms for anomalies. |
| **VPC Flow Logs** | Accept/reject decisions at ENI level; debugging **security group** and **NACL** effects and unexpected traffic. |
| **AWS Config** | **What changed** on resources over time; rules for compliance drift (e.g., public S3). |
| **IAM Access Analyzer** | Identifies **external access** paths to resources; helps find unintended public or cross-account exposure. |
| **IAM Policy Simulator** | Tests whether a **principal** is allowed or denied a specific action on a resource (given current policies). |

---

## Debugging IAM: common issues and evaluation logic

**Common permission issues**

- **Explicit deny** anywhere in the policy stack wins over allows.
- **Missing** `Allow` on the identity **or** resource policy (for services that use resource policies).
- **Condition keys** not satisfied (MFA present, IP range, source VPC, time window).
- **Session policies** or **permission boundaries** further restricting effective permissions.
- **SCPs** in AWS Organizations blocking the action at the account or OU level.

**Policy evaluation (conceptual)**

1. Gather all policies: identity-based, resource-based, session, boundary, SCPs (if applicable).
2. If any applicable policy **denies**, the request is **denied**.
3. Otherwise, there must be at least one **allow** that applies; default is **deny**.

Use **CloudTrail** `AccessDenied` events with error messages, then **Policy Simulator** or **policy analysis** in the console to isolate which statement caused the outcome.

---

## Debugging CodePipeline

| Symptom class | Often points to |
|---------------|----------------|
| **Build failures** | Buildspec errors, missing dependencies, wrong runtime, **CodeBuild** role lacking ECR/S3/Logs permissions. |
| **Permission errors** | Stage role cannot read artifact bucket, decrypt KMS key, or invoke deployment target; check **trust policy** and **key policy**. |
| **Artifact issues** | Wrong bucket/prefix, encryption key not granted to the consuming stage, **object not found** after retention or lifecycle rules. |

Correlate **CodePipeline execution history** with **CloudWatch Logs** for the build and **CloudTrail** for API denials in the same time window.

---

## Use case: security group misconfigurations and Trusted Advisor

**AWS Trusted Advisor** (with appropriate support plan) can highlight **open ports**, **overly permissive security groups**, and related **fault tolerance / security** checks. For debugging:

1. Identify the **ENI** and **security group** attached to the instance or LB.
2. Compare **inbound rules** to least privilege (source CIDRs, port ranges).
3. Use **VPC Flow Logs** to see whether traffic is **rejected** and from which source.
4. Remediate rules; re-test; document the change for change management.

Trusted Advisor complements—but does not replace—**Config rules** and **manual** architecture review.

---

## Hands-On Labs

- [Lab 08: Security Group Validation](../labmanuals/lab08-aws-security-group-validation.md)
- [Lab 09: CloudTrail Debugging](../labmanuals/lab09-aws-cloudtrail-debugging.md)

---

Last updated: March 2026
