from random import randint
right = 0
num = 10
for x in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10:
    print("Question " + str(x) + ".")
    num1 = randint(1,num)
    num2 = randint(1,num)
    q = "What is " + str(num1) + " times " + str(num2) + "? "
    a = int(input(q))
    numsum = numl * num2
    print("The answer is " + str(numsum) +".")
    if numsum == a:
        print("correct")
        right = right + 1
        num = num + 2
    else:
            print("wrong, try again")
            num - 2
            print(" ")
print("I asked you 10 questions. you got " + str(right) + " of them right.")
if 10 == right:
    print("Flawless, Good Job!")
else:
    if right > 9:
        print("Good job!")
    else:
        print("improve yourself.")
        
