ai-log-analyzer

# AI-Powered Log Analyzer \& Alert Triage Tool
===

###### 

###### A beginner-friendly cybersecurity automation script that reads system/firewall logs, structures them alongside a specialized security persona, and prepares them for automated threat triage using Large Language Models (LLMs).

###### 

###### \## 🚀 Project Overview

###### Manual log analysis is time-consuming for Security Operations Center (SOC) analysts. This project demonstrates how Python can be combined with AI to parse logs instantly, identify suspicious behavioral patterns (such as brute-force attacks), and rank alert severity (Low, Medium, High).

###### 

###### \### Core Features

###### \- \*\*Automated Ingestion:\*\* Safely reads raw, local log data from an isolated directory.

###### \- \*\*Contextual Engineering:\*\* Implements a strict system prompt to reduce AI hallucinations.

###### \- \*\*Extensible Integration:\*\* Built to seamlessly connect with local models (Ollama/Llama-3) or cloud-based AI endpoints.

###### 

###### \## 📁 Repository Structure

###### ```text

###### ai-log-analyzer/

###### ├── data/

###### │   └── mock\_logs.log   # Synthetic server logs containing a simulated SSH brute-force attack

###### ├── analyzer.py         # Main Python engine that parses logs and generates AI prompts

###### ├── requirements.txt    # Project dependencies (requests library)

###### └── README.md           # Documentation and portfolio write-up

###### ```

###### 

###### \## ⚙️ Installation \& Usage

###### 

###### 1\. \*\*Clone the repository:\*\*

###### &#x20;  ```bash

###### &#x20;  git clone https://github.com/alexag35/ai-log-analyzer.git

###### &#x20;  cd ai-log-analyzer

###### &#x20;  ```

###### 

###### 2\. \*\*Install dependencies:\*\*

###### &#x20;  ```bash

###### &#x20;  pip install -r requirements.txt

###### &#x20;  ```

###### 

###### 3\. \*\*Run the analyzer:\*\*

###### &#x20;  ```bash

###### &#x20;  python analyzer.py

###### &#x20;  ```

###### 

###### \## 🔍 Future Enhancements

###### \- \[x] Integrate a live local LLM using \*\*Ollama\*\* (`llama3` or `mistral`) for 100% private, offline data processing.

###### - [x] Automate local reporting by auto-saving threat summaries to an isolated text file.

###### - [x] Build an active hardware threat alarm using sound frequencies to notify human defenders of High severity incidents.

###### \- \[ ] Add JSON parsing support to ingest cloud logs (AWS CloudTrail / Windows Event Logs).

###### \- \[ ] Implement an automated email/Slack alert trigger when a `High` severity threat is detected.

###### 

## 🛡️ Enterprise Architecture Context (SIEM & SOAR)
In a real-world enterprise environment, this script functions as an automated **SOAR (Security Orchestration, Automation, and Response)** extension rather than a standalone logger. It sits at the final tier of the standard defensive data pipeline:

1. **Ingestion (The OS/App):** Production environments (Windows/Linux) capture user login events natively.
2. **Collection (The SIEM):** Aggregators like Splunk or ElasticSearch centralize data feeds.
3. **Triage (This Tool):** This Python script queries the data pipeline, leverages local LLMs (Ollama) to bypass data privacy restrictions, dynamically updates active triage text files, and sounds physical hardware alerts for high-severity incidents requiring immediate human review.

This structure allows human defenders to bypass manual log audits and focus exclusively on high-priority security exceptions flagged by the orchestration engine.


