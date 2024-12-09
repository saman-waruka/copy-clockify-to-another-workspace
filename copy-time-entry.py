import requests
import json
import time

# Replace with your actual API keys and workspace IDs
source_user_id = 'your_source_user_id' # your source user id that add these time entries
source_api_key = "your_source_api_key"
target_api_key = "your_target_api_key"
source_workspace_id = "your_source_workspace_id"
target_workspace_id = "your_target_workspace_id"
source_project_id = "your_source_project_id"
target_project_id = "your_target_project_id"

# Get projects and time entries from the source workspace
headers = {"X-Api-Key": source_api_key}
response = requests.get(
    f"https://api.clockify.me/api/v1/workspaces/{source_workspace_id}/user/{source_user_id}/time-entries?page-size=5000",
    headers=headers
)
time_entries = response.json()
print("time_entries",json.dumps(time_entries, indent=4))

# Filter time entries by projectId
filtered_entries = [entry for entry in time_entries if entry["projectId"] == source_project_id]
print("filtered_entries", json.dumps(filtered_entries, indent=4))

# Post time entries to the target workspace
target_headers = {"X-Api-Key": target_api_key}
for entry in filtered_entries:
    print("entry",entry)
    entry_data = {
        "start": entry["timeInterval"]["start"],
        "end": entry["timeInterval"]["end"],
        "description": entry["description"],
        "billable": entry["billable"],
        "projectId": target_project_id,  # Map source project to target project
    }
    insert_response = requests.post(
        f"https://api.clockify.me/api/v1/workspaces/{target_workspace_id}/time-entries",
        headers=target_headers,
        json=entry_data
    )
    print(" entry[description] :",  entry["description"])
    print("response: ", json.dumps(insert_response.json(), indent=4))
    time.sleep(0.02)  # Note sleep 0.02 cause clockify api has rate limit is 50 request/second
