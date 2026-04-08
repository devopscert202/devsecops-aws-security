# Lab 01: Implementing the DREAD Risk Assessment Model

**Difficulty:** Beginner  
**Estimated time:** 15 minutes  

**Source material:** `Lesson_01/01_Implementing_DREAD_Model.docx`

## Prerequisites

- An AWS account with permission to open **AWS CloudShell** in your chosen Region.
- Basic familiarity with a terminal (copy, paste, run commands).

## Learning objectives

By the end of this lab, you will be able to:

- Explain what each letter in **DREAD** represents in risk scoring.
- Run a small Python program that computes a DREAD-style risk score from numeric inputs.
- Interpret high versus low aggregate scores and relate them to prioritization.

## Overview

**DREAD** is a simple, qualitative-to-quantitative model used to compare threats by scoring five factors (commonly **Damage**, **Reproducibility**, **Exploitability**, **Affected users**, and **Discoverability**) on a scale such as 1–10, then averaging them. In this lab you run an interactive Python script in **AWS CloudShell** so you can practice entering ratings and reading the resulting risk level—without installing anything on your local machine.

## Steps

1. **Open AWS CloudShell**
   - Sign in to the [AWS Management Console](https://console.aws.amazon.com/).
   - Choose the **Region** you want to use (CloudShell is available in most Regions).
   - Click the **CloudShell** icon in the top toolbar (terminal prompt appears at the bottom of the console).

2. **Verify Python 3 is available**

   ```bash
   python3 --version
   ```

   You should see a version such as `Python 3.9.x` or newer. CloudShell includes Python 3 by default.

3. **Create a working directory and change into it**

   ```bash
   mkdir -p ~/devsecops-labs && cd ~/devsecops-labs
   ```

4. **Create `dread_model.py`**
   - **Preferred:** If your course repository includes the script, copy it from  
     `devsecops/labs/scripts/dread_model.py` into CloudShell (for example, paste the file contents or clone the repo and copy the file).
   - **Otherwise:** Create the file in CloudShell and paste the reference implementation below.

   ```bash
   nano dread_model.py
   ```

   Paste the following (or use the repository copy if it matches):

   ```python
   #!/usr/bin/env python3
   """Interactive DREAD-style risk score (1-10 per factor, equal-weight average)."""

   FACTORS = [
       ("Damage — how bad if it happens?", "D"),
       ("Reproducibility — how easy to repeat?", "R"),
       ("Exploitability — effort to exploit?", "E"),
       ("Affected users — how many impacted?", "A"),
       ("Discoverability — how easy to find?", "D"),
   ]


   def read_score(prompt: str) -> float:
       while True:
           raw = input(f"{prompt} [1-10]: ").strip()
           try:
               v = float(raw)
           except ValueError:
               print("  Enter a number between 1 and 10.")
               continue
           if 1 <= v <= 10:
               return v
           print("  Value must be between 1 and 10.")


   def main() -> None:
       print("DREAD-style risk calculator (equal-weight average of five 1-10 scores)\n")
       scores = []
       for label, _abbr in FACTORS:
           scores.append(read_score(label))
       average = sum(scores) / len(scores)
       print(f"\nAverage score: {average:.2f} / 10")
       if average >= 8:
           level = "High"
       elif average >= 5:
           level = "Medium"
       else:
           level = "Low"
       print(f"Risk level (illustrative): {level}")
       print("\nTip: tune thresholds to match your org’s risk rubric.")


   if __name__ == "__main__":
       main()
   ```

   Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X` in nano).

5. **Run the script**

   ```bash
   chmod +x dread_model.py
   python3 dread_model.py
   ```

6. **Enter sample ratings and analyze the output**
   - When prompted, enter five numbers between **1** and **10**.
   - Example set (high overall): `8`, `7`, `9`, `6`, `5` → average **7.0** (illustrative **Medium** band with the default thresholds).
   - Confirm the printed **average** and **risk level** match your expectations.

7. **Experiment with scenarios**
   - **Low-risk example:** use mostly `2`–`4` (e.g. `2, 3, 2, 3, 3`) and note the lower average.
   - **High-risk example:** use mostly `9`–`10` and note the higher average.
   - Reflect: which single factor, if raised from 3 to 9, changes prioritization most for your scenario?

## Verification

| Check | Expected result |
|--------|------------------|
| `python3 --version` | Prints Python 3.x |
| Run `python3 dread_model.py` | Five prompts, then average and risk level |
| Invalid input (e.g. `11` or `abc`) | Script rejects and re-prompts |
| Low vs high inputs | Average and band change accordingly |

## Troubleshooting

- **`python3: command not found`** — Rare in CloudShell; refresh CloudShell or switch Region; contact your admin if organizational policy disables CloudShell.
- **`Permission denied`** — Run with `python3 dread_model.py` (no execute bit needed) or `chmod +x dread_model.py`.
- **Wrong file / empty file** — Confirm you are in `~/devsecops-labs` and `ls -la dread_model.py` shows a non-zero size.
- **Script differs from course repo** — Align with `devsecops/labs/scripts/dread_model.py` if your instructor provided a canonical version.

## Cleanup

```bash
cd ~
rm -rf ~/devsecops-labs
```

This removes the practice directory and `dread_model.py` from your CloudShell home. It does not delete anything in AWS beyond local CloudShell files.

## Summary

You used **AWS CloudShell** to run an interactive **Python 3** script that scores a threat across five **DREAD** dimensions, averages them, and maps the result to an illustrative **Low / Medium / High** band—giving you hands-on practice with numeric risk comparison.

## Related resources

- [Threat Modeling Techniques](../docs/fundamentals/stride-dread-pasta.md) — STRIDE, DREAD, and PASTA in context (create or open this doc in your repo if the link 404s locally).
