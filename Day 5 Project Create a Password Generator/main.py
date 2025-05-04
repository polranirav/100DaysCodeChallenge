import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to pypassword generator")
ui_letter = int(input("how many letters would you like in your password?"))
ui_numbers = int(input("how many numbers would you like in your password?"))
ui_symbol = int(input("how many symbols would you like in your password?"))

final_letter = []
for i in range(0, ui_letter):
    final_letter += random.choice(letters)

final_number = []
for i in range(0, ui_symbol):
    final_number += random.choice(numbers)

final_symbol = []
for i in range(0, ui_symbol):
    final_symbol += random.choice(symbols)

password = (final_letter + final_number + final_symbol)
print(password)
random.shuffle(password)
print(password)
# final_password = "".join(password)
# print(final_password)

temp_password = ''
for final_password in password:
    temp_password += final_password
print(temp_password)

# student_score = [111,238,232,237,342,412,432,121,242,121,554,23,231,35,231,453,231,53,342]
# print(sum(student_score))
# print(max(student_score))

# temp = 0
# for max_number in student_score:
#     if max_number > temp:
#         temp = max_number
# print(temp)


# fruits = ['apple', 'banana', 'orange', 'strawberry']
# for fruit in fruits:
#     print(fruit)
#     print(fruits.index(fruit))