from random import choice

words = ['python', 'java', 'swift', 'javascript']

computer_word = choice(words)
clue = computer_word[:3] + ('-' * (len(computer_word) - 3))

print("H A N G M A N")

user_word = input("Guess the word {}: ".format(clue))

if user_word == computer_word:
    print("You survived!")
else:
    print("You lost!")
