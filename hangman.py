from random import choice

words = ['python', 'java', 'swift', 'javascript']
number_steps = 8
won = 0
lost = 0
message = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: '


def clue_replace(play_word, play_clue, input_letter):
    index_list = letter_index(play_word, input_letter)
    pc = list(play_clue)
    for el in index_list:
        pc[el] = input_letter
    return ''.join(pc)


def letter_index(play_word, input_letter):
    return [i for i in range(len(play_word)) for x in play_word.split() if x[i] == input_letter]


print("H A N G M A N")

while True:
    print()
    menu = input(message)

    if menu == 'play':
        word = choice(words)
        clue = '-' * len(word)
        word_set = frozenset(word)
        word_open_set = set()
        user_letter_set = set()

        while all([number_steps > 0, word != clue]):

            while True:
                print()
                print(clue)
                user_letter = input("Input a letter: ")

                if len(user_letter) == 1:
                    if all([user_letter.isalpha(), user_letter.islower()]):
                        break
                    else:
                        print("Please, enter a lowercase letter from the English alphabet.")
                else:
                    print("Please, input a single letter.")

            if user_letter in user_letter_set:
                print("You've already guessed this letter.")
            else:
                user_letter_set.add(user_letter)
                if user_letter not in word_set:
                    print("That letter doesn't appear in the word.")
                    number_steps -= 1
                else:
                    if user_letter not in word_open_set:
                        word_open_set.add(user_letter)
                        clue = clue_replace(word, clue, user_letter)

        else:
            if word == clue:
                won += 1
                print("""
                You guessed the word {}!
                You survived!""".format(word))
            else:
                lost += 1
                print("""
                You lost!""")

    elif menu == 'results':
        print("""You won: {} times.
        You lost: {} times.""".format(won, lost))
    elif menu == 'exit':
        break
