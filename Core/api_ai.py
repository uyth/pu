

import sys, json, codecs, apiai
from course_schedule import course_details



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


def action(response, action):
    """
    Action will change witai response if it recognizes a valid action, ele fallback to apiai response
    if unknown value changed, it is added to result as a new parameter.
    :param response:
    :param action:
    :return: Response
    """
    # if action recognized, change response
    try:
        if action == "get_schedule":
            course_code = response["result"]["parameters"]["course"]
            program = response["result"]["parameters"]["program"]
            schedule = course_details.get_schedule(course_code, program)
            if course_code != "" and program != "":
                print(course_code, program)
                response["result"]["fulfillment"]["speech"] = \
                    response["result"]["fulfillment"]["speech"].replace("$schedule", schedule)
                response["result"]["parameters"]["schedule"] = schedule
                print(response)
        if action == "get_exam_date":
            course_code = response["result"]["parameters"]["course"]
            date = course_details.get_exam_date(course_code)
            days_until = course_details.get_days_until(course_code)
            print(date, days_until)
            response["result"]["fulfillment"]["speech"] = \
                response["result"]["fulfillment"]["speech"].replace("$date", date).replace("$days_until", days_until)
            response["result"]["parameters"]["date"] = date
            response["result"]["parameters"]["days_until"] = days_until
    except:
        pass
    return response

if __name__ == '__main__':
    while True:
        request()