# Lab 09: Debugging with AWS CloudTrail

**Difficulty:** Beginner  
**Estimated time:** 20 minutes

## Prerequisites

- AWS account with permission to create CloudTrail trails and S3 buckets
- Ability to create and delete S3 buckets in the Region where you run the lab (bucket names must be **globally unique** across all of AWS)

## Learning objectives

- Create an organizational or single-account **CloudTrail** trail that delivers logs to Amazon S3
- Confirm the trail is **logging** and **active**
- Use **Event history** to filter and inspect management events
- Read event details: source, identity, request parameters, and response

## Overview

**AWS CloudTrail** records AWS API activity (who did what, when, and from where). Trails persist a continuous stream of events to S3 (and optionally to CloudWatch Logs). This lab walks through creating a simple trail with a new bucket and **without** SSE-KMS on the trail (for simplicity), then using **Event history** to explore real API calls—such as the `CreateTrail` call you just made.

## Steps

1. Open the [AWS Management Console](https://console.aws.amazon.com/) and go to **CloudTrail**.
2. In the left navigation, choose **Trails**, then **Create trail**.
3. Under **Trail name**, enter a name, for example:

   ```text
   devsecops-audit-trail
   ```

4. For **Storage location**, choose **Create new S3 bucket**.  
   - Edit the suggested bucket name if the default is already taken (S3 bucket names are globally unique).  
   - Example pattern:

   ```text
   devsecops-audit-trail-logs-<your-alias-or-random-suffix>
   ```

5. Under **Log file SSE-KMS encryption options**, choose **Disabled** (or the option that **does not** use a KMS key for this lab). This keeps setup minimal; in production you often enable encryption with a customer managed KMS key.
6. Leave other options at defaults unless your organization requires a specific configuration (for example, **Organization trail** only applies if you manage an AWS Organization).
7. Choose **Next** through any remaining steps and then **Create trail**.
8. On the trail details page, confirm **Logging** is **On** and the trail status is **Active** (or equivalent wording in your console version).
9. In the left navigation, choose **Event history** (for management events in the last 90 days in this Region).
10. Use the filters to narrow events:
    - **Time range** — last hour or custom range when you created the trail
    - **Event name** — e.g. `CreateTrail`, `CreateBucket`, `PutBucketPolicy`
    - **Resource type** — e.g. `AWS::S3::Bucket`, `AWS::CloudTrail::Trail`
11. Select an event such as **CreateTrail** and open its details. Review:
    - **Event source** (e.g. `cloudtrail.amazonaws.com`)
    - **User name** / **ARN** under **User identity**
    - **Request parameters** (trail name, S3 bucket name, etc.)
    - **Response elements** (success indicators, resource IDs)
12. Set **Resource type** to **S3 bucket** (or filter events involving S3) and locate events tied to the bucket CloudTrail created for log delivery.

## Verification steps

- Trail `devsecops-audit-trail` (or the name you chose) shows **logging enabled** and references your new S3 bucket.
- In **Event history**, you can find at least one **CreateTrail** (or related) event from your session.
- You can identify the **principal** (IAM user or role) that invoked the API in a sample event.

## Troubleshooting tips

- **Bucket name already exists:** Change the suffix until creation succeeds; S3 names are global.
- **Insufficient permissions to create trail:** Your IAM principal needs CloudTrail and S3 permissions (and often `kms` if you enable KMS). Use an admin role for the lab or ask for a scoped policy.
- **No events in Event history:** Select the correct **Region**, widen the **time range**, and ensure you are viewing **Event history** (not only a custom trail insight without data yet). New trails can take a short time before delivery-related events appear.

## Cleanup

Delete resources in this order to avoid dependency errors:

1. **CloudTrail:** Open your trail → **Stop logging** if shown → **Delete trail**.
2. **S3:** Open the bucket used for logs → **Empty** the bucket (delete all object versions if versioning was on) → **Delete bucket**.

If CloudTrail created a bucket policy or notifications, removal completes when the bucket is deleted after emptying.

## Summary

You configured a basic CloudTrail trail to S3, confirmed logging, and used **Event history** with filters to audit API activity—including S3-related events tied to the new bucket.

## Related resources

- [Debugging AWS Security](../docs/aws-security/debugging-aws-security.md)
