import requests
import json
import sys

import random
import time

# Generate a random 8-digit number
random_number = random.randint(10000000, 99999999)

# Query as command line argument.
if len(sys.argv) <=1 :
    query = "How can i help you?"
else:
    query = sys.argv[1]
    
print(f"\n\nQUERY : {query}\n")

# Define the header and data
header = {
    "Content-Type": "application/json",
    "X-SLLM-Request-Id": "da97e77e-2c30-4301-9790-90c3e581c332",
    "x-dkubex-conversation-id": "ff2081a8-65e8-475d-8a0e-f43e1312cd63",
    #"Authorization" : "Bearer dGo0M2thM2F3eTVncjgxI3ZpdmVrQG9uZWNvbnZlcmdlbmNlLmNvbQ=="
     "Authorization" : "Bearer YWxsb3cjdml2ZWtAb25lY29udmVyZ2VuY2UuY29t" 
}

null = None

random_number = "736e35f8-9bdc-4c9c-8674-33e3c68fde4d"

data = {
  "virtualAgentId": "Test",
  "botConfig": "{\n  \"webhookUrl\": https://a3b3564f1160545dd88fb8ee48dc1919-bc50e9bffcf4a268.elb.us-east-1.amazonaws.com/gicsrbot/api/gichat,\n  \"authorizationHeader\": null,\n  \"customHeaders\": [\n    {\n      \"name\": \"ContentType\",\n      \"value\": \"application/json\"\n    },\n    {\n      \"name\": \"Accept\",\n      \"value\": \"application/json\"\n    }\n  ],\n  \"endpointParameters\": [\n    {\n      \"name\": \"test\",\n      \"value\": \"zee\"\n    }\n  ],\n  \"schemaVersion\": \"V1\",\n  \"timeout\": 10000,\n  \"webhookClientCertificates\": []\n}",
  "userInput": "How can i help you?",
  #"userInput": "run the workflow CloseConversation",
  # "userInput": "escalate",
  "userInput": query,
  "userInputType": 5,
  "executionInfo": {
    "contactId": random_number,
    "busNo": 4602609,
    "requestId": 6,
    "actionType": "RESTPROXY",
    "actionId": 6,
    "scriptName": "System\\Imposters\\RestProxy_Imposter"
  },  
  "systemTelemetryData": {
    "consumerProcessHost": "AOA-C32COR01",
    "consumerProcessName": "VCSvc",
    "consumerProcessVersion": "5.1.1.1",
    "inContactClusterAlias": null,
    "inContactScriptEngineHost": "AOA-C32COR01",
    "consumerMetaData": null
  },  
  "base64wavFile": null,
  "botSessionState": null,
  "customPayload": {
    "language": "",
    "channel": "",  
    "contactId": "",
    "message": "Hi",
    # "agentId": "25914192",
    # "agentId": "help",
    "agentId": "help@oneconvergence.com",
    "dynamic_data": "{}",
    "language": "en",
    "channel": "chat",
    "convForm": {
      "category": "Consumer",
      "role": "",
      "state": "NV",
      "topics": "General"
    }
  },
  "mediaType": "Chat"
}

