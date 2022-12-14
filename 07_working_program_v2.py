"""

V7 -final version of working program

author - Abby Ives
CC AVI 2022

"""

# import libraries below this line ****************************************
import time


# all functions below this line ********************************************
# yes_no function to check that user inputs either yes or no
# parameter is the yes/no question given to the user
# returns the user's response
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please enter either 'Yes' or 'No'.")


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


# function text_decor to add symbols for decoration around statements
# parameters are the text that needs to be decorated and the symbol it is decorated with
# this function returns an empty string
def text_decor(text, symbol):
    text = "{}".format(text)
    up_down = symbol * len(text)
    print(up_down)
    print(text)
    print(up_down)
    return ""


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
    print()
    valid = False
    while not valid:
        if current != question_amount:  # repeat for amount of questions the user input
            print(num_question[current], list_question[current], list_answer[current])
            chosen_answer = string_check("Answer: ").upper()
            if chosen_answer == correct_list[current]:  # if user answer matches correct answer on list
                current += 1
                score += 1
                print()
                print(text_decor(correct_message, "???"), "\nScore: ", score)  # print decorated correct message
            else:
                print()
                print(text_decor(incorrect_message, "???"), "\nThe correct answer was:", correct_list[current], "\nScore: ",
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
                 "Who said 'there's no place like home'?\n", "What is 8 ?? 2 (2+2)?\n",
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
# variables holding instructions in 4 different sections
instructions1 = "Alright, here's the rundown:"
instructions2 = "Step One: Pick how many questions you want to answer.\n" \
                "(This must be between 1 and 10.)"
instructions3 = "Step Two: You will be given a question, with answer options 'A', 'B', 'C', and 'D'. \n"
instructions4 = "Step Three: Pick the answer you think is correct."
# begin 'script' - game-show-esque
text_decor("Welcome to the General Knowledge Quiz!", "???")  # print decorated welcome
time.sleep(1)  # pause program for 1 second
print()
print("Made by quiz-master extraordinaire...")
time.sleep(1)
print()
text_decor("Abby!", "???")  # print decorated name
print()
time.sleep(2)
user_name = input("What is your name? ")  # ask user's name
played_before = yes_no("Hi, {}! Have you played this quiz before? ".format(user_name))
if played_before == "no":
    # if they haven't played before print the instructions
    print()
    print(instructions1)
    print()
    print(instructions2)
    print()
    print(instructions3)
    print(instructions4)
    print()
    user_ready = yes_no("Understood? ")
    print()
    if user_ready == "no":
        # if they do not understand print instructions again
        print("Hey, that's fine. I'll just tell you again.")
        print()
        print(instructions2)
        print()
        print(instructions3)
        print(instructions4)
        print()
        user_ready = yes_no("Understood? ")
        print()
print("Cool beans! Now lets get on with it.")
print()
time.sleep(1)
# central command - calls play_quiz to allow program to run - assigns parameters to the variables above
final_score = play_quiz(question_number, question_list, answer_list, correct_answer, "Correct", "Incorrect!")
# print user final score
text_decor("Your final score is {}!".format(final_score), "???")
play_again = yes_no("Well done, {}! Would you like to play again? ".format(user_name))  # ask if user wants to play again
if play_again == "yes":
    final_score = play_quiz(question_number, question_list, answer_list, correct_answer, "Correct!", "Incorrect!")  # play again
text_decor("Thanks for playing!", "???")  # print decorated goodbye
