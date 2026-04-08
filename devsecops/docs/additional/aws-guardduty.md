# Amazon GuardDuty

*Managed threat detection for AWS accounts and workloads: telemetry sources, finding families, and Security Hub integration—reference material without a dedicated lab.*

---

## What is Amazon GuardDuty?

**Amazon GuardDuty** is a **threat detection** service that continuously analyzes signals from your AWS environment. It applies **machine learning**, **anomaly detection**, and **threat intelligence** to surface **suspicious** or **malicious** activity **without** requiring you to deploy agents on every host for core functionality (some **optional** protections extend coverage for specific workloads).

GuardDuty is primarily a **detective** control: it **produces findings**; blocking or remediating typically involves **automation** (e.g., EventBridge rules, Lambda, Systems Manager), **Security Hub** workflows, or **manual** response runbooks.

---

## Why teams enable GuardDuty

| Reason | Explanation |
|--------|-------------|
| **Breadth** | Monitors **account** and **network** behaviors that span many services. |
| **Low friction** | One-click or API enablement per Region; integrates with existing logs where configured. |
| **Continuous** | Runs 24/7 as AWS-managed analysis—not a point-in-time scan only. |
| **Integration** | Feeds **AWS Security Hub** in **ASFF** for centralized triage. |

GuardDuty does **not** replace **vulnerability scanning** (see **Inspector**), **data classification** (**Macie**), or **configuration compliance** (**Config**); it **complements** them.

---

## Data sources

GuardDuty consumes **AWS-generated** telemetry. Availability and behavior can vary by **Region** and **optional feature** enablement. Conceptually:

| Data source | What GuardDuty analyzes |
|-------------|-------------------------|
| **AWS CloudTrail management events** | Unusual API sequences, possible credential misuse, discovery of resources or permissions. |
| **VPC Flow Logs** | Connection patterns suggestive of scanning, command-and-control, or data movement. |
| **DNS logs** | Queries that may indicate malware, phishing infrastructure, or DNS tunneling (where DNS telemetry is available to the service). |
| **EKS audit logs** | Kubernetes API activity that may indicate cluster or workload compromise when **EKS-related** protections are enabled. |

You must still **configure** underlying logging (e.g., **Flow Logs** to a supported destination, **EKS** control-plane logging) for full **coverage**; enabling GuardDuty alone does not create missing telemetry.

---

## Finding types (high-level)

Findings are typed and **severitized**; exact **types** evolve as AWS adds **detectors**. Groupings useful for triage:

### Reconnaissance

Activity suggesting **mapping** of the environment: broad **API** enumeration, port **scanning**, or systematic **discovery** before exploitation.

### Instance / workload compromise

Indicators that an **EC2 instance**, **container**, or related workload may be **compromised**: communication with **known-malicious** IPs, cryptocurrency mining patterns, or other **behavioral** signals inferred from network and CloudTrail context.

### Account compromise

Suspicious use of **IAM users or roles**: logins from unusual locations, **API** patterns inconsistent with baselines, or attempts to **persist** or **escalate** access.

### Data exfiltration or unusual access

Patterns consistent with **large** or **odd** data transfers, or access to **sensitive** APIs and storage in ways that deviate from normal operations.

Always read the **finding detail** in the console or **Security Hub** for **resource ARNs**, **evidence**, and **remediation** hints; **severity** is a prioritization aid, not a verdict by itself.

---

## Integration with AWS Security Hub

When **Security Hub** is enabled and **GuardDuty** is configured as a **source**:

1. GuardDuty generates findings in its **native** format.
2. Security Hub **imports** and **normalizes** them to **ASFF** (**AWS Security Finding Format**).
3. You can **search**, **filter**, **deduplicate** alongside **Inspector**, **Macie**, **Config**, and **partner** findings.
4. **Automation** can route ASFF events via **EventBridge** to ticketing or remediation.

This **single-pane** workflow reduces **context switching** during incidents and **compliance** reporting.

---

## Operational concepts

