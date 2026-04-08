#!/usr/bin/env python3
"""
PASTA Threat Modeling Framework

Process for Attack Simulation and Threat Analysis (PASTA) is a
seven-stage, risk-centric threat modeling methodology.

Stages:
  1. Define Objectives
  2. Define Technical Scope
  3. Application Decomposition
  4. Threat Analysis
  5. Vulnerability Analysis
  6. Attack Simulation / Risk Analysis
  7. Risk & Impact Analysis + Countermeasures

Usage:
    python3 pasta_model.py
"""


class PASTA:
    """Implements the seven-stage PASTA threat modeling framework."""

    def __init__(self, system_info, objectives, threats, vulnerabilities,
                 impact, countermeasures):
        self.system_info = system_info
        self.objectives = objectives
        self.threats = threats
        self.vulnerabilities = vulnerabilities
        self.impact = impact
        self.countermeasures = countermeasures

    def stage_1_define_objectives(self):
        """Stage 1: Define business and security objectives."""
        print("=" * 60)
        print("  Stage 1 — Define Objectives")
        print("=" * 60)
        print(f"  System:     {self.system_info}")
        print(f"  Objectives: {self.objectives}\n")

    def stage_2_define_technical_scope(self):
        """Stage 2: Define the technical scope of the system."""
        print("=" * 60)
        print("  Stage 2 — Define Technical Scope")
        print("=" * 60)
        print(f"  System under analysis: {self.system_info}")
        print("  Components: Web server, database, API layer, auth module\n")

    def stage_3_application_decomposition(self):
        """Stage 3: Decompose the application into components."""
        print("=" * 60)
        print("  Stage 3 — Application Decomposition")
        print("=" * 60)
        print("  Trust boundaries, data flows, and entry points identified.")
        print("  Data Flow: User -> Web App -> API -> Database\n")

    def stage_4_threat_analysis(self):
        """Stage 4: Identify threats from the threat landscape."""
        print("=" * 60)
        print("  Stage 4 — Threat Analysis")
        print("=" * 60)
        print("  Identified Threats:")
        for threat in self.threats:
            print(f"    - {threat}")
        print()

    def stage_5_vulnerability_analysis(self):
        """Stage 5: Map vulnerabilities to threats."""
        print("=" * 60)
        print("  Stage 5 — Vulnerability Analysis")
        print("=" * 60)
        print("  Vulnerability Scores (1-10):")
        for vuln, score in self.vulnerabilities.items():
            print(f"    - {vuln}: {score}/10")
        print()

    def stage_6_attack_simulation(self):
        """Stage 6: Simulate attacks and calculate risk scores."""
        print("=" * 60)
        print("  Stage 6 — Attack Simulation & Risk Analysis")
        print("=" * 60)
        risk_scores = {}
        for threat in self.threats:
            impact_val = self.impact.get(threat, 0)
            vuln_val = self.vulnerabilities.get(threat, 0)
            risk = impact_val * vuln_val
            risk_scores[threat] = risk
            if risk >= 50:
                level = "CRITICAL"
            elif risk >= 30:
                level = "HIGH"
            elif risk >= 15:
                level = "MEDIUM"
            else:
                level = "LOW"
            print(
                f"    {threat}: impact({impact_val}) x vuln({vuln_val}) = "
                f"{risk} [{level}]"
            )

        total = sum(risk_scores.values())
        print(f"\n  Total Risk Score: {total}\n")
        return risk_scores

    def stage_7_countermeasures(self):
        """Stage 7: Recommend countermeasures and continuous monitoring."""
        print("=" * 60)
        print("  Stage 7 — Countermeasures & Monitoring")
        print("=" * 60)
        print("  Recommended Countermeasures:")
        for vuln in self.vulnerabilities:
            remedy = self.countermeasures.get(vuln, "No countermeasure available")
            print(f"    [{vuln}] -> {remedy}")
        print("\n  Continuous monitoring enabled for new threats.\n")

    def run_all_stages(self):
        """Execute all seven PASTA stages sequentially."""
        self.stage_1_define_objectives()
        self.stage_2_define_technical_scope()
        self.stage_3_application_decomposition()
        self.stage_4_threat_analysis()
        self.stage_5_vulnerability_analysis()
        self.stage_6_attack_simulation()
        self.stage_7_countermeasures()


def main():
    system_info = "E-Commerce Web Application"
    objectives = (
        "Ensure confidentiality, integrity, and availability of customer "
        "data and transactions."
    )

    threats = [
        "SQL Injection",
        "Cross-Site Scripting (XSS)",
        "Denial of Service (DoS)",
    ]

    vulnerabilities = {
        "SQL Injection": 8,
        "Cross-Site Scripting (XSS)": 6,
        "Denial of Service (DoS)": 7,
    }

    impact = {
        "SQL Injection": 9,
        "Cross-Site Scripting (XSS)": 5,
        "Denial of Service (DoS)": 7,
    }

    countermeasures = {
        "SQL Injection": "Use parameterized queries and ORM frameworks.",
        "Cross-Site Scripting (XSS)": (
            "Sanitize and validate all user input; use "
            "Content-Security-Policy headers."
        ),
        "Denial of Service (DoS)": (
            "Implement rate limiting, WAF rules, and DDoS protection "
            "(e.g., AWS Shield)."
        ),
    }

    print("PASTA Threat Modeling Framework\n")
    model = PASTA(
        system_info,
        objectives,
        threats,
        vulnerabilities,
        impact,
        countermeasures,
    )
    model.run_all_stages()


if __name__ == "__main__":
    main()
