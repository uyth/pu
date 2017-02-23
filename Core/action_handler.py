from course_schedule import course_details

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
        parameters = []

        if action == "get_schedule":
            # get parameters: cours_code, program, and schedule
            course_code = response["result"]["parameters"]["course"]
            program = response["result"]["parameters"]["program"]

            # if user input parameters missing skip response change and request more input
            if course_code != "" and program != "":
                # add schedule as (name, value) in parameters
                parameters.append(("schedule", course_details.get_schedule(course_code, program)))

        if action == "get_exam_date":
            # get paramters: course_code, date, days_until
            course_code = response["result"]["parameters"]["course"]

            # add date, days_until as (name, value) in parameters
            parameters.append(("date", course_details.get_exam_date(course_code)))
            parameters.append(("days_until", course_details.get_days_until(course_code)))

        if action == "get_course_description":
            # get course_code
            course_code = response["result"]["parameters"]["course"]
            # add course description as (name, value) in parameters
            parameters.append(("course_description", course_details.get_description(course_code)))

        # modify response
        response = correct_reponse_speech(response, parameters)

    except:
        pass
    return response

def correct_reponse_speech(response, parameters):
    """
    correct_response_speech will add uknown parameters and values to the response to give the
    correct speech
    :param parameters:
    :param response:
    return:
    """

    for parameter in parameters:
        # add parameters to response
        response["result"]["parameters"][parameter[0]] = parameter[1]
        # replace placeholder parameter in response
        response["result"]["fulfillment"]["speech"] = \
            response["result"]["fulfillment"]["speech"].replace("$" + parameter[0], parameter[1])

    return response