<<<<<<< HEAD
from random import randint

top = 1000
 
again = "yes"

while again =="yes":
    number = randint(1, top)
    print(f"Ok, I've thought of a number between 1 and {top}.\n")
    prompt = "Make a guess: "
    answer = 896
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
    
    again = input("Would you like another game? ")

print("Ok. Bye!")
=======
from random import randint

top = 1000
 
again = "yes"

while again =="yes":
    number = randint(1, top)
    print(f"Ok, I've thought of a number between 1 and {top}.\n")
    prompt = "Make a guess: "
    answer = 896
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
    
    again = input("Would you like another game? ")

print("Ok. Bye!")
>>>>>>> 9c7266a268de4418e8eac1a9e4edeef408be8425
