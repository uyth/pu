from course_schedule.course_details import *


def stars():
    print("*" * 69)


def print_stuff(code, program):
    print()
    print()
    stars()
    print("*" * 20 + "    PARRY'S METHOD TESTER    " + "*" * 20)
    stars()
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
    print("7. Credits")
    print()
    print("\'C\' to change code")
    print("\'P\' to change program")
    print("\'Q\' to quit")
    print("\'M\' for menu")
    stars()
    print()


def main():
    code = "tdt4145"
    program = "MTDT"

    print_stuff(code, program)

    while True:
        ans = input("Action:\n>> ")

        if ans == '1':
            stars()
            print(get_name(code))
            stars()
        elif ans == '2':
            stars()
            print(code.upper())
            stars()
        elif ans == '3':
            stars()
            print(get_description(code))
            stars()
        elif ans == '4':
            stars()
            print(get_exam_date_readable(code))
            stars()
        elif ans == '5':
            stars()
            print(get_days_until(code))
            stars()
        elif ans == '6':
            stars()
            print(get_schedule(code, program))
            stars()
        elif ans == '7':
            stars()
            print(get_credits(code))
            stars()

        elif ans == "P":
            program = input("New program:\n>> ")
        elif ans == "C":
            code = input("New course:\n>> ")
        elif ans == 'M':
            print_stuff(code, program)
        elif ans == "Q":
            break

if __name__ == '__main__':
    main()
