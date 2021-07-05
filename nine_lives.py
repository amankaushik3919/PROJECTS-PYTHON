import random

lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'planes']
secret_word = random.choice(words)
r = list(secret_word)
clue = list('?'*len(secret_word))
heart = u'\u2764'
guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1


while lives > 0:
    print(clue)
    print('Lives Left: ' + heart*lives)
    guess = input("Guess a letter or the whole word: ")
    if guess == secret_word:
        guessed_word_correctly = True
        break
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
        if clue == r:
            print("You Won!!!")
            print(secret_word)
            break
    else:
        print("Incorrect, You lose a life")
        lives -= 1
