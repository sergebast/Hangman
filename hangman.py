import random

words = ['python', 'java', 'swift', 'javascript']

computer_word = random.choice(words)

print("H A N G M A N")
user_word = input("Guess the word: ")

if user_word == computer_word:
    print("You survived!")
else:
    print("You lost!")
