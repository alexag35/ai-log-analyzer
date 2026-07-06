import os
import requests
LOG_FILE_PATH = os.path.join("data", "mock_logs.log")
if not os.path.exists(LOG_FILE_PATH):
    print(f"Error: Could not find the log file at {LOG_FILE_PATH}")
    exit(1)

with open(LOG_FILE_PATH, "r") as file:
    log_data = file.read()
print("Successfully loaded mock logs. Sending data to AI for triage...")
system_instruction = (
    "You are an automated Security Operations Center (SOC) Analyst. "
    "Review the following system logs. Identify any security threats, "
    "list suspicious IP addresses, and provide a clear severity rating (Low, Medium, High). "
    "Keep your final summary punchy and easy for a human defender to read."
)
api_url = "https://duckduckgo.com"
print("\n--- AI ANALYSIS REPORT ---")
print(f"Analyzing {len(log_data.splitlines())} log lines...\n")
print(f"PROMPT SENT TO AI:\n{system_instruction}\n\nDATA:\n{log_data}")