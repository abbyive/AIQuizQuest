# import libraries below this line ****************************************


# all functions below this line ********************************************


# print main routine below this line *************************************
question_number = ["Question One:\n", "Question Two:\n", "Question Three:\n", "Question Four:\n", "Question Five:\n", "Question Six:\n", "Question Seven:\n", "Question Eight:\n", "Question Nine:\n", "Question Ten:\n", ]
question_list = ["What is the capital city of Portugal?\n", "What is the name of the '~' symbol?\n", "Who played Danny in the 1978 film Grease?\n", "What is bamboo classified as?\n", "How much weight can an ant lift?\n", "How many breaths does an average human take in a day?\n", "Who said 'there's no place like home'?\n", "What is 8 ÷ 2 (2+2)?\n", "How many bones are in an adult human body?\n", "North Korea shares borders with South Korea, China, and what other country?\n"]
answer_list = ["A. Lisbon\n B. Madrid\n C. Porto\n D. Braga\n", "A. Octothorpe\n B. Curly Hyphen\n C. Asterisk\n D. Tilde\n", "A. Johnny Depp\n B. John Travolta\n C. John Mulaney\n D. John Krasinski\n", "A. Grass\n B. Tree\n C. Bush\n D. None of the above\n", "A. 50 times its body weight\n B. 40 times its body weight\n C. 50% its body weight\n D. 5 times its body weight\n", "A. 46,000\n B. 20,000\n C. 23,000\n D. 22,000\n", "A. Mickey Mouse\n B. Dorothy\n C. Hermione Granger\n D. Simba\n", "A. 1\n B. 16\n C. 8\n D. 12\n", "A. 200\n B. 203\n C. 206\n D. 208\n", "A. Japan\n B. India\n C. Mongolia\n D. Russia\n"]

for num_questions in range(len(question_number)):  # repeat for amount of questions in the list
    print(question_number[num_questions], question_list[num_questions], answer_list[num_questions], "\nAnswer:\n")
    # insert 02_string_check - answer = input(choose_answer) to allow user to answer each question
