# import libraries below this line ****************************************


# all functions below this line ********************************************
def string_check(choose_answer):
    letter_list = ("A", "B", "C", "D")
    error = "Please enter A, B, C, or D.\n"
    valid = False
    while not valid:
        # ask the user what they think the answer is
        answer = input(choose_answer).upper()
        # if the response is one of the options continue
        if answer in letter_list:
            return answer
        # if the response is invalid print an error message
        else:
            print(error)


# print main routine below this line *************************************
chosen_answer = string_check("Which answer is correct? ")
print("You chose {}!".format(chosen_answer))
