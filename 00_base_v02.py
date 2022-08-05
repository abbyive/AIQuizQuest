"""

base component for multiple choice quiz
V0 - skeleton setup

author - Abby Ives
CC AVI 2022

"""

# import libraries below this line ****************************************


# all functions below this line ********************************************
def num_check(how_many_questions, low, high):
    error = "Please enter a valid whole number between 1 and 10.\n"
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
                print(error)
        except ValueError:
            print(error)


# print main routine below this line *************************************
how_many = num_check("How many questions do you want to answer? ", 0, 10)
print("You chose to answer {} questions!".format(how_many))

