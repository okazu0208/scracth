import requests
headers = {"Content-Type": "application/vnd.github+json"}

payload = {
    "event_type": "my-custom-event",
    "client_payload":{
        "key1": "value1",
        "key2": "value2"}}