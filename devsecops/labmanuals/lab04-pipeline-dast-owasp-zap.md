# Lab 04: Performing a DAST Scan with OWASP ZAP and GitHub Actions

**Difficulty:** Intermediate  
**Estimated time:** 25 minutes  

**Source material:** `Lesson_01/04_Performing_DAST_Scan_on_a_Running_Web_Application_with_OWASP_Zap.docx`

## Prerequisites

- A **GitHub** account.
- A **target URL** you are **explicitly allowed** to scan (your own app, a dedicated test instance, or a documented safe demo target). **Do not** point ZAP at systems you do not own or lack written permission to test.

## Learning objectives

By the end of this lab, you will be able to:

- Run **OWASP ZAP Baseline** from **GitHub Actions** against a web target.
- Interpret a **ZAP HTML report** (alerts, risk levels).
- Understand why baseline scans are suited to **quick CI checks** versus full audits.

## Overview

**Dynamic Application Security Testing (DAST)** exercises a running application. **OWASP ZAP** can run a **baseline** scan that spiders a site briefly and reports passive issues. The official **`zaproxy/action-baseline`** Action wraps this for CI. By default the baseline run is **short** (on the order of **one minute**), which makes it practical for pipelines but **not** a substitute for a full penetration test.

## Steps

1. **Create a new GitHub repository**
   - On GitHub: **New repository** → name it (for example `zap-baseline-lab`) → add a **README** → **Create repository**.

2. **Open the Actions tab**
   - **Actions** → **set up a workflow yourself** → **Configure** (starts an empty workflow editor).

3. **Add the ZAP Baseline workflow**
   - Use the course file **`devsecops/labs/pipelines/dast-zap-baseline.yml`** as the source of truth, or create `.github/workflows/zap-baseline.yml` with the following validated example (update **`target`**):

   ```yaml
   name: ZAP Baseline Scan

   on:
     push:
       branches: [main]
     workflow_dispatch:

   jobs:
     zap-baseline:
       runs-on: ubuntu-latest
       name: OWASP ZAP Baseline
       steps:
         - name: ZAP Baseline Scan
           uses: zaproxy/action-baseline@v0.14.0
           with:
             target: "https://example.com"
             allow_issue_writing: false
   ```

4. **Replace the target URL**
   - Change `target` to a URL you have **permission** to scan (HTTPS recommended).
   - Commit the workflow to **`main`**.

5. **Commit the workflow**
   - **Start commit** → commit to `main`.

6. **Monitor the Actions run**
   - **Actions** → open **ZAP Baseline Scan** → select the latest run → open the job log.

7. **Download the HTML report artifact**
   - After a successful run, open the **Artifacts** section on the run summary page (when the action uploads `report_html.html`; if your action version bundles artifacts differently, use the **Upload artifact** step pattern from your course pipeline file).
   - Download **`report_html.html`** (or the artifact name shown in the run).

8. **Review findings**
   - Open the HTML report in a browser.
   - Note **alert** names, **risk** levels, and remediation hints.

> **Note:** ZAP **Baseline** runs a **limited** passive/quick check by design—suitable for **CI/CD** smoke-style **DAST**, not exhaustive coverage.

## Verification

| Check | Expected result |
|--------|------------------|
| Workflow file | Exists at `.github/workflows/*.yml` |
| Run completes | Job finishes (warnings may still appear in report) |
| Report | HTML opens locally; lists alerts and severities |
| Target | Only URLs you are authorized to scan |

## Troubleshooting

- **`403` / blocked scan** — Target may block automated clients; try a simpler public test app you control or adjust allowlists with site owner approval.
- **No artifact** — Add an explicit upload step if your template does not attach reports:

  ```yaml
  - name: Upload ZAP report
    if: always()
    uses: actions/upload-artifact@v4
    with:
      name: zap-baseline-report
      path: report_html.html
  ```

  (Exact path depends on the action version; check the action’s README for the report filename.)

- **Too many findings on demo sites** — Baseline is noisy on large public sites; prefer small apps you own.
- **Fail on findings** — Some configurations fail the build when high-risk alerts exist; read logs for `exit code` behavior.

## Cleanup

- Delete the test repository **or** remove `.github/workflows/zap-baseline.yml` and disable Actions if no longer needed.
- Revoke any tokens if you added authentication (not required for this baseline lab).

## Summary

You configured **GitHub Actions** to run an **OWASP ZAP Baseline** scan against an authorized URL, retrieved an **HTML** report, and reviewed **DAST** findings suitable for **short** CI feedback loops.

## Related resources

- [SAST, DAST & SCA](../docs/fundamentals/sast-dast-sca.md)
- [zaproxy/action-baseline](https://github.com/zaproxy/action-baseline)
