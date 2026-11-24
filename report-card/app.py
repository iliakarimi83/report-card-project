import csv
from datetime import datetime
from pathlib import Path


def set_name():
    while True:
        try:
            first_name = input("first name: ").strip().title()
            last_name = input("last name: ").strip().title()
            if len(first_name) < 2 or len(last_name) < 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("name cannot be empty or under 2 characters")
    while True:
        correct_name = input(
            f"your name is {first_name} {last_name}\nis this correct (y/n)? ").strip().lower()
        try:
            if correct_name == "y":
                break
            elif correct_name == "n":
                while True:
                    try:
                        first_name = input(
                            "try again\nfirst name: ").strip().title()
                        last_name = input("last name: ").strip().title()
                        if len(first_name) < 2 or len(last_name) < 2:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("name cannot be empty or under 2 characters")
            else:
                raise ValueError
        except ValueError:
            print("invalid input, try again")
    return first_name, last_name


def get_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 20:
                return score
            else:
                raise ValueError
        except ValueError:
            print("you didn't enter a valid number")


def set_scores():
    scores = {}
    print("type finish when you're done")
    while True:
        subject = input("subject: ").strip().title()
        if subject.lower() == "finish":
            if not scores:
                print("no subject submitted")
                continue
            break
        elif len(subject) < 3:
            print("subject name cannot be under 3 characters")
        elif subject in scores:
            print("this subject already exists")
        else:
            paper_score = get_score("paper score: ")
            class_score = get_score("class score: ")
            list_scores = [paper_score, class_score,
                           (paper_score + class_score) / 2]
            scores[subject] = list_scores
    return scores


def edit_scores(first_name, last_name, scores, class_name):
    while True:
        today = datetime.now()
        print("-" * 30)
        print(f"{first_name} {last_name}'s report card")
        print(f"Date = {today.strftime('%Y/%m/%d')}")
        if not scores:
            print("no subject")
        else:
            total = 0
            for subject, number in scores.items():
                print(f"{subject}: {number[2]:.2f}")
                total += number[2]
            average = total / len(scores)
            print(f"average: {average:.2f}")
            print("1.edit\n2.add\n3.remove\n4.exit")
        try:
            user_input = input("do you want to continue? ").strip().lower()
            if user_input in ("edit", "1"):
                while True:
                    subject = input(
                        "which subject you want to change: ").strip().title()
                    try:
                        if subject not in scores:
                            raise ValueError
                    except ValueError:
                        print(
                            f"there is not any subject named {subject} in this report card")
                    else:
                        break
                while True:
                    user_decision = input("paper or class? ").strip().lower()
                    if user_decision == "paper":
                        paper_score = get_score("new paper score: ")
                        list_scores = [paper_score, scores.get(subject)[1],
                                       (paper_score + scores.get(subject)[1]) / 2]
                        scores[subject] = list_scores
                        break
                    elif user_decision == "class":
                        class_score = get_score("new class score: ")
                        list_scores = [scores.get(subject)[0], class_score,
                                       (scores.get(subject)[0] + class_score) / 2]
                        scores[subject] = list_scores
                        break
                    else:
                        print("Invalid Input")
            elif user_input in ("add", "2"):
                while True:
                    subject = input("new subject: ").strip().title()
                    try:
                        if len(subject) < 3:
                            raise ValueError(
                                "subject cannot be under 3 characters")
                        elif subject in scores:
                            raise ValueError("this subject already exists")
                    except ValueError as invalid:
                        print(invalid)
                    else:
                        break
                paper_score = get_score("paper score: ")
                class_score = get_score("class score: ")
                list_scores = [paper_score, class_score,
                               (paper_score + class_score) / 2]
                scores[subject] = list_scores
            elif user_input in ("remove", "3"):
                if len(scores) == 1:
                    print("only one subject remaining, you can't delete all")
                else:
                    while True:
                        subject = input(
                            "which subject you want to remove: ").strip().title()
                        try:
                            if subject not in scores:
                                raise ValueError
                            else:
                                del scores[subject]
                                break
                        except ValueError:
                            print(
                                f"there is not any subject named {subject}  in this report card")
            elif user_input in ("exit", "4"):
                path = Path("school") / class_name / \
                    f"{first_name} {last_name}'s report card.csv"
                path.parent.mkdir(parents=True, exist_ok=True)
                with open(path, "w",  newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["first name:", first_name])
                    writer.writerow(["last name:", last_name])
                    writer.writerow(["date:", today.strftime("%Y/%m/%d")])
                    writer.writerow([])
                    writer.writerow(["", "subject", "paper", "class", "score"])
                    index = 0
                    for subject, number in scores.items():
                        index += 1
                        writer.writerow(
                            [index, subject, number[0], number[1], f"{number[2]:.2f}"])
                    writer.writerow(["average", "score:", f"{average:.2f}"])
                print("thank you")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input")


def main(class_name):
    first_name, last_name = set_name()
    scores = set_scores()
    edit_scores(first_name, last_name, scores, class_name)


if __name__ == "__main__":
    main("other")
