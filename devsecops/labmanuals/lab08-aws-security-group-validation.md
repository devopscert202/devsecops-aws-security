# Lab 08: Validating Security Group Misconfigurations with AWS Trusted Advisor

**Difficulty:** Beginner  
**Estimated time:** 20 minutes

## Prerequisites

- An AWS account where you can create and delete EC2 security groups
- Permission to use the EC2 and **AWS Trusted Advisor** consoles (some checks are available to all accounts; a few advanced checks require an eligible [AWS Support plan](https://aws.amazon.com/premiumsupport/plans/))
- Your current public IP address (for the LDAP rule). Find it from your workstation:

```bash
curl -s https://checkip.amazonaws.com
```

Copy the output (for example `203.0.113.10`) and append `/32` when you add the rule in the console.

## Learning objectives

- Create a security group with both **intentionally unsafe** and **restricted** inbound rules
- Use Trusted Advisor security checks to detect overly permissive network access
- Interpret findings for unrestricted SSH and RDP
- Remove lab resources safely after the exercise

## Overview

Security groups act as virtual firewalls for EC2 instances and other resources. Allowing SSH (port 22) or RDP (port 3389) from `0.0.0.0/0` exposes administrative access to the entire internet and is a common misconfiguration. In this lab you will create a group with deliberate bad rules and a good rule, then use **AWS Trusted Advisor** to review security recommendations. The open SSH and RDP rules are **only for this exercise**—never deploy this pattern in production.

## Steps

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) and open **EC2**.
2. In the left navigation, under **Network & Security**, choose **Security groups**.
3. Choose **Create security group** and configure:
   - **Security group name:** `devsecops-lab-sg`
   - **Description:** e.g. `DevSecOps lab – intentional misconfigurations for Trusted Advisor (delete after lab)`
   - **VPC:** Select your lab VPC (default VPC is fine if allowed by your organization).
4. Under **Inbound rules**, choose **Add rule** and add the following **intentionally misconfigured** rules:

   | Type | Protocol | Port range | Source   | Purpose (lab only)        |
   |------|----------|------------|----------|---------------------------|
   | SSH  | TCP      | 22         | `0.0.0.0/0` | Open to world — **BAD** |
   | RDP  | TCP      | 3389       | `0.0.0.0/0` | Open to world — **BAD** |

5. Add one **restricted** inbound rule (good practice example):

   | Type  | Protocol | Port range | Source              |
   |-------|----------|------------|---------------------|
   | Custom TCP | TCP | 389        | `YOUR_IP/32` (LDAP) |

   Use the `/32` address you obtained in **Prerequisites** (for example `203.0.113.10/32`).

6. Under **Outbound rules**, either keep the default **All traffic** to `0.0.0.0/0` or add outbound rules that **mirror** your inbound intent for the lab (SSH/RDP/LDAP as needed). For a minimal lab, the default outbound rule is sufficient.
7. Choose **Create security group** and confirm the new group appears in the list.
8. Open **Trusted Advisor** from the services search bar (or **AWS Support** → **Trusted Advisor**, depending on your console layout).
9. In the left pane, open **Security** (or the security category that lists port and access checks).
10. Choose **Refresh all checks** (or refresh the relevant security checks) and wait for the refresh to finish.
11. Review findings related to **security groups** and **unrestricted ports**. Trusted Advisor should flag risks for **unrestricted access** on administrative ports such as **22** and **3389** when sourced from `0.0.0.0/0`.
12. Open one of the flagged findings and read the **description** and **recommended action** so you understand **why** `0.0.0.0/0` on SSH/RDP is treated as high risk.

## Verification steps

- The security group `devsecops-lab-sg` exists in the correct VPC with three inbound rules as specified (SSH and RDP from `0.0.0.0/0`, LDAP from your IP only).
- Trusted Advisor (or the security check UI) lists findings that call out **unrestricted** or **public** access for **port 22** and **port 3389** (wording may vary slightly by check name).
- You can explain in one sentence: unrestricted SSH/RDP allows anyone on the internet to attempt connections to those services.

## Troubleshooting tips

- **No Trusted Advisor security findings:** Confirm you are in the **same Region** where you created the security group. Wait a few minutes after creation and choose **Refresh** again. If checks are unavailable, your account may not have access to that category—ask your administrator or try a different Region where you have permissions.
- **LDAP rule shows invalid source:** Ensure the source is a single host in CIDR form (`x.x.x.x/32`), not a bare IP without the mask.
- **Cannot delete the security group later:** A security group must have **no dependencies** (not attached to ENIs or referenced by other rules). Remove associations first, then delete.

## Cleanup

1. In **EC2** → **Security groups**, select `devsecops-lab-sg`.
2. If **Actions** → **Delete security groups** is disabled, remove the group from any **network interfaces** or **instances** first, then retry.
3. Confirm deletion.

**Reminder:** Deliberately open SSH/RDP to `0.0.0.0/0` is for this lab only. In production, use bastion hosts, SSM Session Manager, VPN, or IP-restricted sources.

## Summary

You built a security group with dangerous public SSH and RDP rules and a tighter LDAP rule, then validated that **AWS Trusted Advisor** surfaces unrestricted access as a security concern. Removing the group completes the exercise.

## Related resources

- [Debugging AWS Security](../docs/aws-security/debugging-aws-security.md)
