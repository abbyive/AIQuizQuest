# import libraries below this line ****************************************


# all functions below this line ********************************************


# print main routine below this line *************************************
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
            print("Correct! The answer was {}!\nScore: {}".format(chosen_answer, score))
        else:
            print("Incorrect. Try again!\nScore: {}".format(score))
    except TypeError:
        print("error")
