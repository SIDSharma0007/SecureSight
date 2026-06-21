# 🛡️ SecureSight AI: Transparent Agent Data Pipeline

## 📖 Overview
This repository contains the data simulation layer for **SecureSight AI**, a prototype designed to solve the opacity and trust deficit commonly found in enterprise AI agent interfaces. 

When AI agents take autonomous actions, they often rely on probabilistic reasoning and dynamic inputs that leave users with calibration uncertainty. To solve this, our frontend dashboard requires structured, explainable data. This repository provides the lightweight Python generation script and the resulting JSON output used to power our visual interactive prototype.

---

## 📂 Repository Contents
This repository is intentionally minimal and contains strictly the data generation logic required to simulate our IT environment:

* **`data_generator.py`**: A Python script utilizing the `Faker` library to simulate IT security logs and translate technical indicators into human-readable explanations.
* **`trustlens_output.json`**: The generated JSON file that acts as the structured mock database for our frontend dashboard components. 

---

## 🔍 The Prototype: Core Transparency Elements
While the interactive visual interface is hosted externally in our Figma prototype, the JSON data generated in this repository strictly maps to the **five core transparency elements** required to build trustworthy AI workflows:

1. **Reasoning Steps (`reasons`)**: The script's logic translates raw machine logs (e.g., identifying an unknown executable) into non-technical, plain-language explanations so the agent's thought process is visible to non-experts.
2. **Contextualised Confidence (`confidence`)**: Alert confidence is clearly labeled qualitatively (e.g., "High" or "Medium") to help the administrator gauge trust, rather than relying solely on an opaque probability score.
3. **Data Source Attribution (`data_sources`)**: Every alert explicitly cites the specific telemetry, security logs, or scanners used to formulate the recommendation.
4. **Known Limitations (`limitations`)**: The output explicitly surfaces the AI's boundaries (e.g., "Possible false positive" or "Insufficient historical data") so the operator knows when the AI might be operating at the edge of its capability.
5. **Human-in-the-Loop Controls (`recommendation`)**: The JSON structures actionable recommendations (e.g., "Quarantine Device" or "Force Password Reset") that are sent to the UI to await explicit human approval, ensuring the AI does not execute high-impact actions fully autonomously. 

---

## 🚀 Getting Started
If you wish to regenerate the data or add new simulated alerts to the pipeline, follow these steps:

### 1. Install Dependencies
Ensure you have Python installed, along with the required `Faker` library.
```bash
pip install Faker
```

### 2. **Execute the Script**
   Run the generator file from your terminal.

```bash
python data_generator.py
```

### 3. **Verify Output**
   The script will print the structured payload directly to the console and automatically write the updated data to ```trustlens_output.json``` in your root directory.

### 👥 Team SecureSight
A team of Sophomores in B.Tech Computer Science and Engineering (CSE), Institute of Technical Education and Research (ITER), SOA
* **Saurav Sharma** [Leader]
* **Atulya Mishra**
* **Vikash Raj**
* **Sujay Shaw**
