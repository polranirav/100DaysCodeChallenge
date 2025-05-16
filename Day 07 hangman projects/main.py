import random
import hangman_art
import hangman_words

lives = 0
random_word = random.choice(hangman_words.word_list)
print(random_word)
random_word_length = len(random_word)

blank = ''
for i in range(random_word_length):
    blank += '_'
print(blank)

game_over = False


collect_letter = []

while not game_over:
    Guess_letter = input("Guess a letter: ").lower()
    display = ""
    for letter in random_word:
        if letter.lower() == Guess_letter:
            display += letter
            collect_letter.append(letter)
        elif letter in collect_letter:
            display += letter
        else:
            display += '_'

    if Guess_letter not in random_word:
        lives += 1
        print(hangman_art.stages[lives])
        print(f"you need to be play carefully becuase you have {7-lives} lives left")
        if lives == 7:
            game_over = True
            print("you lose")

    print(display)
    if "_" not in display:
        game_over = True
        print("you won the game")



