# Author         : Cheri Stevens
# Student number : ###########

# This program is designed to be a multiple maths quiz

# Creating the functions

# importing random
import random

def menu():
    username = input("******* Welcome to this maths quiz!! *******\n"
            "       Each question is Randomly Generated\n"
          "       There are three levels of difficulty to choose from.\n"+"\nWhat is your name? ")


    print("Hi there "+username+",welcome to the maths quiz.")
    print(" DIFFICULTY LEVEL:\n"
    "E = EASY\n"
    "M = MEDIUM\n"
    "D = DIFFICULT\n")

def get_difficulty():

    choice = ""

    while choice not in ("M", "m", "E", "e", "D", "d"):
        choice = input("PLEASE ENTER YOUR DIFFICULTY LEVEL: ")

        if choice == "E" or choice == "e":
            print("**** YOU HAVE SELECTED EASY MODE****")

        elif choice == "M" or choice == "m":
            print("**** YOU HAVE SELECTED MEDIUM MODE****")

        elif choice == "D" or choice == "d":
            print("**** YOU HAVE SELECTED DIFFICULT MODE ****")
        return choice.upper()


def run_quiz(difficulty):
    print("** LETS BEGIN **")

# Creating the counter along with the loop playing your difficulty level

    counter = 1
    score = 0
    while counter <= 15:
        print("Question "+ str(counter) + ":")
        if difficulty == "E":
            score += easy_question()
        elif difficulty == "M":
            score += medium_question()
        else:
            score += hard_question()
        counter += 1
    return score

# The question functions with random questions and answers

def easy_question():

    a = random.randint(1, 50)
    b = random.randint(10, 60)

    print("What is the sum of "+str(a)+" and " +str(b))

    answer_wrong_one = random.randint(11, 110)
    answer_correct = a + b
    answer_wrong_two = random.randint(11, 110)

    answer_list = [answer_wrong_one, answer_correct, answer_wrong_two]
    random.shuffle(answer_list)


    print("***PICK AN ANSWER***\n"
          "1. "+ str(answer_list[0])+"\n"
          "2. "+ str(answer_list[1])+"\n"
          "3. "+ str(answer_list[2]))

    user_choice = input("Choose the corresponding number with the correct answer: ")
    user_choice = int(user_choice) - 1

    if answer_correct == answer_list[user_choice]:
        print("\n*** CORRECT ***\n")
        return 1
    else:
        print("\n*** INCORRECT ***\n")
        return 0





def medium_question():
    a = random.randint(2, 15)
    b = random.randint(5, 20)

    print("What is " + str(a) + " times " + str(b))

    answer_wrong_one = random.randint(10, 300)
    answer_correct = a * b
    answer_wrong_two = random.randint(10, 300)

    answer_list = [answer_wrong_one, answer_correct, answer_wrong_two]
    random.shuffle(answer_list)


    print("***PICK AN ANSWER***\n"
          "1. " + str(answer_list[0]) + "\n"
          "2. " + str(answer_list[1]) + "\n"
          "3. " + str(answer_list[2]))



    user_choice = input("Choose the corresponding number with the correct answer: ")
    user_choice = int(user_choice) - 1

    if answer_correct == answer_list[user_choice]:
        print("\n*** CORRECT ***\n")
        return 3
    else:
        print("\n*** INCORRECT ***\n")
        return 0



def hard_question():
    a = random.randint(2, 21)
    b = random.randint(5, 30)
    c = random.randint(3, 36)

    print("What is " + str(a) + " times " + str(b)+ " plus "+ str(c))

    answer_wrong_one = random.randint(13, 666)
    answer_correct = a * b + c
    answer_wrong_two = random.randint(13, 666)

    answer_list = [answer_wrong_one, answer_correct, answer_wrong_two]
    random.shuffle(answer_list)

    print("***PICK AN ANSWER***\n"
          "1. " + str(answer_list[0]) + "\n"
          "2. " + str(answer_list[1]) + "\n"
          "3. " + str(answer_list[2]))

    user_choice = input("Choose the corresponding number with the correct answer: ")
    user_choice = int(user_choice) - 1

    if answer_correct == answer_list[user_choice]:
        print("\n*** CORRECT ***\n")
        return 6
    else:
        print("\n*** INCORRECT ***\n")
        return 0


def show_score(score):
    print("*** YOU GOT A SCORE OF " + str(score) + " ***")



playing = True
while (playing):
    menu()
    difficulty = get_difficulty()
    score = run_quiz(difficulty)
    show_score(score)
