import sys, json, codecs, apiai
from Core import action_handler

CLIENT_ACCESS_TOKEN = 'a2ed79849dd443bf95c422257d78f816'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

def request():
    # Create a request
    request = ai.text_request()
    request.query = input("You: ")

    # Get respons, convert to json and print it
    response = request.getresponse().read().decode('utf-8')
    response = json.loads(response)
    print("Recognized action:", response["result"]["action"])
    response = action_handler.action(response, response["result"]["action"])
    print("Parry:", response["result"]["fulfillment"]["speech"])
    print()
    return

if __name__ == '__main__':
    while True:
        request()
