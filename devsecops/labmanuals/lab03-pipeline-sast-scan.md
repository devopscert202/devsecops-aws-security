# Lab 03: Running a SAST Scan with Semgrep and GitHub Actions

**Difficulty:** Intermediate  
**Estimated time:** 30 minutes  

**Source material:** `Lesson_01/03_Running_SAST_Scan_on_a_Static_Web_Application_Using_GitHub.docx`

## Prerequisites

- A **GitHub** account.
- Permission to enable **GitHub Actions** and add **secrets** on a repository you control.
- A **fork** of a Java/Maven project (steps below use a public sample repo).

> **Security:** Store the Semgrep token only as a **GitHub Actions secret**. Never commit tokens, API keys, or `.env` files containing secrets to the repository.

## Learning objectives

By the end of this lab, you will be able to:

- Add a **Maven** CI workflow to a GitHub repository.
- Connect **Semgrep** to GitHub via the official app and a **SEMGREP_APP_TOKEN** secret.
- Run **`semgrep ci`** in Actions and review findings in the Semgrep cloud UI.

## Overview

**Static Application Security Testing (SAST)** analyzes source code for vulnerability patterns. **Semgrep** is a popular engine that integrates cleanly with **GitHub Actions**. In this lab you fork a sample **Java** project, enable a **Maven** build workflow, then add a second job that runs **`semgrep ci`** inside the **`semgrep/semgrep`** container, authenticated to Semgrep Cloud with **`SEMGREP_APP_TOKEN`**.

## Steps

1. **Fork the sample repository**
   - Open [https://github.com/GithubWorkstation/JavaProject](https://github.com/GithubWorkstation/JavaProject).
   - Click **Fork** → choose your account (or org) → create the fork.

2. **Add a Maven workflow (if you do not already have one)**
   - In your fork, open the **Actions** tab.
   - If prompted to enable workflows, approve for this fork.
   - Click **New workflow** → search for **Java with Maven** (or **Maven**).
   - Use GitHub’s template **“Java with Maven”** and commit it to `.github/workflows/maven.yml` on the default branch (often `main`).

3. **Register at Semgrep and sign in with GitHub**
   - Go to [https://semgrep.dev/](https://semgrep.dev/) and create an account (sign in with GitHub is typical).

4. **Install the Semgrep GitHub App**
   - From Semgrep’s documentation or deployment UI, install the **GitHub App** for the organization or user that owns your fork.
   - Grant access to the **forked** repository (or all repositories, per your org policy).

5. **Create a Semgrep API token**
   - In Semgrep: **Settings** → **Tokens** (or **API tokens** per current UI) → **Create new token**.
   - Copy the token once; you will not be able to see it again.

6. **Add the token as a repository secret**
   - On GitHub: your fork → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
   - Name: **`SEMGREP_APP_TOKEN`** (exact spelling).
   - Value: paste the token → **Add secret**.

7. **Add the Semgrep job to your workflow**
   - Open `.github/workflows/maven.yml` (or merge into your existing CI file).
   - Incorporate the Semgrep job from your course file:  
     `devsecops/labs/pipelines/sast-semgrep-workflow.yml`  
     (copy the `semgrep` job and top-level keys such as `permissions` if shown there).

   **Reference workflow** (adjust `branches` and job `needs:` if your Maven job has a different `job_id`; this example keeps **build** and **semgrep** independent):

   ```yaml
   name: Java CI with Semgrep

   on:
     push:
       branches: ["main"]
     pull_request:
       branches: ["main"]
     workflow_dispatch:

   permissions:
     contents: read

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - name: Set up JDK 17
           uses: actions/setup-java@v4
           with:
             java-version: "17"
             distribution: "temurin"
             cache: maven
         - name: Build with Maven
           run: mvn -B package --file pom.xml

     semgrep:
       name: semgrep/ci
       runs-on: ubuntu-latest
       container:
         image: semgrep/semgrep
       if: github.actor != 'dependabot[bot]'
       steps:
         - uses: actions/checkout@v4
         - run: semgrep ci
           env:
             SEMGREP_APP_TOKEN: ${{ secrets.SEMGREP_APP_TOKEN }}
   ```

   > Do **not** inline the token in YAML. Always use `${{ secrets.SEMGREP_APP_TOKEN }}`.

8. **Commit and push**

   ```bash
   git add .github/workflows/maven.yml
   git commit -m "ci: add Semgrep scan job"
   git push
   ```

9. **Verify the workflow run**
   - **Actions** tab → select the latest workflow run.
   - Confirm both **build** and **semgrep** jobs complete (green) or review logs if either fails.

10. **Review findings in Semgrep**
    - Open the Semgrep Cloud dashboard for your deployment.
    - Locate the project/repository scan results and drill into any findings.

## Verification

| Check | Expected result |
|--------|------------------|
| Secrets | `SEMGREP_APP_TOKEN` exists under **Actions** secrets |
| Workflow file | Valid YAML under `.github/workflows/` |
| Actions run | `semgrep` job runs `semgrep ci` and finishes |
| Semgrep UI | New scan / findings associated with your repo |

## Troubleshooting

- **`SEMGREP_APP_TOKEN` not found** — Secret name must match exactly; fork must be the repo where you added the secret.
- **Semgrep job cannot clone** — Ensure `permissions: contents: read` (or equivalent) for `GITHUB_TOKEN`.
- **No findings** — Normal for small samples; try Semgrep rulesets or custom rules in the Semgrep app configuration.
- **App not installed on fork** — Re-check GitHub App installation includes this repository.
- **Do not set `SEMGREP_RULES` in the same job** as `SEMGREP_APP_TOKEN` when using Semgrep Cloud in certain modes—follow [Semgrep CI environment variables](https://semgrep.dev/docs/semgrep-ci/ci-environment-variables) if you customize.

## Cleanup

- **Optional — disable workflow:** `.github/workflows/maven.yml` → **Delete file** or disable Actions in **Settings** → **Actions** → **General**.
- **Optional — remove secret:** Settings → **Secrets** → remove `SEMGREP_APP_TOKEN`.
- **Optional — revoke token** in Semgrep and **uninstall** the GitHub App from repos you no longer want scanned.

## Summary

You configured **GitHub Actions** to build a **Maven** project and run **Semgrep** in CI using the official **`semgrep/semgrep`** image and a **`SEMGREP_APP_TOKEN`** repository secret—demonstrating **SAST** in the pipeline without hardcoding credentials.

## Related resources

- [SAST, DAST & SCA](../docs/fundamentals/sast-dast-sca.md)
- [Semgrep sample CI configs](https://semgrep.dev/docs/semgrep-ci/sample-ci-configs)
- [Semgrep tokens](https://semgrep.dev/docs/deployment/tokens)
