# Ues 1024.no's Data API to get curse information from NTNU.
# Author: Martin Langmo Karlstrøm

import requests

base_url_1 = "http://www.ntnu.no/web/studier/emner?p_p_id=coursedetailsportlet_WAR_courselistportlet&p_p_lifecycle" \
                "=2&p_p_resource_id=timetable&_coursedetailsportlet_WAR_courselistportlet_year=2017" \
                "&_coursedetailsportlet_WAR_courselistportlet_courseCode="
base_url_2 = "&year=2017&version=1"

code = input("Course code:\n>> ").upper()



# Fetch the course
course = requests.get(base_url_1 + code + base_url_2).json()

# Get relevant data
# Name

code = course["course"]["summarized"][0]["courseCode"]
name = course["course"]["summarized"][0]["courseName"]
print()
print(code + ' ' + name)