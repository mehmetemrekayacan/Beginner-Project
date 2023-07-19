import random

cards=[2,3,4,5,6,7,8,9,10,10,10,10,"A"]

your_card=[]
dealer_card=[]

y=0
def you():
    global y
    x=random.choice(cards)
    your_card.append(x)
    if x=="A":
        print(f"Your current cards: {your_card}")
        a=int(input("Do you want an Ace as 1 or 11: "))
        y+=a
    else:
        y+=x

d=0
def dealer():
    global d
    x=random.choice(cards)
    dealer_card.append(x)
    if x=="A":
        if d>=11:
            x=1
            d+=x
        elif d<=10:
            x=11
            d+=x
    else:
        d+=x

you()
you()
dealer()
dealer()

game=True
while game:
    print(f"Your cards: {your_card}, current score is {y}")
    print(f"Dealer first card {dealer_card[0]}")
    y_n=input("Type 'y' to another card, type 'n' to pass: ")
    if y_n=="n":
        d_game=True
        while d_game:
            if d>=17:
                d_game=False
            else:
                dealer()
            
        print(f"Dealer cards {dealer_card}")
        print(f"Dealer current score is {d}")
        game=False
    if y_n=="y":
        if y<21:
            you()
        if y>=21:
            print(f"Your cards: {your_card}, current score is {y}")
            game=False

if y<=21 and d<=21:
    if y>d:
        print("\nYou win!")
    elif y==d:
        print("\nIt's draw!")
    elif y<d:
        print('\nThe Dealers wins!')
if y>21:
    print('\nBust! You lose!')
if d>21:
    print('\nDealers Bust. You Win!')



