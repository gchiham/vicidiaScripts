'''
Get recordings URLs in JSON format using LEAD ID
'''

import requests
import re
import json

def get_recordings_for_lead():
    lead_id = input("Enter the lead ID: ")

    api_url = "https://YourServer.com/vicidial/non_agent_api.php"
    params = {
        "source": "Anything",
        "user": "6666", # ENTER YOU NON AGENT API USER AND PASSWORD
        "pass": "6666",
        "function": "recording_lookup",
        "lead_id": lead_id,
        "stage": "ALL"
    }

    response = requests.get(api_url, params=params)
    recordings = response.text

    # Extracting URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', recordings)
    
    # Creating a JSON object
    json_output = json.dumps(urls, indent=4)
    return json_output

if __name__ == "__main__":
    recording_urls_json = get_recordings_for_lead()
    print(recording_urls_json)
