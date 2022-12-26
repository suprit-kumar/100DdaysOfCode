# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.
# Use of F strings.

def kbc():
    print("Lets Play!!!")
    print("-------------")
    prize_money = 10000
    questions = ["Who is the Captain of Indian Cricket Team ?", "Who won the Fifa worldcup 2022 ?",
                 "Who is the Prime Minister of India ?"]
    answers = ["rohit sharma","argentina","narendra modi"]
    correct_answers = 0
    question_count = 1
    for question in questions:
        print(f"{question_count}.{question}")
        question_count = question_count + 1
        inp = input("Type the answer of the above question:  ")
        correct_answers = correct_answers + 1 if inp.lower() in answers else correct_answers
    print("*****************-------------------------*****************")
    if correct_answers == len(questions):
        print(f"Congratulations!!! . You have won the prize money of Rs. {prize_money}/-")
    else:
        print(f"Better luck next time!!!...You have only {correct_answers} correct answers.")

kbc()