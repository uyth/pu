# Fetching and returning course details.

import requests
import datetime
from datetime import datetime

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

def get_days_until(code):
    """
    Days until exam in given subject.
    :param code: String of course code.
    :return: String days until exam
    """
    date_format = "%Y-%m-%d"
    input_date = get_exam_date(code)
    exam_date = datetime.strptime(input_date, date_format)
    today = datetime.today()
    diff = exam_date - today

    return str(diff.days)


def get_schedule(code, program):
    """
    Builds the schedule of a single course.
    :param code: Course code
    :param program: Study program (MTDT, BIT, ...)
    :return: String timetable
    """

    # Uses 1024 API, makes course as dictionary and fetches correct subsection.
    course = jason_to_dictionary(code.upper())[1]
    s = course["course"]["summarized"]

    # Starts with empty time table (schedule) and hashed days (API).
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
    table = {}
    prev_day = 0
    # Iterate through all lectures on 1024 (s).
    for lecture in s:
        # If correct parallel, include in table; times, room, description.
        if program.upper() in lecture["studyProgramKeys"]:
            # (day, from, to, room, type)
            day_int = lecture["dayNum"]
            if prev_day == day_int:
                table[day_int].append(
                    (lecture["from"], lecture["to"], lecture["rooms"][0]["romNavn"], lecture["description"]))
            else:
                table[day_int] = []
                table[day_int].append(
                    (lecture["from"], lecture["to"], lecture["rooms"][0]["romNavn"], lecture["description"]))

            prev_day = day_int

    # Make schedule as printable string.
    ret = ''
    for key, day in table.items():
        for lecture in day:
            ret += days[key] + '\n' + lecture[3] + ', ' + lecture[2] + '\n'\
               + lecture[0] + ' - ' + lecture[1] + '\n\n'

    if len(ret) == 0:
        return "You do not have this subject."
    else:
        return ret
