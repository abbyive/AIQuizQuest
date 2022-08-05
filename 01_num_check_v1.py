# import libraries below this line ****************************************


# all functions below this line ********************************************


# print main routine below this line *************************************

try:
    # ask the user how many questions they want
    response = int(input("How many questions do you want to answer? "))
    # if the number is between 1 and 10 print
    if 0 < response <= 10:
        print("You will answer {} questions!".format(response))
    # if the number is invalid print an error message
    else:
        print("Please enter a valid number between 1 and 10.")
except ValueError:
    print("Please enter a valid number between 1 and 10.")

