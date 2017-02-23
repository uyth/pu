import requests

base_url = "http://www.ime.ntnu.no/api/course/en/"

def get_exam_date(course_code):
    # Fetch the course
    course = requests.get(base_url + course_code).json()

    # course_code = course["course"]["code"]
    # name = course["course"]["name"]
    exam_date = course["course"]["assessment"][0]["date"]
    # t = course["course"]
    return exam_date
