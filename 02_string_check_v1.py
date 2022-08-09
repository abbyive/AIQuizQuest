# import libraries below this line ****************************************


# all functions below this line ********************************************


# print main routine below this line *************************************
valid = False
while not valid:
    # ask the user what they think the answer is
    response = (input("Answer: "))
    # if the response is one of the options continue
    if response in ("A", "B", "C", "D"):
        print("program continues")
    # if the response is invalid print an error message
    else:
        print("Please enter A, B, C, or D")
