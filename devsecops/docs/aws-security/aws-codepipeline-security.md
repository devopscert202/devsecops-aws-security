# Security in AWS CodePipeline

*Concepts for protecting CI/CD: encryption, identity, observability, compliance alignment, and resilience—without pipeline lab steps.*

---

## Overview

**AWS CodePipeline** orchestrates release stages (source, build, test, deploy). Securing a pipeline means protecting **artifacts and metadata**, **who can trigger and promote**, **audit evidence**, and the **downstream infrastructure** that stages touch.

---

## Core security aspects

| Aspect | What it covers |
|--------|----------------|
| **Data protection** | Source code, build artifacts, logs, and parameters (secrets, tokens) from theft or tampering. |
| **IAM** | Least-privilege roles per stage; no long-lived keys in buildspecs when roles suffice. |
| **Logging** | Who did what, when—which API calls and stage outcomes support investigations. |
| **Compliance** | Mapping controls (e.g., encryption, access reviews) to frameworks your org must meet. |
| **Resilience** | Pipelines that fail safe; protected branches; rollback and approval patterns. |
| **Infrastructure** | Hardening build projects (CodeBuild), deployment targets, and integration services. |

---

## KMS encryption for artifacts

Pipeline artifacts often pass through **Amazon S3** buckets and **CodePipeline**-managed staging. **AWS KMS** keys can encrypt:

- **Artifacts at rest** in the artifact store (customer-managed or AWS-managed CMKs).
- **Data in transit** between stages when combined with TLS for API and console access.

Using **customer-managed keys (CMKs)** improves **key policy** control, **rotation** options, and **audit** trails (CloudTrail on KMS). Align key policies with the **pipeline service role** and **CodeBuild** roles so encryption does not break least privilege.

---

## IAM roles and policies for pipeline stages

Each stage should use a **dedicated IAM role** with permissions **scoped** to that stage’s needs:

- **Source:** Read from CodeCommit, S3, or GitHub (via CodeStar Connections) with minimal repo scope.
- **Build:** Access to ECR pull/push if needed, CloudWatch Logs, and specific S3 prefixes—not `*`.
- **Deploy:** Deploy only to approved targets (e.g., specific CloudFormation stacks, CodeDeploy applications, ECS services).

Use **permission boundaries** and **SCPs** (Organizations) to cap what pipeline roles can ever obtain. Avoid reusing one **overpowered** role for every stage.

---

## CloudTrail and CloudWatch for audit

- **AWS CloudTrail** records management API usage (who changed the pipeline, roles, or KMS policies).
- **Amazon CloudWatch Logs** captures **CodeBuild** and integration logs for **operational** and **security** monitoring.

Together they support **detection** (failed auth spikes), **non-repudiation**, and **compliance** evidence that pipeline activity was logged and retained per policy.

---

## Compliance context (examples)

AWS services are **in scope** for many AWS compliance programs; **your** configuration must still meet control objectives:

| Framework (examples) | Pipeline-relevant themes |
|----------------------|-------------------------|
| **SOC** | Logical access, change management, logging, encryption. |
| **PCI-DSS** | Protect cardholder data environments; restrict CDE access from generic build roles; strong authentication for changes. |
| **HIPAA** | PHI only in approved accounts and services; BAA in place; encryption and minimum necessary access for build/deploy paths that touch regulated systems. |

Map **each stage** to data classification and control requirements; do not treat “CI” as outside compliance scope.

---

## Use case: secure CI/CD for a banking application

- **Segregation:** Separate accounts for **dev / test / prod**; pipeline promotions require **manual approval** or **gated automation** with break-glass procedures.
- **Secrets:** No secrets in source; use **Secrets Manager** or **SSM Parameter Store** with IAM-scoped retrieval from CodeBuild.
- **Artifacts:** **KMS-encrypted** artifact bucket; block public access; short-lived presigned URLs if needed.
- **Immutable builds:** Tag images and artifacts with **commit SHA**; deploy only signed or scanned artifacts that passed **SAST/DAST** policy.
- **Audit:** CloudTrail organization trail; **CloudWatch** alarms on pipeline failures and IAM changes; retention aligned to banking policy.

---

## Hands-On Labs

- [Lab 07: CodePipeline Encryption](../labmanuals/lab07-aws-codepipeline-encryption.md)

---

Last updated: March 2026
