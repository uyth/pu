# Fetching and returning course details.

import requests


def jason_to_dictionary(course_code):
    base_ime = "http://www.ime.ntnu.no/api/course/en/"
    base_1024a = "http://www.ntnu.no/web/studier/emner?p_p_id=coursedetailsportlet_WAR_courselistportlet&p_p_lifecycle" \
                 "=2&p_p_resource_id=timetable&_coursedetailsportlet_WAR_courselistportlet_year=2017" \
                 "&_coursedetailsportlet_WAR_courselistportlet_courseCode="
    base_1024b = "&year=2017&version=1"

    url_ime = base_ime + course_code
    url_1024 = base_1024a + course_code + base_1024b

    # Fetch the course, parse to dict.
    courseIME = requests.get(url_ime).json()
    course1024 = requests.get(url_1024).json()

    # ime = [0], 1024 = [1]
    return courseIME, course1024


def get_name(code):
    """
    Fetches full course name.
    :param code: String of course code
    :return: String course name
    """
    course = jason_to_dictionary(code)[0]
    return course["course"]["name"]


def get_credits(code):
    """
    Fetch credited credit for completing course.
    :param code: String of course code
    :return: Float credits
    """
    course = jason_to_dictionary(code)[0]
    return course["course"]["creditTypeCode"] + ': ' + str(course["course"]["credit"])


def get_description(code):
    """
    Fetches course description.
    :param code: String of course code
    :return: String description.
    """
    course = jason_to_dictionary(code)[0]
    return course["course"]["infoType"][2]["text"]


def get_level(code):
    """
    Fetches course study level.
    :param code: String of course code
    :return: String study level.
    """
    course = jason_to_dictionary(code)[0]
    return course["course"]["studyLevelName"]


def get_exam_date(code):
    """
    Fetches course exam date.
    :param code: String of course code.
    :return: String exam date.
    """
    course = jason_to_dictionary(code)[0]
    date = course["course"]["assessment"][0]["date"]
    return date


def build_schedule(code, program):
    # Uses 1024 API, makes course as dictionary and fetches correct subsection.
    course = jason_to_dictionary(code)[1]
    s = course["course"]["summarized"]

    # Starts with empty time table (schedule) and hashed days (API).
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
    table = {}
    # Iterate through all lectures on 1024 (s).
    for lecture in s:
        # If correct parallel, include in table; times, room, description.
        if program.upper() in lecture["studyProgramKeys"]:
            # (day, from, to, room, type)
            day_int = lecture["dayNum"]
            table[day_int] = (lecture["from"], lecture["to"], lecture["rooms"][0]["romNavn"], lecture["description"])

    # Make schedule as printable string.
    ret = ''
    for key, day in table.items():
        ret += days[key] + '\n' + table[key][3] + ', ' + table[key][2] + '\n'\
               + table[key][0] + ' - ' + table[key][1]
        ret += '\n\n'

    return ret
