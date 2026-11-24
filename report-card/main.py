from app import main
from pathlib import Path


def set_class():
    while True:
        try:
            class_name = input("class name: ").strip().title()
            if len(class_name) < 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid class name")
    while True:
        correction = input(
            f"class name is {class_name}\n correct (y/n)? ").strip().lower()
        try:
            if correction == "y":
                Path(f"school/{class_name}").mkdir(parents=True, exist_ok=True)
                break
            elif correction == "n":
                while True:
                    try:
                        class_name = input(
                            "try again\nclass name: ").strip().title()
                        if len(class_name) < 2:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("Invalid class name")
            else:
                raise ValueError
        except ValueError:
            print("Invalid input try again")
    return class_name


def set_students():
    while True:
        try:
            number_students = int(
                input("how many students are in this class? "))
            if 0 < number_students <= 50:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input")
    while True:
        try:
            correction = input(
                f"students = {number_students}\n correct (y/n)? ").strip().lower()
            if correction == "y":
                break
            elif correction == "n":
                while True:
                    try:
                        number_students = int(input(
                            "try again\nhow many students are in this class? "))
                        if 0 < number_students <= 50:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid input")
            else:
                raise ValueError
        except ValueError:
            print("Invalid input")
    return number_students


def execute():
    class_name = set_class()
    number_students = set_students()
    for i in range(number_students):
        main(class_name)


if __name__ == "__main__":
    execute()
