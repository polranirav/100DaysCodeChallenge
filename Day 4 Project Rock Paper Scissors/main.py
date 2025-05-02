import random
from math import trunc

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Your trunc
human_selection = int(input("select the number 0 for rock, 1 for paper, 2 for scissors"))
if human_selection == 0:
    print("You chose rock: \n" + rock)
elif human_selection == 1:
    print("You chose paper: \n" + paper)
elif human_selection == 2:
    print("You chose scissors: \n" + scissors)
else:
    print("You selected wrong values please try again")

computer_selection = random.randint(0,2)
if computer_selection == 0:
    print("Computer chose rock: \n" + rock)
elif computer_selection == 1:
    print("Computer chose paper: \n" + paper)
elif computer_selection == 2:
    print("Computer chose scissors: \n" + scissors)

# now you need set up the rules of game
if human_selection == 0:
    if computer_selection == 0:
        print("no one can win please try again")
    elif computer_selection == 1:
        print("you won the game")
    elif computer_selection == 2:
        print("you lose");
elif human_selection == 1:
    if computer_selection == 0:
        print("you won")
    elif computer_selection == 1:
        print("please try again");
    elif computer_selection == 2:
        print("you lose");
elif human_selection == 2:
    if computer_selection == 0:
        print("you lose");
    elif computer_selection == 1:
        print("you won");
    elif computer_selection == 2:
        print("please try again")

# select a name of friend who pay bills
# friends = ["nirav","chitan","mitul","divyesh","jayesh","nikhil"]
# print(random.choice(friends))
# random_index = random.randint(0,len(friends)-1)
# print(friends[random_index])


# State_of_america = ["delver", "new york", "pensilyenia", "texas"]
# State_of_america.append("Nirav Polara")
# State_of_america.extend(["jayeshland","gujjuland"])
# print(State_of_america)



#
# random_heads_or_tails = random.randint(0, 1)
# if random_heads_or_tails == 0:
#     print("heads")
# else:
#     print("tails")




# random_integer = random.randint(1,100)
# print(random_integer)
# random_random = random.random() * 100
# print(random_random)