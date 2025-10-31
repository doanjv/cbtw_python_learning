import os
import re


def capitalizedFullName(s):
    print(len(s))
    if s and len(s) > 0 and len(s) < 100:
        names = re.split(" ", s)
        result = str.capitalize(names[0])
        for name in names[1:]:
            result = result + " " + str.capitalize(name)
        print(result)
        return
    raise "The input string size should be greater than 0 and less than 100"

if __name__ == '__main__':
    capitalizedFullName("doan nguyen van 1989okla hello World")