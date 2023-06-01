import requests
headers = {"Content-Type": "application/vnd.github+json"}

payload = {
    "event_type": "i",
    "client_payload":{
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"}}
