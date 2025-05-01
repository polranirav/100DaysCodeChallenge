# Fantasy Band Name Generator By @Nirav Polara

print("Welcome to the Fantasy Band Name Generator!")
print("Let's create a unique band name for your Brand.\n")

# 2. Ask for the user's hometown
city = input("Which city did you grow up in?\n")

# 3. Ask for the user's favorite animal
animal = input("What is the name of your favorite animal?\n")

# 4. Ask for a fun or powerful word that you like Most
word = input("Give me a powerful or fun word (Ex : fire, power):\n")

# 5. Combine them into a band name
band_name = word + " " + city + " " + animal

# 6. Show the result
print("\nYour fantasy band name is:")
print(band_name)