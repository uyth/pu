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

print("Exam:", exam_date)
print()
print(t)
