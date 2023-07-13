from random import randint

again = "yes"

while again =="yes":
    number = randint(1, 6)
    print("Ok, I've thought of a number between 1 and 6.\n")
    prompt = "Make a guess: "
    answer = -1
    counter = 0

    while answer != number:
        answer = int(input(prompt))
        counter = counter + 1
        if answer < number:
            print("that's too low.\n")
        elif answer > number:
            print("that's too high.\n")

    print("That was my number. Well done!")
    print(f'\nYou took {counter} guesses')
