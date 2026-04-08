# Lab 12: Creating an IAM User and Attaching Permissions

**Difficulty:** Beginner  
**Estimated time:** 20 minutes

## Prerequisites

- AWS account with **IAM** permissions to create users, groups, and attach managed policies
- A **second browser profile** or **private window** is helpful for testing console sign-in as the new user without logging out your admin session (optional)

## Learning objectives

- Create an IAM user with **AWS Management Console** access
- Assign permissions via a **group** or **direct policy** attachment
- Validate that the user can perform allowed actions (EC2 in this lab)
- Remove lab identities cleanly

## Overview

IAM **users** represent people or applications that need long-term credentials in an account. Best practice is **least privilege** and **group-based** permissions. For learning, this lab attaches **AmazonEC2FullAccess** so you can clearly verify EC2 access—**do not** copy this pattern to production without narrowing permissions to real job functions.

## Steps

1. Open **IAM** in the console → **Users** → **Create user**.
2. **User name:**

   ```text
   devsecops-lab-user
   ```

3. Under **AWS access type** (or **Console access**), enable **AWS Management Console access** for the lab.
4. Choose **Custom password**, set a strong password, and for the lab **clear** **Users must create a new password at next sign-in** if you want a single known password for the exercise (your org may require password reset on first login—in that case, complete the forced reset during verification).
5. Choose **Next**.
6. On **Set permissions**, choose **one** of:
   - **Add user to group** → **Create group**  
     - Group name: e.g. `devsecops-lab-group`  
     - Attach policy: search **`AmazonEC2FullAccess`** and select it  
     - Create the group and ensure `devsecops-lab-user` is a member  
   - **Attach policies directly** → search **`AmazonEC2FullAccess`** and select it  
7. Choose **Next** → review → **Create user**.
8. Note the **Console sign-in URL** for your account (IAM shows the account-specific sign-in link). You will need:
   - Account alias or **12-digit account ID**
   - User name `devsecops-lab-user`
   - The password you set
9. **Verify as the new user:**
   - Open an incognito/private window (or a different browser profile).
   - Sign in to the IAM console URL with `devsecops-lab-user`.
   - Open **EC2** and confirm you can reach the EC2 dashboard and list resources (exact actions depend on Region and account contents).
10. Confirm the user **cannot** access unrelated services if you want an extra check—for example, **IAM** should return **access denied** for creating users (unless policy allows it). `AmazonEC2FullAccess` does **not** grant IAM admin; you should see denial on IAM mutations.

## Verification steps

- User `devsecops-lab-user` exists and is in `devsecops-lab-group` **or** has `AmazonEC2FullAccess` attached directly.
- Console sign-in succeeds with the lab password (or after first-sign-in reset, if enforced).
- From that session, **EC2** console loads without authorization errors for read/list operations.

## Troubleshooting tips

- **Cannot sign in:** Use the **account-specific** IAM URL, not the root email login page, unless you use IAM Identity Center (SSO)—this lab assumes standard IAM user URL.
- **Access denied in EC2:** Confirm the managed policy **`AmazonEC2FullAccess`** is attached to the user or group, and that you are in a Region where you have resources or permissions to describe EC2.
- **MFA required by SCP or policy:** Complete MFA setup (see Lab 13) or use an account without that guardrail for this exercise.

## Cleanup

1. Sign back in with your **administrator** credentials.
2. **IAM** → **Users** → select `devsecops-lab-user` → **Delete user** (remove **access keys**, **signing certificates**, and **password** if prompted).
3. **IAM** → **User groups** → select `devsecops-lab-group` (if created) → remove members → **Delete group**.

**Security note:** In production, prefer **job-function** policies, **permission boundaries**, and **no** broad `FullAccess` unless strictly required and approved.

## Summary

You created `devsecops-lab-user` with console access, granted **EC2 full access** for demonstration, verified the experience from a separate sign-in, and cleaned up the user and group.

## Related resources

- [IAM Best Practices](../docs/advanced/iam-best-practices.md)
