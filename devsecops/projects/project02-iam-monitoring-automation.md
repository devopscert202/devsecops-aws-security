# Project 02: Automating IAM Access Key Monitoring with Lambda and EventBridge

**Lesson:** 2 — AWS Cloud Security Fundamentals  
**Source:** Lesson 02 — Lesson End Project — Automating Security Monitoring for AWS IAM Access Key Creation

## Overview

Build an automated monitoring path that detects **IAM access key creation** (`CreateAccessKey`), forwards the event to **AWS Lambda** via **Amazon EventBridge**, and persists an audit record in **Amazon DynamoDB**. AWS CloudTrail supplies the API activity that EventBridge matches.

## Architecture (high level)

```text
CreateAccessKey (IAM API)
    → CloudTrail (management events)
    → EventBridge rule (IAM, CreateAccessKey)
    → Lambda function
    → DynamoDB table (audit record)
```

---

## Prerequisites

- Permissions to create CloudTrail trails, S3 buckets, IAM roles, Lambda, DynamoDB, and EventBridge rules.
- Python **3.13** runtime available in your target Region for Lambda.

---

## Steps

### 1. Create a CloudTrail trail

1. Open **CloudTrail** in the AWS Management Console.
2. Create a trail with name: **`iam-audit-trail`**.
3. **Storage:** Create a **new S3 bucket** for log delivery.  
   - For this lab, **disable KMS encryption** on the bucket/trail if prompted (follow instructor/account policy if different).
4. **CloudWatch Logs:** Enable delivery to CloudWatch Logs.
5. Create or assign an **IAM role** that allows CloudTrail to write to CloudWatch Logs (use the console wizard to create the role if offered).

Ensure the trail logs **management events** (default for multi-Region trails includes IAM control-plane activity in each Region as configured).

### 2. Create the Lambda function

1. Open **Lambda** and **Create function**.
2. **Runtime:** Python **3.13**.
3. **Function code:** Copy the implementation from the course repository file:

   `devsecops/labs/aws/lambda-iam-monitor.py`

   That function expects:

   - Environment variable **`TABLE_NAME`** (default in code: `iamkey_storer`) — set this to match your DynamoDB table name.
   - Environment variable **`REGION`** (default: `us-east-1`) — set to the Region where the table and function run.

4. **Timeout:** Set to **2 minutes 3 seconds** (**123** seconds).
5. **Execution role:** Attach **`AmazonDynamoDBFullAccess`** to the Lambda execution role for this lab.  
   - **Production note:** Replace with a least-privilege policy that allows only `dynamodb:PutItem` (and any needed `GetItem`/`DescribeTable`) on your specific table ARN.

### 3. Create the DynamoDB table

1. Open **DynamoDB** → **Tables** → **Create table**.
2. **Table name:** `iamkey_storer`
3. **Partition key:** `cloudtrail_key` (type **String**)
4. Create the table in the **same Region** as the Lambda function.

### 4. Create the EventBridge rule

1. Open **Amazon EventBridge** → **Rules** → **Create rule**.
2. **Event source:** AWS service → **IAM**.
3. **Event type:** **AWS API Call via CloudTrail**.
4. **Specific operation:** **`CreateAccessKey`**.
5. **Target:** Select the Lambda function from step 2.
6. Approve any prompt to add **Lambda invoke permissions** for EventBridge.

### 5. Test by creating an IAM access key

1. Open **IAM** → **Users** → select a test user (or create a lab user).
2. **Security credentials** → **Create access key**.
3. Choose a use case such as **Command Line Interface (CLI)** and complete the wizard.

### 6. Monitor results

1. **DynamoDB:** Open table **`iamkey_storer`** → **Explore table items** (or use the console item viewer) and confirm a **new item** appeared with fields such as `cloudtrail_key`, `access_key`, `created_on`, `sourceIPAddress`, and `userName` (as written by the sample Lambda).
2. **CloudWatch Logs:** Open the **Log group** for your Lambda function and verify log output including the serialized event and successful execution.

---

## Cleanup

Remove resources in an order that respects dependencies:

1. EventBridge **rule** (disable/delete).
2. **Lambda** function.
3. **DynamoDB** table `iamkey_storer`.
4. CloudTrail **trail** `iam-audit-trail`.
5. **S3 bucket** used for CloudTrail (empty the bucket, then delete; delete any bucket policy if required).
6. **CloudWatch Logs** log group for the trail/Lambda if you want a full reset.
7. **IAM roles** created only for this lab (CloudTrail to CloudWatch, Lambda execution) if no longer needed.

---

## Reference implementation

The Lambda handler processes EventBridge’s CloudTrail-shaped `detail`, extracts `responseElements.accessKey`, and writes one item per event. See:

`devsecops/labs/aws/lambda-iam-monitor.py`
