# Lab 05: Penetration Testing with OWASP ZAP API Scan

**Difficulty:** Intermediate | **Time:** 25 minutes

## Prerequisites

- GitHub account

## Overview

Configure automated penetration testing using OWASP ZAP’s API scan action integrated into GitHub Actions. Unlike the baseline scan in Lab 04, the API scan performs deeper analysis including SQL injection detection and authentication checks.

**Important:** Only scan targets you own or have **explicit written permission** to test.

## Steps

1. Sign in to GitHub at [https://github.com/login](https://github.com/login).

2. Create a new repository with a README file.

3. Navigate to the **Actions** tab → **set up a workflow yourself**.

4. Create a workflow file (for example `.github/workflows/zap-api-scan.yml`) with this content:

   ```yaml
   name: OWASP ZAP API Scan

   on:
     push:
       branches: ["main"]
     pull_request:
       branches: ["main"]
     workflow_dispatch:

   permissions:
     issues: write

   jobs:
     zap_scan:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout Repository
           uses: actions/checkout@v4

         - name: ZAP API Scan
           uses: zaproxy/action-api-scan@v0.9.0
           with:
             target: 'https://your-target-url.example.com/'
             token: ${{ secrets.GITHUB_TOKEN }}
   ```

5. Replace the `target` URL with a site you have permission to test.

6. Commit the workflow.

7. Navigate to the **Actions** tab to monitor the workflow run.

8. Click the **`zap_scan`** job to view detailed steps.

9. Review the logs — look for SQL injection checks, authentication flaws, and security headers.

10. Click **Summary** → download the report artifact.

11. Open **`report_html.html`** to review the full ZAP report.

## Key differences from Lab 04 (baseline scan)

- API scan uses `zaproxy/action-api-scan@v0.9.0` instead of `zaproxy/action-baseline@v0.14.0`.
- API scan performs a full scan against APIs defined by OpenAPI/SOAP specs.
- Deeper security checks including SQL injection and authentication testing.
- Longer scan duration.

## Verification

- Confirm the workflow completes.
- A downloadable HTML report artifact is available from the run **Summary**.
- **`report_html.html`** opens in a browser and shows ZAP findings.

## Cleanup

- Delete the test repository if no longer needed, or remove the workflow under `.github/workflows/` if you want to keep the repo.

## Troubleshooting

- If the workflow fails with permissions errors, ensure `permissions: issues: write` is set.
- If ZAP times out, the target may be unreachable — verify the URL is accessible from the public internet (GitHub-hosted runners).
- For private targets, ensure the GitHub Actions runner can reach the URL (self-hosted runner, VPN, or allowlisted runner IPs may be required).

## Related docs

- [DevSecOps Pipeline Security](../docs/fundamentals/devsecops-pipeline.md)

## Lab file reference

[`devsecops/labs/pipelines/dast-zap-api-scan.yml`](../labs/pipelines/dast-zap-api-scan.yml)
