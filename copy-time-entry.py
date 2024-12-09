import requests # type: ignore

# Replace with your actual API keys and workspace IDs
source_api_key = "your_source_api_key"
target_api_key = "your_target_api_key"
source_workspace_id = "your_source_workspace_id"
target_workspace_id = "your_target_workspace_id"
target_project_id = "your_target_project_id"

# Get projects and time entries from the source workspace
headers = {"X-Api-Key": source_api_key}
response = requests.get(
    f"https://api.clockify.me/api/v1/workspaces/{source_workspace_id}/time-entries",
    headers=headers
)
time_entries = response.json()

# Post time entries to the target workspace
headers = {"X-Api-Key": target_api_key}
for entry in time_entries:
    entry_data = {
        "start": entry["timeInterval"]["start"],
        "end": entry["timeInterval"]["end"],
        "description": entry["description"],
        "projectId": target_project_id,  # Map source project to target project
    }
    requests.post(
        f"https://api.clockify.me/api/v1/workspaces/{target_workspace_id}/time-entries",
        headers=headers,
        json=entry_data
    )
