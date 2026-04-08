# Lab 07: Implementing Encryption for AWS CodePipeline

**Difficulty:** Intermediate | **Time:** 40 minutes

## Prerequisites

- AWS Console access
- GitHub account

## Overview

Create a secure CI/CD pipeline using AWS CodePipeline with KMS-encrypted artifacts stored in S3. This lab demonstrates data protection in transit and at rest for build artifacts.

## Steps

### Part 1: Create an S3 Bucket with KMS Encryption

1. Import the Maven build repository to your GitHub account:
   - Go to [https://github.com/new/import](https://github.com/new/import).
   - **Source URL:** `https://github.com/anujdevopslearn/MavenBuild`

2. Open **AWS Console** → **S3** → **Create bucket**.

3. Configure the bucket:
   - **Bucket type:** General purpose
   - **Name:** `codepipelineartifact-YOURNAME` (must be globally unique)
   - Leave other defaults

4. Under **Default encryption**:
   - **Encryption type:** **Server-side encryption with AWS KMS keys (SSE-KMS)**
   - **AWS KMS key:** Select **Enter AWS KMS key ARN**

5. Click **Create a KMS key** (opens in new tab):
   - **Key type:** Symmetric
   - **Key usage:** Encrypt and decrypt
   - Click **Next**
   - **Alias:** `artifacts-key`
   - Click **Next**
   - **Key administrators:** select your IAM user
   - Check **Allow key administrators to delete this key**
   - Click **Next**
   - **Key users:** select your IAM user
   - Click **Next** → **Finish**

6. Copy the KMS key ARN from the **General configuration** section.

7. Go back to the S3 bucket creation page, paste the ARN, and click **Create bucket**.

### Part 2: Create the CodePipeline

8. Navigate to **AWS CodePipeline** → **Create pipeline**.

9. Select **Create pipeline from template** → **Next**.

10. **Category:** **Continuous Integration** | **Template:** **CI Build Maven**

11. **Source provider:** **GitHub (via GitHub App)**
    - Create a new connection if needed
    - Install and authorize the GitHub App
    - Select your **MavenBuild** repository
    - **Branch:** `master`
    - **Output format:** CodePipeline default

12. In the **CICodeBuildSpec** section, enter:

    ```yaml
    version: 0.2
    phases:
      build:
        commands:
          - echo "Starting Maven build"
          - mvn -B package --file pom.xml
          - echo "Build completed successfully"
    artifacts:
      files:
        - target/*.war
      discard-paths: 'yes'
    ```

13. Click **Create pipeline from template**.

### Part 3: Configure Encrypted Artifacts

14. Navigate to **AWS CodeBuild** → select the build project created by the pipeline.

15. Click **Edit** under **Actions** tab.

16. In **Artifacts** section:
    - **Type:** Amazon S3
    - **Bucket:** your bucket from step 3
    - **Namespace type:** None
    - **Encryption key:** paste the KMS key ARN from step 6

17. Click **Update project**.

### Part 4: Test

18. Navigate back to the pipeline → **Release change** (or **Start pipeline**, depending on console wording) to run the pipeline.

19. Verify the build succeeds and artifacts appear in your S3 bucket (encrypted with KMS).

## Verification

- Pipeline executes successfully (green status).
- S3 bucket contains the build artifact (`.war` file).
- S3 object properties show SSE-KMS encryption.

## Cleanup

1. Delete the CodePipeline.
2. Delete the CodeBuild project.
3. Empty and delete the S3 bucket.
4. Schedule the KMS key for deletion (minimum 7-day waiting period).
5. Delete the GitHub connection.

## Troubleshooting

- If the build fails with **Access Denied**, ensure the CodeBuild role has permission to use the KMS key (and S3 on the artifact bucket); add the role as a **Key user** on the KMS key if needed.
- If GitHub connection fails, verify the GitHub App installation and authorization.
- Ensure the S3 bucket name is globally unique.

## Related docs

- [AWS CodePipeline Security](../docs/aws-security/aws-codepipeline-security.md)

## Lab file reference

[`devsecops/labs/pipelines/codepipeline-buildspec.yml`](../labs/pipelines/codepipeline-buildspec.yml)
