# number guessing game in python 3.8
# author - Tanish sarmah
# note : this proect was made in 2020 but was uploaded late .

import random
import math

# taking the range from  the user and splitting it into two variables
start, stop = input("Enter the range:\n").split()
start, stop = int(start), int(stop)

n = random.randint(start, stop)  # generating the number
form = math.log(stop-start+2, 2)  # the formula to create number of guesses


def main(n, form):
    form = int(form)
    print(
        f"Welcome to the number guessing game !!!\n\nYou have only {form} chances to guess!\n")
    while True:

        user = int(input("Guess the number:\n"))

        if n == user:
            print(f"You won in {form} attempts !!")
            break
        elif n < user:
            print("please try again the number you entered is greater")
            form -= 1
        else:
            print("please try again the number you entered is less")
            form -= 1

        if form == 0:
            print("game over!!!")
            break

        print(f"You have {form} chances remaining")


if __name__ == '__main__':
    main(n, form)
