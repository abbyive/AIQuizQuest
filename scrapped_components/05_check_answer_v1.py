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


def check_answer(correct_message, incorrect_message):
    current_ans = 0
    correct_answer = ["A", "D", "B", "A", "A", "C", "B", "B", "C", "D"]

    valid = False
    while not valid:
        print(question_number[current_ans], question_list[current_ans], answer_list[current_ans],)
        chosen_answer = string_check("Answer: ")
        if chosen_answer == correct_answer[current_ans]:  # if user answer matches correct answer on list
            print(correct_message)  # print "correct"
            print()
            current_ans += 1
            return correct_answer[current_ans]
        elif chosen_answer != correct_answer[current_ans]:
            print(incorrect_message)  # if user is incorrect print "incorrect"
            print()
            current_ans += 1


def looping():
    current_question = 0
    for current_question in question_list[current_question]:  # repeat for amount of questions in the list
        correct_incorrect = check_answer("Correct!", "Incorrect! Try again.")
        print(correct_incorrect[0])
        current_question += 1
        return check_answer
    if current_question == how_many:
        print("end")


# print main routine below this line *************************************

question_number = ["Question One:\n", "Question Two:\n", "Question Three:\n", "Question Four:\n", "Question Five:\n", "Question Six:\n", "Question Seven:\n", "Question Eight:\n", "Question Nine:\n", "Question Ten:\n", ]
question_list = ["What is the capital city of Portugal?\n", "What is the name of the '~' symbol?\n", "Who played Danny in the 1978 film Grease?\n", "What is bamboo classified as?\n", "How much weight can an ant lift?\n", "How many breaths does an average human take in a day?\n", "Who said 'there's no place like home'?\n", "What is 8 ÷ 2 (2+2)?\n", "How many bones are in an adult human body?\n", "North Korea shares borders with South Korea, China, and what other country?\n"]
answer_list = ["A. Lisbon\n B. Madrid\n C. Porto\n D. Braga\n", "A. Octothorpe\n B. Curly Hyphen\n C. Asterisk\n D. Tilde\n", "A. Johnny Depp\n B. John Travolta\n C. John Mulaney\n D. John Krasinski\n", "A. Grass\n B. Tree\n C. Bush\n D. None of the above\n", "A. 50 times its body weight\n B. 40 times its body weight\n C. 50% its body weight\n D. 5 times its body weight\n", "A. 46,000\n B. 20,000\n C. 23,000\n D. 22,000\n", "A. Mickey Mouse\n B. Dorothy\n C. Hermione Granger\n D. Simba\n", "A. 1\n B. 16\n C. 8\n D. 12\n", "A. 200\n B. 203\n C. 206\n D. 208\n", "A. Japan\n B. India\n C. Mongolia\n D. Russia\n"]

how_many = num_check("How many questions do you want to answer? ", 0, 10)
print("You chose to answer {} questions!".format(how_many))
current = looping()
