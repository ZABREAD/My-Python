import random

lives = 9
words = ['pumpkin', 'ghost', 'skeleton', 'vampire', 'wherewolf', 'candy', 'clown', 'Chocolate' , 'Grave', 'Witch', 'Potion', 'Broom', 'Trick-or-treating', 'Costume', 'Sugar', 'Decorations', 'Zombie', 'Snake', 'Spider', 'Insect']
secret_word = random.choice(words)
clue = list('_' * len(secret_word))
#heart_symbol = u'/u2764'
ghost_symbol = "👻"
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1
#This setts up the difficulty level
difficulty = input('choose a difficulty level (type 1, 2, 3 or 4):/n 1: Easy, 2: Normal, 3: Hard, 4: Extreme')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
elif difficulty == 3:
    lives = 6
elif difficulty == 4:
    lives = 3
else: 
    print("You didn't press a correct number, try again.")
    difficulty = input('choose a difficulty mode(type 1, 2, 3 or 4) 1: Easy, 2: Normal 3: Hard 4: Extreme')

while lives > 0:
    print(" ".join(clue))
    print(clue)
    print("Lives left: " + ghost_symbol * lives)
    guess = input('guess a letter or the whole word: ')

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)

    else:
        print('Incorrect. You lose a life!')
        lives = lives - 1
if guessed_word_correctly:
    print(" You Win! The secret word is: " + secret_word)
    print("you had " + str(lives) + " Lives left.")
 

else:
    print("You lost. the word was " + secret_word)


