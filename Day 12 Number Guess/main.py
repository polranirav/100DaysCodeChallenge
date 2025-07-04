from random import randint
easy_level_turn = 10
hard_level_turn = 5

def check_answer(user_guide, actual_answer, turns):
    if user_guide > actual_answer:
        print("too high")
        return turns - 1
    if user_guide < actual_answer:
        print("too low")
        return turns - 1
    else:
        print(f"you are right the answer was {actual_answer}")

def set_difficulty():
    level = input("enter your difficulty: 'easy' or 'hard'")
    if level == "easy":
        return easy_level_turn
    else:
        return hard_level_turn

def game():
    print("welcome to the number guessing game")
    print("i am thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"the correct answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"you have {turns} number of guesses left")
        guess = int(input("guess the number: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(" you are running out of guess' sorry, you lose the game")
            return
        elif guess != answer:
            print("guess again")
    return

game()



