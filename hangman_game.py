import random
import hangman_stages
import word_file


print("Let's play HANGMAN!!")
print('You have only 6 Lives so try to guess the word within 6 attempts.')
print("GOOD LUCK!")

lives = 6

chosen_word = random.choice(word_file.words).lower()
print(chosen_word)

display = []

for i in range (len(chosen_word)):
    display += '_'
print(display)


game_over = False

while not game_over:
    guessed_letter = input('Guess a Letter:').lower()
    for position in range (len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        print('Now, you have only',lives,'lives remaining.')
        if lives == 0:
            game_over = True
            print("You Lose")
    if '_' not in display:
        game_over = True
        print("You Win")
    print(hangman_stages.stages[lives])
