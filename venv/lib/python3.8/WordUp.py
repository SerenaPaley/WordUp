# Serena Paley
# March, 2021
from getpass import getpass


def main():

    print('Welcome to Word Up')
    secret_word = getpass('Enter the secret word')
    current_list = ["_"] * len(secret_word)

    while "_" in current_list:
        print_board(current_list)
        print()
        check_letter(secret_word, guess_letter(), current_list)

    print_board(current_list)
    print()
    print("Congratulations, the word was " + secret_word)


def print_board(current_list):
    for i in current_list:
        print(i, end=" ")


def guess_letter():
    guess = input("Guess a letter ")
    return guess

def check_letter(secret_word, guess,current_list):
    k = 0;
    while k < len(secret_word):
        if guess == secret_word[k]:
            current_list[k] = guess
            k = k + 1
        else:
            k = k + 1

    if guess not in secret_word:
        print (guess + " is not in the secret word")


if __name__ == "__main__":
    main()