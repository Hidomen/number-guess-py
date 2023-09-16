import random

tries = 0

while True :
    try :
        uplimit = int(input("What's your uplimit? (min 10) "))  #fix bug and must be bigger than 10 thing
        if uplimit >= 10 : 
            break
        else :
            print("Your uplimit must be > or = 10")
    except ValueError : 
        print("It's not an Integer")



number = random.randint(1, uplimit)

print(f"# GUESS THE NUMBER [1 - {uplimit}]")


while True:
    try :
        guess = int(input("> "))

        if guess > 0 and guess <= uplimit:
            if guess > number : 
                print("Too High")
                tries += 1
            elif guess < number :
                print("Too Low")
                tries += 1
            else :
                print("CORRECT!")
                tries += 1
                break
        else :
            print(f"Type between [1 - {uplimit}] please")

    except ValueError :
        print("It's not an Integer")

print(f"Finally you found the #{number} in {tries} tries")