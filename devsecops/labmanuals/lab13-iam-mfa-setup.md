# Lab 13: Enabling MFA for an IAM User

**Difficulty:** Beginner  
**Estimated time:** 20 minutes

## Prerequisites

- AWS console access with permission to manage IAM user **security credentials**
- A smartphone with an **authenticator app** (this lab uses **Google Authenticator**; **Microsoft Authenticator** and **Authy** are common alternatives that also work with TOTP QR codes)
- An IAM user with **console access** (create `devsecops-lab-user` in [Lab 12](lab12-iam-user-permissions.md) if you do not already have one)

## Learning objectives

- Register a **virtual MFA device** for an IAM user
- Complete the two-code confirmation flow required by AWS
- Sign out and sign back in with **MFA** challenge
- Remove the MFA device and optional user as part of cleanup

## Overview

**Multi-factor authentication (MFA)** adds a second factor on top of a password. For IAM users, a **virtual MFA** application generates time-based one-time passwords (TOTP). This lab assigns MFA to a lab user, validates login behavior, then removes the device.

## Steps

### 1. Prepare or reuse an IAM user

1. If needed, create a user (e.g. `devsecops-lab-user`) with **AWS Management Console** access and a **custom password**.
2. For a smooth lab, **deselect** **Users must create a new password at next sign-in** if your security policy allows it for this exercise—otherwise complete any forced password change before MFA setup.

### 2. Install an authenticator app

1. On your phone, install **Google Authenticator** from the official store (iOS App Store or Google Play).
2. You will use it to scan a **QR code** from the IAM console.

### 3. Assign MFA in IAM

1. Sign in to the console as an administrator (not as the lab user, unless that user may self-manage MFA per your policy).
2. Open **IAM** → **Users** → select the lab user (e.g. `devsecops-lab-user`).
3. Open the **Security credentials** tab.
4. In **Multi-factor authentication (MFA)**, choose **Assign MFA device**.
5. **Device name**, for example:

   ```text
   my-phone-mfa
   ```

6. Select **Authenticator app** (virtual MFA) → **Next**.
7. Choose **Show QR code**.
8. On your phone, open **Google Authenticator** → **+** → **Scan a QR code** and scan the console QR.
9. Enter **two consecutive** 6-digit codes from the app into the IAM wizard (codes rotate about every 30 seconds; wait for a fresh code if one expires).
10. Choose **Add MFA** (or **Assign MFA**) and confirm success.

### 4. Test MFA at sign-in

1. **Sign out** of the console.
2. Open the **IAM user sign-in URL** for your account and sign in as the lab user.
3. When prompted, enter the **current** MFA code from Google Authenticator.
4. Confirm you reach the console home.

## Verification steps

- The user’s **Security credentials** page lists **my-phone-mfa** (or your device name) under MFA.
- A full sign-in flow requires a valid **password** and **MFA code**.
- After removing MFA in cleanup, sign-in should **not** prompt for MFA (verify only in a disposable lab user).

## Troubleshooting tips

- **Invalid MFA code:** Check phone time is set to **automatic**; TOTP is time-sensitive. Wait for the next code rotation.
- **Lost access to MFA device:** As an admin, you can **remove** the MFA device from IAM for the user (requires IAM permissions); keep this in mind for runbooks.
- **QR scan fails:** Use the **manual secret key** entry option in the app if the console offers **Show secret key** for manual configuration.

## Cleanup

1. As an administrator, open **IAM** → **Users** → the lab user → **Security credentials**.
2. Next to the virtual MFA device, choose **Remove** (or **Deactivate** then remove, per console wording).
3. If the user exists only for this lab, delete the user per [Lab 12](lab12-iam-user-permissions.md) cleanup steps.

## Summary

You registered a **virtual MFA** device for an IAM user, confirmed **two-code** enrollment, and validated password+MFA sign-in—then removed the device as part of teardown.

## Related resources

- [IAM Best Practices](../docs/advanced/iam-best-practices.md)
