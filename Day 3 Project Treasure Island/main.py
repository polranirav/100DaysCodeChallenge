print('''
******************************************************
                        _
                       //
                      //
             _.-````'//_
         ,-'`       //  `'-.,_
 /)     (\         //        '``-.
( ( .,-') )       //             ``
 \)'   (_/       `#'              !!
  |       /)     ###   '          !!!
  `\    X'       ###  '     !    !!!!
    !      _/! , !## !  ! !  !   !!!
     \Y,   |!!!  ! #! !!  !! !!!!!!!
       `!!! !!!! !!# )!!!!!!!!!!!!!
        !!  ! ! \( \(  !!!|/!  |/!
               /_(/#(    /_(  /_(
                 %%%%
                %%%%%%%
                 %%%%%%%
                   %%%%
                      %%
********************************************
''')
print("Welcome to treasure hunt island")
print("your mission is find treasure island")

Answer1 = input("you are at a cross road. Where do you want to go? Type 'left' or 'right'' ")

if Answer1 == "left":
    print("you are come to the lack. There is an island in the middle of the lake")
    answer2 = input('Type "wait" to wait for the boat. Type "swim" to swim across the lake ')

    if answer2 == "wait":
        print("you are waiting for the boat")
        answer3 = input("Which door you would like to go? Type 'red' or 'blue' of 'yellow' ")
        if answer3 == "red":
            print("You enter in fire room!!!!!!game over")
        elif answer3 == "blue":
            print("you enter in the beasts room!!!!!!game over")
        elif answer3 == "yellow":
            print("You get treasure!!!!!!You won the game")
        else:
            print("you selected wrong colors please try again.....")
    elif answer2 == "swim":
        print("you are swimming and your are die")
        print("game over")
    else:
        print("game over")
elif Answer1 == "right":
    print("game over")

else:
    print("select the right option")

# Get input from user
# number = int(input("Enter a number to check if it's prime: "))
# # Check if the number is prime
# if number <= 1:
#     print(f"{number} is not a prime number")
# else:
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")





    #  Even & odd number calculation
# print("check the number is even or odd")
# number = int(input("Enter the number"))
# if number % 2 == 0:
#     print(f"The number {number} is even")
# else:
#     print(f"The number {number} is odd")

# print("it is decide whether you are sit in rollercoaster or not?")
# height = input("enter the height")
# height_int = int(height)
# if height_int > 120:
#     print("you are sit in roller coaster")
#     age = int(input("enter the age"))
#     if age <= 10:
#         bill = 5
#         print("Your ticket should be 5$")
#     elif age <= 18:
#         bill = 10
#         print("Your ticket should be 10$")
#     else:
#         bill = 15
#         print("Your ticket should be 15$")
#     capture = input("Do you want to capture photos or not? Y for Yes or N for no")
#     if capture == "Y":
#         total_bill = bill + 3
#         print(f"your total bill {total_bill}")
#     else:
#         print(f"Your total bill is {bill}")
# else:
#     print("you are not sit in roller coaster")

