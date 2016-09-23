"""
Typing Game for Kids
Authur: Mandy H.
Date: 17 June 2016
"""

import timeit

def open_file(filename):
    input_file = open(filename)
    content = input_file.read()
    input_file.close()
    new_content = clear_space(content)
    print(new_content)
    content = list(new_content)
    return new_content

def clear_space(content):
    content = content.replace("\n", " ")
    new_content = ""
    for index in range(len(content)-1):
        if index != -1:
            if content[index] == " " and content[index + 1] == " ":
                new_content += ""
            else:
                new_content += content[index]
    if content[-1] != " ":
        new_content += content[-1]
    return new_content

def user_begin():
    print("=" * 30)
    input("Press Enter to begin. Then timer will begin.")

def user_input():
    user_input = input()
    input_list = list(user_input)
    return input_list

def input_length(content):
    total_length = len(content)
    return total_length

def checking_correct(content, user_input):
    correct = 0
    if len(content) <= len(user_input):
        for index in range(len(content)):
            if content[index] == user_input[index]:
                correct += 1
        print()
        print("*" * 30)
    else:
        content = content[: len(user_input)]
        for index in range(len(content)):
            if content[index] == user_input[index]:
                correct += 1
        print()
        print("*" * 30)
        print("You input is shorter than the provided paragraph.")
    return correct

def checking_complete(content, user_input):
    complete = input_length(content) - (input_length(content) - len(user_input))
    return complete

def calculation_correctness(correct, complete):
    correctness = round(correct / complete * 100, 2)
    return correctness

def calculation_completeness(complete, content):
    completeness = round(complete / input_length(content) * 100, 2)
    return completeness

def speed(time_used, content):
    speed = round(input_length(content) / time_used, 2)
    return speed

def grade(correctness, completeness, speed):
    if correctness >= 90 and completeness >= 90 and speed >= 3:
        print ("Well done! :D")
    elif 60 <= correctness < 90 and 60 <= completeness < 90 and 2 <= speed <3:
        print ("Pretty good!")
    else:
        print ("Work harder :)")
    print("=" * 30)
    
def print_result(complete, correct, correctness, completeness, typing_speed):
    print("In this game, you have typed", complete, "characters.")
    print("Among which,", correct, "characters are correctly typed.")
    print("You have completed ", completeness, "% of the game.", sep = "")
    print("Your correctness rate is: ", correctness, "%", sep = "")
    print("Your typing speed is: ", typing_speed, "characters per second.")


def main():
    print("Please follow the paragraph to type.")
    print("=" * 30)
    source_list = open_file("source.txt")
    
    begin = user_begin()
    start = timeit.default_timer()
    typing = user_input()
    end = timeit.default_timer()
    time_used = round(end - start)
    correct = checking_correct(source_list, typing)
    complete = checking_complete(source_list, typing)
    correctness = calculation_correctness(correct, complete)
    completeness = calculation_completeness(complete, source_list)
    typing_speed = speed(time_used, source_list)
    print_result(complete, correct, correctness, completeness, typing_speed)
    print("Time used:", time_used, "seconds")
    grade(correctness, completeness, typing_speed)

main()
    
    

                    
