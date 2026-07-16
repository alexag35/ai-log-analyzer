import os
import requests
import winsound  # Built-in Windows library for audio feedback

LOG_FILE_PATH = os.path.join("data", "mock_logs.log")
REPORT_FILE_PATH = "triage_report.txt"

# 1. Read the local logs
if not os.path.exists(LOG_FILE_PATH):
    print(f"Error: Could not find the log file at {LOG_FILE_PATH}")
    exit(1)

with open(LOG_FILE_PATH, "r") as file:
    log_data = file.read()

print("Successfully loaded mock logs. Sending data to local AI for triage...")

# 2. Build the instruction prompt
system_prompt = (
    "You are an automated Security Operations Center (SOC) Analyst. "
    "Review the following system logs. Identify any security threats, "
    "list suspicious IP addresses, and provide a clear severity rating (Low, Medium, High). "
    f"Keep your final summary punchy and easy for a human defender to read:\n\n{log_data}"
)

# 3. Target the local Ollama API endpoint
ollama_url = "http://localhost:11434/api/generate"
payload = {
    "model": "llama3:8b",
    "prompt": system_prompt,
    "stream": False
}

try:
    # Send the logs to your offline AI engine
    response = requests.post(ollama_url, json=payload, timeout=120)
    response.raise_for_status()
    
    # Extract the real AI response
    analysis = response.json().get("response", "No response received.")
    
    print("\n--- AI AUTOMATED TRIAGE REPORT ---")
    print(analysis)
    
    # 4. Auto-save the report to a text file
    with open(REPORT_FILE_PATH, "w", encoding="utf-8") as report_file:
        report_file.write("=== AUTOMATED SOC ANALYST TRIAGE REPORT ===\n\n")
        report_file.write(analysis)
        
    print(f"\n[+] Success! Threat report auto-saved to: {REPORT_FILE_PATH}")

        # 5. NEW FEATURE: Dynamic Threat Alarm System (Improved Scan)
    # Triggers if the word "high" appears near the severity discussion
    if "high:" in analysis.lower() or "severity: high" in analysis.lower() or "high severity" in analysis.lower():
        print("\n🚨 [ALERT] CRITICAL THREAT INTEL RECEIVED! INITIATING AUDIO ALARM...")
        # Beep parameters: winsound.Beep(frequency_in_hz, duration_in_milliseconds)
        for _ in range(3):
            winsound.Beep(2500, 400)  # High-pitched panic tone
            winsound.Beep(1800, 300)  # Alternating warning tone
    else:
        print("\n[+] System state: Safe. No active alert alarms triggered.")

except requests.exceptions.RequestException as e:
    print(f"\nError connecting to Ollama: {e}")
    print("Make sure you ran 'ollama run llama3:8b' in another window first!")
