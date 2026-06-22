from faker import Faker
import json

# Generate sample security log
fake = Faker()

log = """
15 failed login attempts from IP 192.168.1.45.
Unknown executable detected.
Suspicious network activity observed.
"""

# Convert technical indicators into human-readable explanations
def explain_log(log_text):

    explanations = []

    if "failed login" in log_text.lower():
        explanations.append(
            "Repeated failed login attempts were detected."
        )

    if "unknown executable" in log_text.lower():
        explanations.append(
            "An unknown executable file was found."
        )

    if "network" in log_text.lower():
        explanations.append(
            "Unusual network activity was observed."
        )

    return explanations

# Structured JSON output for frontend integration
output = {
    "alert_1": {
        "recommendation": "Quarantine Device",
        "confidence": "High",
        "reasons": explain_log(log),
        "data_sources": [
            "Security Logs",
            "Device Telemetry"
        ],
        "limitations": [
            "Possible false positive"
        ]
    },

    "alert_2": {
        "recommendation": "Block IP Address",
        "confidence": "High",
        "reasons": [
            "Suspicious traffic detected",
            "Multiple connection attempts"
        ],
        "data_sources": [
            "Firewall Logs",
            "Network Monitor"
        ],
        "limitations": [
            "Shared IP may affect legitimate users"
        ]
    },
