"""
A Python script that takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter.

- The letter must be sent in the variable q
- If no argument is given, set q=""
- If the response body is properly JSON formatted and not empty, 
display the id and name like this: [<id>] <name>
Otherwise:
- Display Not a valid JSON if the JSON is invalid
- Display No result if the JSON is empty
"""

import requests
import sys

if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q= ""


payload = {'q':q}
req = requests.post("http://0.0.0.0:5000/search_user", data = payload)
if req.status_code == 200 and print(req.raise_for_status) == "None":
    print("[{}] {}".format(req.json["id"], req.json["name"]))
elif req.json()== None:
    print("No result")
else:
    print("Not a valid JSON")
       

