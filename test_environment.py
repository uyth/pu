from course_schedule.course_details import *


code = "tdt4145"
program = "MTDT"

print("*" * 69)
print("*" * 20 + "    PARRY'S METHOD TESTER    " + "*" * 20)
print("*" * 69)
print("Current course: " + code.upper())
print("Current program: " + program.upper())
print()
print("get_course_ ...")
print("1. Name")
print("2. Code")
print("3. Description")
print("4. Exam date")
print("5. Days until exam")
print("6. Schedule")
print()
print("\'C\' to change code")
print("\'P\' to change program")
print("\'Q\' to quit")
print("\'M\' for menu")
print("*" * 49)
print()


while True:

    ans = input("Action:\n>> ")

    if ans == '1':
        print("*" * 69)
        print(get_name(code))
        print("*" * 69)
    elif ans == '2':
        print("*" * 69)
        print(code.upper())
        print("*" * 69)
    elif ans == '3':
        print("*" * 69)
        print(get_description(code))
        print("*" * 69)
    elif ans == '4':
        print("*" * 69)
        print(get_exam_date(code))
        print("*" * 69)
    elif ans == '5':
        print("*" * 69)
        print(get_days_until(code))
        print("*" * 69)
    elif ans == '6':
        print("*" * 69)
        print(get_schedule(code, program))
        print("*" * 69)

    if ans == "P":
        program = input("New program:\n>> ")
    elif ans == "C":
        code = input("New course:\n>> ")
    elif ans == 'M':
        print("*" * 69)
        print("*" * 20 + "    PARRY'S METHOD TESTER    " + "*" * 20)
        print("*" * 69)
        print("Curre6nt course: " + code.upper())
        print("Current program: " + program.upper())
        print()
        print("get_course_ ...")
        print("1. Name")
        print("2. Code")
        print("3. Description")
        print("4. Exam date")
        print("5. Days until exam")
        print("6. Schedule")
        print()
        print("\'C\' to change code")
        print("\'P\' to change program")
        print("\'Q\' to quit")
        print("\'M\' for menu")
        print("*" * 69)
        print()
    elif ans == "Q":
        break
