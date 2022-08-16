# import libraries below this line ****************************************


# all functions below this line ********************************************
def scoring(correct_message, incorrect_message):
    score = 0
    current = 0
    correct_answer = ["A", "D", "B", "A", "A", "C", "B", "B", "C", "D"]
    valid = False
    while not valid:
        try:
            chosen_answer = input("Answer: ").upper()
            if chosen_answer == correct_answer[current]:
                score = score + 1
                current = current + 1
                print(correct_message, "\nScore:", score)
                print()
                return chosen_answer
            else:
                print(incorrect_message, "\nScore:", score)
                print()
        except TypeError:
            print("error")


# print main routine below this line *************************************
correct_incorrect = scoring("Correct!", "Incorrect! Try again.")
