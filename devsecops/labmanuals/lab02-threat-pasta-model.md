# Lab 02: Implementing the PASTA Threat Modeling Framework

**Difficulty:** Beginner  
**Estimated time:** 15 minutes  

**Source material:** `Lesson_01/02_Implementing_PASTA_Model.docx`

## Prerequisites

- An AWS account with permission to open **AWS CloudShell**.
- Completion of [Lab 01: Implementing the DREAD Risk Assessment Model](./lab01-threat-dread-model.md) is helpful but not required.

## Learning objectives

By the end of this lab, you will be able to:

- Name the **seven stages** of **PASTA** (Process for Attack Simulation and Threat Analysis).
- Walk through each stage in a structured checklist driven by a script.
- Record stage outputs in a repeatable way for documentation or review.

## Overview

**PASTA** is a risk-centric threat modeling methodology that progresses from business context through technical analysis to attack simulation and countermeasures. This lab uses a short **Python** script in **AWS CloudShell** to guide you through all **seven stages** with prompts and placeholders—mirroring a workshop-style workflow without requiring specialized tooling.

## Steps

1. **Open AWS CloudShell** (same as Lab 01: console → **CloudShell**).

2. **Verify Python 3**

   ```bash
   python3 --version
   ```

3. **Create a working directory**

   ```bash
   mkdir -p ~/devsecops-labs && cd ~/devsecops-labs
   ```

4. **Create `pasta_model.py`**
   - **Preferred:** Copy from `devsecops/labs/scripts/pasta_model.py` in your course repository.
   - **Otherwise:** Create the file with the reference implementation below.

   ```bash
   nano pasta_model.py
   ```

   ```python
   #!/usr/bin/env python3
   """Guided walkthrough of the seven PASTA stages (inputs captured as text)."""

   STAGES = [
       "Stage 1 — Define objectives & business risk: What are we protecting? Why does it matter?",
       "Stage 2 — Define technical scope: Systems, data flows, trust boundaries, dependencies.",
       "Stage 3 — Decompose the application: Components, entry points, authentication/authorization.",
       "Stage 4 — Threat analysis: STRIDE-style or similar enumeration tied to components.",
       "Stage 5 — Vulnerability & weakness analysis: Known flaws, misconfigurations, gaps.",
       "Stage 6 — Attack modeling: Likely paths, preconditions, attacker goals.",
       "Stage 7 — Risk & impact analysis: Likelihood, impact, controls, residual risk.",
   ]


   def main() -> None:
       print("PASTA — seven-stage guided capture\n")
       print("For each stage, enter a short note for your scenario (or 'skip').\n")
       notes = []
       for title in STAGES:
           print(f"--- {title} ---")
           line = input("Your notes: ").strip()
           notes.append((title, line))
       print("\n========== Summary ==========")
       for title, line in notes:
           print(f"\n{title}\n  -> {line or '(no notes)'}")
       print("\nExport this summary to your threat model doc or ticket system.")


   if __name__ == "__main__":
       main()
   ```

5. **Run the script**

   ```bash
   python3 pasta_model.py
   ```

6. **Complete all seven stages**
   - For each prompt, type a short realistic note for a sample system (for example, an internal API that handles customer profile updates).
   - Use **skip** for any stage you want to leave blank.

7. **Review the printed summary**
   - Confirm all seven stages appear.
   - Copy the summary from the terminal into a document if your instructor requires submission.

## Verification

| Check | Expected result |
|--------|------------------|
| Script start | Seven section headers appear one after another |
| After last stage | A **Summary** block lists all stages and your notes |
| Empty line at a prompt | Summary shows `(no notes)` for that stage |

## Troubleshooting

- **Accidentally closed CloudShell** — Files under `~/devsecops-labs` persist in your CloudShell home until you delete them; reopen CloudShell and `cd ~/devsecops-labs`.
- **Keyboard interrupt (`Ctrl+C`)** — Run `python3 pasta_model.py` again from the start.
- **Repo script differs** — Use the repository’s `pasta_model.py` if your course defines different stage text or scoring.

## Cleanup

```bash
cd ~
rm -rf ~/devsecops-labs
```

## Summary

You ran a **seven-stage PASTA** walkthrough in **AWS CloudShell**, capturing business context through risk and impact in a single repeatable session—building muscle memory for how **PASTA** structures threat analysis end to end.

## Related resources

- [Threat Modeling Techniques](../docs/fundamentals/stride-dread-pasta.md)
