#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program displays the middle grade of each mark level

import string


def find_middle(level_mark):
    # Finds middle grade

    # Process and output
    if level_mark == "4+":
        grade = 97
    elif level_mark == "4":
        grade = 90
    elif level_mark == "4-":
        grade = 83
    elif level_mark == "3+":
        grade = 78
    elif level_mark == "3":
        grade = 75
    elif level_mark == "3-":
        grade = 71
    elif level_mark == "2+":
        grade = 68
    elif level_mark == "2":
        grade = 65
    elif level_mark == "2-":
        grade = 61
    elif level_mark == "1+":
        grade = 58
    elif level_mark == "1":
        grade = 55
    elif level_mark == "1-":
        grade = 51
    elif level_mark == "R":
        grade = 25
    else:
        grade = -1

    return grade


def main():
    # This function calls find_middle

    # Input
    level_mark = str(
        input("Enter the grade level you wanted converted to a percentage: ")
    )

    # Function call
    percentage = find_middle(level_mark)

    # Process and output
    if percentage == -1:
        print("Invalid mark")
    else:
        print("The middle percentage of {0} is {1}%.".format(
            level_mark, percentage
        ))
    print("\nDone.")


if __name__ == "__main__":
    main()