| Topic | Guidance |
|-------|----------|
| **Multi-Region** | Threats do not respect Region boundaries; many teams enable GuardDuty in **every** in-use Region. |
| **Delegated admin** | In **Organizations**, a **delegated administrator** account can **aggregate** member findings for security operations. |
| **Suppression rules** | Use carefully to reduce **noise** without hiding **true** risks; document rationale. |
| **Cost** | Pricing is usage-based (e.g., volume of analyzed events); monitor **Cost Explorer** after enablement. |

---

## Relationship to other AWS security services

| Service | Distinction |
|---------|-------------|
| **AWS Config** | **Compliance** and **configuration drift** rules—not the same as behavioral threat detection. |
| **Amazon Inspector** | **Vulnerability** assessment for **EC2**, **ECR** images, and **Lambda**—complements GuardDuty’s **runtime** signals. |
| **Amazon Macie** | **Sensitive data discovery** in **S3**—orthogonal to GuardDuty’s primary threat use cases. |
| **Security Hub** | **Aggregation** and **standards**—orchestrates response across findings. |

---

## Limitations (conceptual)

- GuardDuty **detects**; **response** is your **runbook** and **automation**.
- **False positives** can occur; tune **suppressions** and **correlate** with **CloudTrail** and **application** logs.
- **Coverage gaps** exist if **logging** is off, **Regions** are unused but unmonitored, or **legacy** architectures bypass observed telemetry.

---

## Finding lifecycle (conceptual)

Understanding how a finding moves through states helps you design **triage** and **metrics**:

1. **Generation:** A detector matches telemetry to a **threat** or **anomaly** model and opens a finding with a **unique ID**.
2. **Enrichment:** The console and APIs show **affected resources**, **principal** context (when available), and **MITRE**-style **tactics** in many cases.
3. **Notification:** **EventBridge** can fan out **new** or **updated** findings to email, chat, or SOAR.
4. **Investigation:** Analysts pivot to **CloudTrail**, **VPC Flow Logs**, **Config** timeline, or **application** logs.
5. **Remediation:** **Contain** (isolate SG, revoke sessions), **eradicate** (rebuild instance), **recover** (restore from known-good), and **document**.
6. **Closure:** Mark **archived** or **suppressed** per process; feed lessons into **preventive** controls (IAM, patching, segmentation).

---

## Optional protections and extended coverage

AWS periodically introduces **optional** GuardDuty capabilities (names and scope change over time). Conceptually, these extend analysis beyond **core** CloudTrail + VPC + DNS:

- **Malware protection** for **EC2** (scanning behavior tied to backup volumes—understand **privacy** and **data handling** in your jurisdiction).
- **EKS** protection leveraging **Kubernetes** audit logs when enabled.
- **Runtime monitoring** for **Fargate** or **EC2** in some offerings.

Always review the **official** product page for your **Region** and **version** before enabling paid features.

---

## Triage checklist (for operators)

| Step | Action |
|------|--------|
| 1 | Confirm **account**, **Region**, and **resource ARN** in the finding. |
| 2 | Check **first seen** / **last seen** to judge ongoing vs historical noise. |
| 3 | Correlate with **CloudTrail** in the same window for **API** attribution. |
| 4 | For network findings, inspect **Flow Logs** for **source/dest** and **bytes**. |
| 5 | Escalate to **application owner** if the resource is shared or **multi-tenant**. |
| 6 | Record **outcome** in your **IR** system for **trends** and **audit**. |

---

## IAM and organization patterns (concept)

- **Enablement** requires permissions such as `guardduty:CreateDetector` (exact actions per your **IAM** strategy).
- **Delegated administrator** in **AWS Organizations** lets a **security** account manage **member** accounts without sharing **break-glass** credentials broadly.
- **Cross-account** roles for **SOC** should still follow **least privilege**—read findings and **update** status without **admin** on workloads.

---

## Hands-On Labs

There is **no dedicated hands-on lab** for Amazon GuardDuty in this curriculum. Use this page as **reference** while working through **[Lab 11: AWS Security Hub](../labmanuals/lab11-aws-security-hub.md)** and broader AWS security labs where findings appear in the **aggregated** view.

---

Last updated: March 2026
