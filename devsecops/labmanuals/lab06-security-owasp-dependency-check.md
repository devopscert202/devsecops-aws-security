# Lab 06: Securing a Node.js Application with OWASP Dependency-Check

**Difficulty:** Intermediate | **Time:** 30 minutes

## Prerequisites

- Ubuntu lab environment or EC2 instance with internet access

## Overview

Clone a Node.js application, audit its npm dependencies for known vulnerabilities, and run OWASP Dependency-Check to generate a comprehensive CVE report.

## Steps

1. Clone the test repository:

   ```bash
   git clone https://github.com/anujdevopslearn/SonarQubeNodeJS.git
   cd SonarQubeNodeJS/
   ```

2. Install Node Version Manager (NVM):

   ```bash
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
   source ~/.bashrc
   ```

3. Install Node.js 20:

   ```bash
   nvm install 20
   ```

4. Verify installations:

   ```bash
   node -v    # Should show v20.x.x
   npm -v     # Should show 10.x.x
   ```

5. Install project dependencies:

   ```bash
   npm install
   ```

6. Run npm audit to identify vulnerabilities:

   ```bash
   npm audit
   ```

   **Note:** You’ll see a list of vulnerabilities with severity levels (low, moderate, high, critical).

7. Attempt automatic fixes:

   ```bash
   npm audit fix
   ```

   **Note:** Not all vulnerabilities can be auto-fixed. Some require manual dependency updates. Review the remaining issues carefully — newer versions may introduce breaking changes.

8. Download OWASP Dependency-Check:

   ```bash
   wget https://github.com/jeremylong/DependencyCheck/releases/download/v11.1.0/dependency-check-11.1.0-release.zip
   ```

9. Extract:

   ```bash
   unzip dependency-check-11.1.0-release.zip
   ```

10. Run the dependency check scan:

    ```bash
    ./dependency-check/bin/dependency-check.sh \
      --project "NodeJS App" \
      --scan . \
      --out dependency-check-report \
      --format HTML
    ```

    **Note:** The first run downloads the NVD database and may take several minutes.

11. Open the report:

    ```bash
    # If on a desktop environment:
    xdg-open dependency-check-report/dependency-check-report.html

    # Or copy to Desktop:
    cp dependency-check-report/dependency-check-report.html ~/Desktop/
    ```

12. Review the report: check CVE IDs, CVSS scores, affected libraries, and recommended fixes.

## Verification

- `npm audit` produces a vulnerability summary.
- The `dependency-check-report/` directory contains `dependency-check-report.html`.
- The HTML report lists identified CVEs with severity ratings.

## Cleanup

```bash
cd ~
rm -rf SonarQubeNodeJS/
```

Optionally remove `dependency-check-11.1.0-release.zip` and the extracted `dependency-check` directory if you no longer need them.

## Troubleshooting

- If `nvm` command not found after install, run `source ~/.bashrc` or open a new terminal.
- If dependency-check takes very long, it’s downloading the NVD database — be patient on first run.
- If `wget` fails, check your internet connection or use `curl` instead:

  ```bash
  curl -L -O https://github.com/jeremylong/DependencyCheck/releases/download/v11.1.0/dependency-check-11.1.0-release.zip
  ```

## Related docs

- [Security Principles](../docs/aws-security/security-principles.md)
- [SAST, DAST & SCA](../docs/fundamentals/sast-dast-sca.md)
