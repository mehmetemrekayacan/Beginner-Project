import random

level_easy=10
level_hard=5

def level():
    x=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if x=="easy":
        return level_easy
    elif x=="hard":
        return level_hard

def number(num,guess,turn):
    if guess<num:
        print("To low")
        return turn-1
    elif guess>num:
        print("To high")
        return turn-1
    else:
        print(f"You got it! The answer was {num}.")


def game():
    print("Welcome to the Guessing Game!")
    print("Try to find a number between 1 and 100.")
    num =random.randint(1,100)
    turn=level()
    game=True
    while game:
        print(f"You have {turn} attempts remaining to guess the number.")
        guess=int(input("Guess the number: "))
        turn=number(num,guess,turn)
        if turn==0:
            print("You lost! Your guess is over.")
            game=False

game()
