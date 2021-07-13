# python ---
# hangman game---
# author --- Tanish sarmah
# idea ---- https://www.geeksforgeeks.org/hangman-game-python/

import random

fruits = ['apple', 'banana', 'mango', 'strawberry', '\norange', 'grape', 'pineapple', 'apricot',
          'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

fruit = random.choice(fruits)  # generating the random fruit
dashed = "_"*len(fruit)  # making a dashed string like --  _ _ _

# will be used to change the _ into user 's letter if matching at particular index
lst = list(dashed)
chances = len(fruit) + 2
print("Welcome to the hangman game \nYou have to guess the letter of the word (HINT:the word is a fruit)")

count = 0
hint = 0

while True:
    try:
        print(f"\n{chances-count} chances left")

        for i in lst:
            print(i, end=" ")  # printing the lst in dashed way
        if count != chances:
            print("Enter 'hint' to get a hint (NOTE:don't use more than two hints otherwise you will run out of chances)")
            user = input("\nEnter the letter:\n")

        if user == "hint".lower():
            if hint == 0:
                # printing the first letter
                print("\nThe word startswith {}".format(fruit[0]))
                hint += 1
            elif hint == 1:
                # printing the last letter
                print("\nThe word endswith {} ".format(fruit[-1]))
                hint += 1
            else:
                print("No more hints!!!!!!!!!!!!")

        elif user == "q":
            quit()

        for index, item in enumerate(list(fruit)):
            if item == user:
                lst[index] = user  # changing the _ to user's letter at the index

        if lst == list(fruit):
            print(" ".join(fruit))
            print("You won the game in {} chances!!".format(count))
            break

        if count == chances:
            print("Game over !! The word was {}".format(fruit))
            break

        count += 1
    except KeyboardInterrupt:
        print("You can't quit like this ... Enter 'q' to quit")
