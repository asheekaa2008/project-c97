import random
print('NUMBER GUESSING GAME')
number=random.randint(1,20)
chances=0
while chances<5:
    guess=int(input("PLS ENTER NUMBER BETWEEN 1 TO 20- "))
    if guess==number:
        print("U HAVE WON CONGRATULATION")
        break
    elif guess<number:
        print("TRY A HIGHER NUMBER")
    else:
        print("TRY A LOWER NUMBER")
    chances=chances+1
if not chances<5:
    print("U LOOSE I WANT PARTY THE CORRECT NUMBER IS- ",number)

