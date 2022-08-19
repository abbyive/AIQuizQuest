"""

base component for multiple choice quiz
V5 - play_quiz central function and scoring

author - Abby Ives
CC AVI 2022

"""

# import libraries below this line ****************************************


# all functions below this line ********************************************
# num_check function to check that user inputs a number between 1-10
# parameters are the user prompt for number of questions, a  minimum value of 1, and maximum value of 10
# returns the user's valid input
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


# string_check function to check that user inputs a valid answer of A, B, C, or D
# parameters are the user prompt for an answer
# returns the user's valid answer of A, B, C, or D
def string_check(choose_answer):
    letter_list = ("A", "B", "C", "D")
    string_error = "Please enter A, B, C, or D.\n"
    valid = False
    while not valid:
        # ask the user what they think the answer is
        chosen_answer = input(choose_answer).upper()
        # if the response is one of the options continue
        if chosen_answer in letter_list:
            return chosen_answer
        # if the response is invalid print an error message
        else:
            print(string_error)


# central function play_quiz to allow the program to run
# checks if user answer is correct, add to score, and loop for user input amount in num_check
# parameters are the list of question numbers, the list of questions, the list of answer choices, the list of correct answers,
# a 'correct' output, and an 'incorrect' output
# returns the user's final score
def play_quiz(num_question, list_question, list_answer, correct_list, correct_message, incorrect_message):
    score = 0
    current = 0
    question_amount = num_check("How many questions do you want to answer? ", 0, 10)
    print("You chose to answer {} questions!".format(question_amount))
    valid = False
    while not valid:
        if current != question_amount:  # repeat for amount of questions the user input
            print(num_question[current], list_question[current], list_answer[current])
            chosen_answer = string_check("Answer: ").upper()
            if chosen_answer == correct_list[current]:  # if user answer matches correct answer on list
                current += 1
                score += 1
                print(correct_message, "\nScore: ", score)  # print "correct"
                print()

            else:
                print(incorrect_message, correct_list[current], "\nScore: ",
                      score)  # if user is incorrect print "incorrect"
                print()
                current += 1
        else:
            break
    return score


# print main routine below this line *************************************
# variables to hold lists for questions, answer choices, and the correct answers
question_number = ["Question One:\n", "Question Two:\n", "Question Three:\n", "Question Four:\n", "Question Five:\n",
                   "Question Six:\n", "Question Seven:\n", "Question Eight:\n", "Question Nine:\n", "Question Ten:\n", ]
question_list = ["What is the capital city of Portugal?\n", "What is the name of the '~' symbol?\n",
                 "Who played Danny in the 1978 film Grease?\n", "What is bamboo classified as?\n",
                 "How much weight can an ant lift?\n", "How many breaths does an average human take in a day?\n",
                 "Who said 'there's no place like home'?\n", "What is 8 ÷ 2 (2+2)?\n",
                 "How many bones are in an adult human body?\n",
                 "North Korea shares borders with South Korea, China, and what other country?\n"]
answer_list = ["A. Lisbon\n B. Madrid\n C. Porto\n D. Braga\n",
               "A. Octothorpe\n B. Curly Hyphen\n C. Asterisk\n D. Tilde\n",
               "A. Johnny Depp\n B. John Travolta\n C. John Mulaney\n D. John Krasinski\n",
               "A. Grass\n B. Tree\n C. Bush\n D. None of the above\n",
               "A. 50 times its body weight\n B. 40 times its body weight\n C. 50% its body weight\n D. 5 times its body weight\n",
               "A. 46,000\n B. 20,000\n C. 23,000\n D. 22,000\n",
               "A. Mickey Mouse\n B. Dorothy\n C. Hermione Granger\n D. Simba\n", "A. 1\n B. 16\n C. 8\n D. 12\n",
               "A. 200\n B. 203\n C. 206\n D. 208\n", "A. Japan\n B. India\n C. Mongolia\n D. Russia\n"]
correct_answer = ["A", "D", "B", "A", "A", "C", "B", "B", "C", "D"]
# central command - calls play_quiz to allow program to run - assigns parameters to the variables above
final_score = play_quiz(question_number, question_list, answer_list, correct_answer, "Correct!",
                        "Incorrect! The answer was:")
# print user final score
print("Your final score is ", final_score)
