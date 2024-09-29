import random

guesses = 0
random_number = random.randrange(1,100)
# print(random_number)

while True:
    number = int(input("Guess the number: "))

    guesses = guesses + 1

    if guesses == 10:
        print("You lost the game maximum limit 10 guesses extends.")
        break

    if number > random_number:
        print("choose smaller.")
    elif number < random_number:
        print("choose greater.")
    elif number == random_number:
        print(f"congratulations! you guess the right number in {guesses} guesses.")
        break


