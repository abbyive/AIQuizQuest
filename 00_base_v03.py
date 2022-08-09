"""

base component for multiple choice quiz
V3 - string check added

author - Abby Ives
CC AVI 2022

"""

# import libraries below this line ****************************************


# all functions below this line ********************************************
def num_check(how_many_questions, low, high):
    num_error = "Please enter a valid whole number between 1 and 10.\n"
    valid = False
    while not valid:
        try:
            # ask the user how many questions they want
            num_questions = int(input(how_many_questions))
            # if the number is between 1 and 10 print
            if low < num_questions <= high:
                return num_questions
            # if the number is invalid print an error message
            else:
                print(num_error)
        except ValueError:
            print(num_error)


def string_check(choose_answer):
    letter_list = ("A", "B", "C", "D")
    string_error = "Please enter A, B, C, or D.\n"
    valid = False
    while not valid:
        # ask the user what they think the answer is
        answer = input(choose_answer).upper()
        # if the response is one of the options continue
        if answer in letter_list:
            return answer
        # if the response is invalid print an error message
        else:
            print(string_error)


# print main routine below this line *************************************
how_many = num_check("How many questions do you want to answer? ", 0, 10)
print("You chose to answer {} questions!".format(how_many))
print()
print("ask question")

chosen_answer = string_check("Which answer is correct? ")
print("You chose {}!".format(chosen_answer))
