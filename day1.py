# Part 1

def first_digit(line: str):
    digit_one = 0
    for i in line:
        try:
            digit_one = int(i)
            return digit_one
        except:
            continue

def last_digit(line: str):
    text = list(line)
    last_digit = 0
    for i in text[::-1]:
        try:
            last_digit = int(i)
            return last_digit
        except:
            continue

calibration_values = []

# with open("sample_day1.txt") as file:
#     data = file.readlines()
#     for line in data:
#         number = int(str(first_digit(line)) + str(last_digit(line)))
#         calibration_values.append(number)
#     print(sum(calibration_values))

sample = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


# Part 2

spelled_numbers = {"one": 1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def convert_spelled_nums(line: str):
    new_line = ""
    for spelling in spelled_numbers:
        if spelling == "one":
            new_line = line.replace(spelling,str(spelled_numbers[spelling]))
        else:
            holder = new_line.replace(spelling,str(spelled_numbers[spelling]))
            new_line = holder
    return new_line


for line in sample.splitlines():
    print(convert_spelled_nums(line)) 