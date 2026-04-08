# Lab 11: Configuring AWS Security Hub

**Difficulty:** Beginner  
**Estimated time:** 15 minutes

## Prerequisites

- AWS account with permission to enable **AWS Security Hub** and security standards
- Awareness that Security Hub aggregates findings from integrated services; some integrations may have their own pricing

## Learning objectives

- Enable **AWS Security Hub** in a Region
- Turn on one or more **security standards** (e.g. AWS Foundational Security Best Practices, CIS)
- Navigate **Findings** and interpret severity, workflow state, and product fields
- Open a finding to read remediation guidance

## Overview

**AWS Security Hub** gives you a centralized view of security posture across accounts (with Organizations) and services. It can run continuous checks against **security standards** and consolidate findings from services such as GuardDuty, Inspector, and Firewall Manager. This lab enables Security Hub in the console and explores the **Findings** experience.

## Steps

1. Open the [AWS Management Console](https://console.aws.amazon.com/) and go to **Security Hub**.
2. If prompted, choose **Go to Security Hub** (or **Enable Security Hub**).
3. On the setup page, review available **Security standards**, for example:
   - **AWS Foundational Security Best Practices**
   - **CIS AWS Foundations Benchmark**
   - **PCI DSS** (enable only if it applies to your workload and compliance scope)
4. Select the standards you want for the lab (at minimum, **AWS Foundational Security Best Practices** is a common default).
5. Choose **Enable Security Hub** and wait until the console shows that Security Hub is active for the **current Region**.
6. In the left navigation, open **Findings**.
7. Without changing filters, scan the list and note columns such as:
   - **Severity** (e.g. CRITICAL, HIGH)
   - **Workflow status** (e.g. NEW)
   - **Region** and **Account**
   - **Product** (which detector or standard produced the finding)
8. Select a finding to open the detail pane. Read **Description**, **Resources**, and **Remediation** (or **Recommendation**) links if present.
9. Optional: Use the filter bar to narrow by **Severity** = **HIGH** or by a specific **Product name** to see how consolidated views help triage.

## Verification steps

- Security Hub shows as **enabled** in the Region where you performed the steps.
- At least one **security standard** you selected appears as **enabled** (status may show **Recording** or **Passed/Failed** controls after initial evaluation).
- The **Findings** page lists items (it may take time for new accounts to populate; some controls run on a schedule).

## Troubleshooting tips

- **Empty findings list:** New or pristine accounts may have few findings initially. Run other security services in the lab account (or wait for control evaluations) to see more data.
- **Cannot enable a standard:** Verify IAM permissions (`securityhub:*` or managed policies for Security Hub administrators) and that you are in the intended **Region**.
- **Charges:** Security Hub offers a free tier for finding ingestion and usage; beyond that, pricing is usage-based. Disable Security Hub when the lab is complete if you do not need it.

## Cleanup

1. Open **Security Hub** → **Settings** (or **General** settings, depending on console version).
2. **Disable** Security Hub for the Region if you no longer need it, or **disable individual standards** to reduce evaluations.
3. Confirm with your organization’s cloud governance policy before disabling Security Hub in shared accounts.

## Summary

You enabled **AWS Security Hub**, turned on selected **security standards**, and explored how **Findings** present severity, workflow, Region, account, and source product—plus remediation hints for individual issues.

## Related resources

- [AWS Security Hub](../docs/advanced/aws-security-hub.md)
