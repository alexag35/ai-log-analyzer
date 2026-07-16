import os
import json
import requests
import winsound

LOG_FILE_PATH = os.path.join("data", "mock_logs.log")
REPORT_FILE_PATH = "triage_report.txt"

# 1. Read and parse the local log data safely
if not os.path.exists(LOG_FILE_PATH):
    print(f"Error: Could not find the log file at {LOG_FILE_PATH}")
    exit(1)

with open(LOG_FILE_PATH, "r") as file:
    raw_content = file.read()

print("Successfully loaded log file. Parsing structure...")

# Initialize an empty string to hold formatted log logs for the AI
formatted_logs = ""

try:
    # Attempt to load the log dataset as structured JSON data
    json_data = json.loads(raw_content)
    print("[+] JSON data detected. Structuring cloud telemetry events...")
    
    for event in json_data:
        timestamp = event.get("eventTime", "N/A")
        action = event.get("eventName", "N/A")
        user = event.get("userIdentity", {}).get("userName", "Unknown")
        ip = event.get("sourceIPAddress", "N/A")
        status = "FAIL: " + event.get("errorCode") if event.get("errorCode") else "SUCCESS"
        
        # Build clean string representations of each cloud audit log
        formatted_logs += f"[{timestamp}] User: {user} | Action: {action} | Source IP: {ip} | Status: {status}\n"

except json.JSONDecodeError:
    print("[!] Standard plain-text log format detected. Fallback routing initiated.")
    formatted_logs = raw_content

# 2. Build the instruction prompt
system_prompt = (
    "You are an automated Cloud Security Operations Center (SOC) Analyst. "
    "Review the following processed cloud infrastructure logs. Identify any security threats, "
    "list suspicious IP addresses, and provide a clear severity rating (Low, Medium, High). "
    f"Keep your final summary punchy and easy for a human defender to read:\n\n{formatted_logs}"
)

# 3. Target the local Ollama API endpoint
ollama_url = "http://localhost:11434/api/generate"
payload = {
    "model": "llama3:8b",
    "prompt": system_prompt,
    "stream": False
}

try:
    print("Sending structured cloud telemetry to local AI for triage...")
    response = requests.post(ollama_url, json=payload, timeout=120)
    response.raise_for_status()
    
    analysis = response.json().get("response", "No response received.")
    print("\n--- AI AUTOMATED CLOUD TRIAGE REPORT ---")
    print(analysis)
    
    # 4. Auto-save the report to a text file
    with open(REPORT_FILE_PATH, "w", encoding="utf-8") as report_file:
        report_file.write("=== AUTOMATED CLOUD SOC ANALYST TRIAGE REPORT ===\n\n")
        report_file.write(analysis)
        
    print(f"\n[+] Success! Threat report auto-saved to: {REPORT_FILE_PATH}")

        # 5. Dynamic Threat Alarm System (Bulletproof Scan)
    if "high" in analysis.lower():

        print("\n🚨 [ALERT] CRITICAL CLREAT INTEL RECEIVED! INITIATING AUDIO ALARM...")
        for _ in range(3):
            winsound.Beep(2500, 400)
            winsound.Beep(1800, 300)
    else:
        print("\n[+] System state: Safe. No active alert alarms triggered.")

except requests.exceptions.RequestException as e:
    print(f"\nError connecting to Ollama: {e}")
