# STRIDE, DREAD, and PASTA

*Three complementary approaches for classifying threats, scoring risk, and running a risk-aligned threat modeling process.*

## Table of Contents

1. [How These Frameworks Fit Together](#how-these-frameworks-fit-together)
2. [STRIDE](#stride)
3. [DREAD](#dread)
4. [PASTA](#pasta)
5. [Comparison: STRIDE vs DREAD vs PASTA](#comparison-stride-vs-dread-vs-pasta)
6. [Hands-On Labs](#hands-on-labs)

---

## How These Frameworks Fit Together

- **STRIDE** answers: *What kinds of threats should we consider?* (a **classification** aid)
- **DREAD** answers: *Which threats matter most right now?* (a **prioritization** aid)
- **PASTA** answers: *How do we run threat modeling as a process aligned with business risk?* (a **methodology**)

Teams often combine them—for example, STRIDE to brainstorm, DREAD to score, and PASTA stages to structure workshops and documentation.

---

## STRIDE

**STRIDE** is a mnemonic for six **categories** of threats, originally associated with Microsoft’s threat modeling approach. It helps teams systematically walk through an architecture (especially across **trust boundaries**) and ask, “Could this happen here?”

### The six categories

| Category | Meaning (conceptual) | Example question |
|----------|----------------------|------------------|
| **S** – Spoofing | Pretending to be someone or something else | Can an attacker forge tokens, sessions, or service identities? |
| **T** – Tampering | Modifying data or code | Can requests, files, or configs be altered in transit or at rest? |
| **R** – Repudiation | Denying an action without proof | Can a user dispute a transaction; do we lack tamper-evident logs? |
| **I** – Information disclosure | Exposing data to unauthorized parties | Do errors, logs, or APIs leak secrets or PII? |
| **D** – Denial of service | Making the system unavailable or degraded | Can one caller exhaust threads, storage, or CPU? |
| **E** – Elevation of privilege | Gaining unauthorized capabilities | Can a user become admin, or a service exceed its role? |

### Key components in practice

- **Diagrams**: Data flow diagrams (DFD) with **trust boundaries** (browser, API gateway, app tier, database).
- **Per-element analysis**: For each component or flow, consider which STRIDE categories apply.
- **Mapping to controls**: Authentication against spoofing, integrity checks against tampering, logging against repudiation, encryption and minimization against disclosure, rate limits and scaling against DoS, authorization and sandboxing against elevation.

### E-commerce example (concise)

An **online storefront** with a web app, cart service, payment integration, and order database:

| STRIDE | Illustrative threat |
|--------|---------------------|
| Spoofing | Attacker reuses or forges session cookies to check out as another user. |
| Tampering | Modified cart prices sent to the payment API if server-side validation is missing. |
| Repudiation | Customer claims they did not place an order; weak audit trail for payment consent. |
| Information disclosure | Order API returns full payment details to the browser unnecessarily. |
| Denial of service | Bot traffic exhausts inventory reservation or checkout endpoints. |
| Elevation of privilege | Regular user accesses merchant admin APIs due to broken access control. |

---

## DREAD

**DREAD** is a **risk scoring** model used to **prioritize** threats after they are identified (often alongside STRIDE or other lists). Each factor is typically scored **1–10** (higher = worse for that dimension). Exact calibration varies by organization; consistency matters more than the specific numbers.

### The five categories

| Letter | Factor | What it captures |
|--------|--------|------------------|
| **D** | **Damage** | How bad would exploitation be? (data loss, financial impact, reputation) |
| **R** | **Reproducibility** | How easy is it to trigger reliably? |
| **E** | **Exploitability** | How much skill, access, or effort does an attacker need? |
| **A** | **Affected users** | How many users—or how critical a population—could be impacted? |
| **D** | **Discoverability** | How easy is the weakness to find? (Some teams de-emphasize this factor today, arguing attackers will find issues anyway.) |

### Scoring (typical pattern)

Scores are often **averaged** or **summed** into a total for ranking. Teams define rubrics so that “7” means the same thing across reviewers.

**Example rubric fragment (illustrative, not prescriptive):**

| Score | Damage | Exploitability |
|-------|--------|----------------|
| 1–3 | Limited impact | Requires insider access or rare conditions |
| 4–7 | Significant for subset of users | Known techniques, moderate effort |
| 8–10 | Severe org-wide or regulatory | Trivial to exploit at scale |

### E-commerce example

**Threat**: Broken access control on the **order history** API exposes other customers’ orders.

| Factor | Example rationale | Example score |
|--------|-------------------|---------------|
| Damage | PII + purchase history; regulatory and trust impact | High (e.g., 8–9) |
| Reproducibility | Simple HTTP parameter manipulation | High |
| Exploitability | No special tools required | High |
| Affected users | Potentially all customers | High |
| Discoverability | Might be found via inspection or fuzzing | Medium–high |

Such a threat would typically rank **above** a niche admin-only bug with narrow impact—guiding remediation order.

---

## PASTA

**PASTA** (Process for Attack Simulation and Threat Analysis) is a **seven-stage**, **risk-centered** methodology. It links **business** objectives and **technical** reality so security work traces back to what the organization actually cares about.

### The seven stages (overview)

| Stage | Focus |
|-------|--------|
| **1** | Define **objectives**—business context, crown jewels, success criteria. |
| **2** | Define **technical scope**—components, data flows, dependencies. |
| **3** | **Decompose** the application (diagrams, use cases, trust boundaries). |
| **4** | **Threat analysis**—identify realistic threats (often threat libraries, STRIDE, intel). |
| **5** | **Weakness and vulnerability** analysis—map threats to flaws and exposure. |
| **6** | **Attack modeling**—describe attack paths and feasibility (“kill chain” thinking). |
| **7** | **Risk and impact** analysis—countermeasures, residual risk, decisions. |

PASTA emphasizes **correlation** between business impact and attacker behavior, making it a strong fit for regulated or high-stakes environments.

### Banking example (concise)

**Stage 1–2**: Objective—protect **customer funds** and **regulatory compliance**; scope includes mobile app, API layer, fraud service, and ledger integration.

**Stage 3**: Decompose login, high-value transfers, and account recovery flows; mark trust boundaries (device, API gateway, internal services).

**Stage 4–5**: Threats include **credential stuffing**, **ATO** (account takeover), **wire fraud** via API abuse; weaknesses might include weak rate limits, missing device fingerprint signals, or excessive **service account** permissions on the ledger.

**Stage 6**: Model an attack path: stolen credentials → session fixation or weak MFA → transfer API called with scripted beneficiaries.

**Stage 7**: Prioritize **MFA**, **step-up** for new payees, **behavioral analytics**, and **least-privilege** IAM; document accepted risks and monitoring.

---

## Comparison: STRIDE vs DREAD vs PASTA

| Aspect | STRIDE | DREAD | PASTA |
|--------|--------|-------|-------|
| **Primary purpose** | Threat **taxonomy** (what types?) | Threat **prioritization** (how urgent?) | End-to-end **process** (how to run modeling?) |
| **Output** | Categorized threat list | Scores / ranked backlog | Staged analysis tied to business risk |
| **Best when** | Brainstorming from diagrams | Many findings need ordering | Executive alignment, regulated systems |
| **Depth** | Single-layer categories | Five scoring dimensions | Seven stages, attack simulation lens |
| **Typical use with others** | Feeds into DREAD scoring | Applied after STRIDE or PASTA threat ID | Can embed STRIDE/DREAD inside stages |

STRIDE and DREAD are **building blocks**. PASTA is a **container** that organizes when and how those building blocks (and other inputs) are applied.

---

## Hands-On Labs

Practice structured scoring and methodology:

- [Lab 01: DREAD Model](../labmanuals/lab01-threat-dread-model.md)
- [Lab 02: PASTA Model](../labmanuals/lab02-threat-pasta-model.md)

---

*Last updated: March 2026*
