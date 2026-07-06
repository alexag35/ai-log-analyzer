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

###### &#x20;  git clone https://github.com

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

###### \- \[ ] Integrate a live local LLM using \*\*Ollama\*\* (`llama3` or `mistral`) for 100% private, offline data processing.

###### \- \[ ] Add JSON parsing support to ingest cloud logs (AWS CloudTrail / Windows Event Logs).

###### \- \[ ] Implement an automated email/Slack alert trigger when a `High` severity threat is detected.

###### 

