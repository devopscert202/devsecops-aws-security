#!/usr/bin/env python3
"""
DREAD Risk Assessment Model

The DREAD model evaluates security threats across five dimensions:
- Damage Potential: How severe is the damage if exploited?
- Reproducibility: How easy is it to reproduce the attack?
- Exploitability: How easy is it to launch the attack?
- Affected Users: How many users are impacted?
- Discoverability: How easy is it to discover the vulnerability?

Each dimension is rated 1 (low risk) to 10 (high risk).
Total score ranges from 5 (minimal) to 50 (critical).

Usage:
    python3 dread_model.py
"""


class DREADRiskModel:
    """Implements the DREAD threat risk assessment framework."""

    RISK_LEVELS = {
        (5, 15): "LOW",
        (16, 30): "MEDIUM",
        (31, 40): "HIGH",
        (41, 50): "CRITICAL",
    }

    def __init__(self, damage_potential, reproducibility, exploitability,
                 affected_users, discoverability):
        params = {
            "Damage Potential": damage_potential,
            "Reproducibility": reproducibility,
            "Exploitability": exploitability,
            "Affected Users": affected_users,
            "Discoverability": discoverability,
        }
        for name, value in params.items():
            if not isinstance(value, int) or not 1 <= value <= 10:
                raise ValueError(f"{name} must be an integer between 1 and 10, got {value}")

        self.damage_potential = damage_potential
        self.reproducibility = reproducibility
        self.exploitability = exploitability
        self.affected_users = affected_users
        self.discoverability = discoverability

    def calculate_risk(self):
        """Return the total DREAD risk score (5-50)."""
        return (self.damage_potential + self.reproducibility +
                self.exploitability + self.affected_users +
                self.discoverability)

    def risk_level(self):
        """Classify the risk score into LOW / MEDIUM / HIGH / CRITICAL."""
        score = self.calculate_risk()
        for (low, high), level in self.RISK_LEVELS.items():
            if low <= score <= high:
                return level
        return "UNKNOWN"

    def print_risk_assessment(self):
        """Print a formatted risk assessment report."""
        score = self.calculate_risk()
        level = self.risk_level()
        print("\n" + "=" * 50)
        print("       DREAD Risk Model Assessment")
        print("=" * 50)
        print(f"  Damage Potential:  {self.damage_potential}/10")
        print(f"  Reproducibility:   {self.reproducibility}/10")
        print(f"  Exploitability:    {self.exploitability}/10")
        print(f"  Affected Users:    {self.affected_users}/10")
        print(f"  Discoverability:   {self.discoverability}/10")
        print("-" * 50)
        print(f"  Total Risk Score:  {score}/50")
        print(f"  Risk Level:        {level}")
        print("=" * 50)


def get_input():
    """Prompt the user for DREAD parameter ratings."""
    print("Rate each parameter from 1 (low risk) to 10 (high risk):\n")
    fields = [
        ("Damage Potential", "How severe is the damage if exploited?"),
        ("Reproducibility", "How easy is it to reproduce the attack?"),
        ("Exploitability", "How easy is it to launch the attack?"),
        ("Affected Users", "How many users are impacted?"),
        ("Discoverability", "How easy is it to discover the vulnerability?"),
    ]
    values = []
    for name, hint in fields:
        while True:
            try:
                val = int(input(f"  {name} ({hint}): "))
                if 1 <= val <= 10:
                    values.append(val)
                    break
                print("    Please enter a number between 1 and 10.")
            except ValueError:
                print("    Invalid input. Enter an integer.")
    return tuple(values)


def main():
    print("Welcome to the DREAD Risk Assessment Model\n")
    damage, repro, exploit, affected, discover = get_input()
    model = DREADRiskModel(damage, repro, exploit, affected, discover)
    model.print_risk_assessment()


if __name__ == "__main__":
    main()
