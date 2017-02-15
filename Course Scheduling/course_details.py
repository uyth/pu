# Fetching and returning course details.

import requests

base_url = "http://www.ime.ntnu.no/api/course/en/"
code = input("Please provide a course code: ")

# Fetch the course
course = requests.get(base_url + code).json()

# Get relevant data and print it
code = course["course"]["code"]
name = course["course"]["name"]
exam_date = course["course"]["assessment"][0]["date"]

t = course["course"]

print("Exam date for", code, name, "is", exam_date)
print()
print(t)


def get_code(course):
    """
    Fetches course code.
    :param course: json
    :return: Returns the string course code
    """
    return course["course"]["code"]


def get_name(course):
    """
    Fetches full course name.
    :param course: json
    :return: String course name
    """
    return course["course"]["name"]


def get_credit(course):
    """
    Fetch credited credit for completing course.
    :param course: json
    :return: Float credits
    """
    return course["course"]["credits"]


def get_description(course):
    """
    Fetches course description.
    :param course:
    :return: String description.
    """
    return course["course"]["infotype"][1]['text']


#TODO: More getters.