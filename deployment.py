import sys, errno
import argparse
import json
import requests

# Ensure empty strings can't be passed for required arguments
def non_empty_string(s):
    if not s:
        raise ValueError("Must not be empty string")
    return s

# Define arguments
parser = argparse.ArgumentParser()
parser.add_argument('--apiKey', required=True, type=non_empty_string)
parser.add_argument('--version', required=True, type=non_empty_string)
parser.add_argument('--authToken', required=True, type=non_empty_string)
parser.add_argument('--ownerName')
parser.add_argument('--emailAddress')
parser.add_argument('--comment')
parser.add_argument('--scmIdentifier')
parser.add_argument('--scmType')
parser.add_argument('--createdAt')

parser.add_argument('--ghAction', action='store_true')

# Parse arguments
args, extra = parser.parse_known_args()

# Remove empty arguments
data = vars(args)
for key, value in list(data.items()):
    if value is None: del data[key]

# Build URL, remove auth token from payload
url = "https://app.raygun.com/deployments?authToken={}".format(data["authToken"])
del data["authToken"]

# Check if we should output in the Github Action format
ghAction = "ghAction" in data
if ghAction:
    del data["ghAction"]

# Make request
response = requests.post(url, json.dumps(data))

if response.ok:
    result = json.loads(response.text)

    if ghAction:
        for output,value in result.items():
            print("::set-output name={}::{}".format(output, value))
    else:
        print(result)
    sys.exit(0)
else:
    error = {}
    error["error"] = response.reason
    print(error)
    sys.exit(errno.ECONNABORTED)
