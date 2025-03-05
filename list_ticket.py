# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://prabhatgouda.atlassian.net/rest/api/3/project"


auth = HTTPBasicAuth("prabhatgouda12111998@gmail.com", "API_token")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)

print(output) 
# for name in output:
#     print(output[name]["name"])
for project in output:
    print(f"Project Name: {project['name']}")
    print(f"Project Key: {project['key']}")