# data = {
#   "virtualAgentId": "Test",
#   "botConfig": "{\n  \"webhookUrl\": https://a7bb83d5c2fbc4fb1922df3b04477c04-ec6d78e1a28ce66a.elb.us-west-2.amazonaws.com/giniceapi/api/gichat,\n  \"authorizationHeader\": null,\n  \"customHeaders\": [\n    {\n      \"name\": \"ContentType\",\n      \"value\": \"application/json\"\n    },\n    {\n      \"name\": \"Accept\",\n      \"value\": \"application/json\"\n    }\n  ],\n  \"endpointParameters\": [\n    {\n      \"name\": \"test\",\n      \"value\": \"zee\"\n    }\n  ],\n  \"schemaVersion\": \"V1\",\n  \"timeout\": 10000,\n  \"webhookClientCertificates\": []\n}",
#   "userInput": "What is ACA?",
#   "userInputType": 5,
#   "executionInfo": {
#     "contactId": 506314056968,
#     "busNo": 4602609,
#     "requestId": 6,
#     "actionType": "RESTPROXY",
#     "actionId": 6,
#     "scriptName": "System\\Imposters\\RestProxy_Imposter"
#   },  
#   "systemTelemetryData": {
#     "consumerProcessHost": "AOA-C32COR01",
#     "consumerProcessName": "VCSvc",
#     "consumerProcessVersion": "5.1.1.1",
#     "inContactClusterAlias": null,
#     "inContactScriptEngineHost": "AOA-C32COR01",
#     "consumerMetaData": null
#   },  
#   "base64wavFile": null,
#   "botSessionState": null,
#   "customPayload": {
#     "unique_id": "545454",
#     "tenant_id": "tenant_11811131",
#     "message": "8137313475",
#     "metadata": {
#       "bot_id": "8KqDBlD1qbDJyB8GctVQleJSU6HvdxvL",
#       "bot_name": "Vimo Demo"
#     },
#     "dynamic_data": "{}",
#     "language": "en",
#     "channel": "chat",
#     "convForm": {
#       "category": "Consumer",
#       "role": "L2",
#       "state": "PA",
#       "topics": "All"
#     }
#   },
#   "mediaType": "Chat"
# }
# data = {
#   "virtualAgentId": "GI Chat",
#   "botConfig": "{\n  \"webhookUrl\": \"https://nvbot.ginicechat.com/gicsrbot/api/gichat/\",\n  \"authorizationHeader\": null,\n  \"customHeaders\": [\n    {\n      \"name\": \"x-dkubex-conversation-id\",\n      \"value\": \"ff2081a8-65e8-475d-8a0e-f43e1312cd63\"\n    },\n    {\n      \"name\": \"Authorization\",\n      \"value\": \"Bearer dGo0M2thM2F3eTVncjgxI25pY2VAZ2V0aW5zdXJlZC5jb20=\"\n    },\n    {\n      \"name\": \"X-SLLM-Request-Id\",\n      \"value\": \"da97e77e-2c30-4301-9790-90c3e581c332\"\n    }\n  ],\n  \"endpointParameters\": [],\n  \"schemaVersion\": \"V1\",\n  \"timeout\": 10000,\n  \"webhookClientCertificates\": []\n}",
#   "userInput": "What are the EHB deductible for dental plans?",
#   "userInputType": 1,
#   "executionInfo": {
#     "contactId": 510212552349954,
#     "busNo": 4602609,
#     "requestId": 6,
#     "actionType": "TextBotExchange",
#     "actionId": 88,
#     "scriptName": "DEV\\CH - 01 - Agent Assist"
#   },
#   "systemTelemetryData": {
#     "consumerProcessHost": "AOA-C32COR01",
#     "consumerProcessName": "VCSvc",
#     "consumerProcessVersion": "5.1.1.1",
#     "inContactClusterAlias": null,
#     "inContactScriptEngineHost": "AOA-C32COR01",
#     "consumerMetaData": null
#   },
#   "base64wavFile": null,
#   "botSessionState": null,
#   "customPayload": {
#     "language": "en",
#     "channel": "chat",
#     "agentId": "help@oneconvergence.com",
#     "contactId": "",
#     "convForm": {
#       "category": "Consumer",
#       "role": "L1",
#       "state": "NV",
#       "topics": "All"
#     }
#   },
#   "mediaType": "Chat",
#   "branchName": "PromptAndCollectNextResponse"
# }


# Define the URL
# url = "https://a3b3564f1160545dd88fb8ee48dc1919-b01b0c84ed7ade8e.elb.us-east-1.amazonaws.com/gicsrbot/api/gichat"
# url = "https://nvbot.ginicechat.com/gicsrbot/api/gichat/"
# url = "https://192.168.200.132:32443/gi-lama1/api/gichat/"
# url = "https://a233a40ceafa1409bacbe6aa5b51af3f-e34106682552bf22.elb.us-west-2.amazonaws.com/gicsrbot/api/gichat/"
# url = "https://devbot.ginicechat.com/gicsrbot/api/gichat/"
# url = "https://devbot.ginicechat.com/gi-v-test/api/gichat/"
# app_url = "https://192.168.200.132:32443/nice-llm-sec-4/"
app_url = "https://ad46449457b5e4d7fbc99eb01dc7dbc8-ba8182fca0a35e00.elb.us-east-1.amazonaws.com/sharmi56/"
# app_url = "https://192.168.200.132:32443/nice-llm-sec-5/"
url = app_url + "api/gichat/"
# url = "https://192.168.200.132:32443/nice-1/api/gichat/"


# Make the POST request
start_time = time.time()
response = requests.post(url, headers=header, data=json.dumps(data),  verify=False)
end_time = time.time()
duration = end_time - start_time
# Check the response
if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    # print(response.text,'\n')  # Assuming the response is in JSON format
    # print(response.headers.get('content-type'),'\n')
    print(f"Raw Resp : {response}\n\n")  # Print the response content if request fails
    print(f"resp json : {response.json()}")  # Assuming the response is in JSON format
else:
    print(f"Request failed with status code: {response.status_code}")
    print("Response:")
    print(response)  # Print the response content if request fails


