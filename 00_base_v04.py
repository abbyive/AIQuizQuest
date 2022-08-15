"""

base component for multiple choice quiz
V4 - questions and answers added

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
how_many = num_check("How many questions do you want to answer? ", 0, 10)
print("You chose to answer {} questions!".format(how_many))

question_number = ["Question One:\n", "Question Two:\n", "Question Three:\n", "Question Four:\n", "Question Five:\n", "Question Six:\n", "Question Seven:\n", "Question Eight:\n", "Question Nine:\n", "Question Ten:\n", ]
question_list = ["What is the capital city of Portugal?\n", "What is the name of the '~' symbol?\n", "Who played Danny in the 1978 film Grease?\n", "What is bamboo classified as?\n", "How much weight can an ant lift?\n", "How many breaths does an average human take in a day?\n", "Who said 'there's no place like home'?\n", "What is 8 ÷ 2 (2+2)?\n", "How many bones are in an adult human body?\n", "North Korea shares borders with South Korea, China, and what other country?\n"]
answer_list = ["A. Lisbon\n B. Madrid\n C. Porto\n D. Braga\n", "A. Octothorpe\n B. Curly Hyphen\n C. Asterisk\n D. Tilde\n", "A. Johnny Depp\n B. John Travolta\n C. John Mulaney\n D. John Krasinski\n", "A. Grass\n B. Tree\n C. Bush\n D. None of the above\n", "A. 50 times its body weight\n B. 40 times its body weight\n C. 50% its body weight\n D. 5 times its body weight\n", "A. 46,000\n B. 20,000\n C. 23,000\n D. 22,000\n", "A. Mickey Mouse\n B. Dorothy\n C. Hermione Granger\n D. Simba\n", "A. 1\n B. 16\n C. 8\n D. 12\n", "A. 200\n B. 203\n C. 206\n D. 208\n", "A. Japan\n B. India\n C. Mongolia\n D. Russia\n"]
current = 0

for loop_num in question_list:  # repeat for amount of questions in the list
    print(question_number[current], question_list[current], answer_list[current],)
    chosen_answer = string_check("Answer: ")
    print("You chose {}!\n".format(chosen_answer))
    current = current + 1
    if current >= how_many:
        break
