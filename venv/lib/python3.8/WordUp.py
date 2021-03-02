# Serena Paley
# March, 2021
from getpass import getpass


def main():

    print('Welcome to Word Up')
    secret_word = getpass('Enter the secret word')
    current_list = ["_"] * len(secret_word)
    letter_bank = []
    guess = ""

    while "_" in current_list:
        print_board(current_list)
        get_letter(guess, letter_bank)
        print_letter_bank(letter_bank)
        print()
        guess = input("Guess a letter ")
        check_letter(secret_word, guess, current_list)

    print_board(current_list)
    print()
    print("Congratulations, the word was " + secret_word)


def print_board(current_list):
    for i in current_list:
        print(i, end=" ")


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


def get_letter(guess, letter_bank):
    letter_bank.append(guess)


def print_letter_bank(letter_bank):
    print()
    print("Used Letters:" ,end="")
    for j in letter_bank:
        print (j,  end=" ")


if __name__ == "__main__":
    main()