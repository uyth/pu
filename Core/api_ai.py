# API.AI Example
# This example shows how API.AI can be used to process requests
# The connected bot will recognize requests for news, and will output the requested action and topic
# Feel free to insert your own client access token to connect your own bot
# Author: Audun Liberg

import sys, json, codecs, apiai
from course_schedule import exam_date_IME

CLIENT_ACCESS_TOKEN = 'a2ed79849dd443bf95c422257d78f816'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

def request():
    # Create a request
    request = ai.text_request()
    request.query = input("Say something: ")

    # Get respons, convert to json and print it
    response = request.getresponse().read().decode('utf-8')
    response = json.loads(response)
    print("Recognized action:", response["result"]["action"])
    response = action(response, response["result"]["action"])
    print("Recognized topic:", response["result"]["fulfillment"]["speech"])
    print()
    return

# action will change witai response if it recognizes a valid action, else fallback to apiai response
def action(response, action):
    # if action recognized, change response
    if action == "schedule":
        pass
    if action == "get_exam_date":
        course_code = response["result"]["parameters"]["course"]
        date = exam_date_IME.get_exam_date(course_code)
        response["result"]["fulfillment"]["speech"] = \
            response["result"]["fulfillment"]["speech"].replace("$date", date)
    return response

if __name__ == '__main__':
    while True:
        request()
