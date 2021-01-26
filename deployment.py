import sys, errno
import argparse
import json
import requests

# Define arguments
parser = argparse.ArgumentParser()
parser.add_argument('--apiKey', required=True)
parser.add_argument('--version', required=True)
parser.add_argument('--authToken', required=True)
parser.add_argument('--ownerName')
parser.add_argument('--emailAddress')
parser.add_argument('--comment')
parser.add_argument('--scmIdentifier')
parser.add_argument('--scmType')
parser.add_argument('--createdAt')

# Parse arguments
args, extra = parser.parse_known_args()

# Remove empty arguments
data = vars(args)
for key, value in list(data.items()):
    if value is None: del data[key]

# Build URL, remove auth token from payload
url = "https://app.raygun.com/deployments?authToken={}".format(data["authToken"])
del data["authToken"]

# Make request
response = requests.post(url, json.dumps(data))
if (response.ok):
    result = json.loads(response.text)
    print(result)
    sys.exit(0)
else:
    error = {}
    error["error"] = response.reason
    print(error)
    sys.exit(errno.ECONNABORTED)
