import random
import datas

game_data=datas.data

def choice_a():
    a=random.choice(game_data)
    a_list=[]
    for i in a.values():
        a_list.append(str(i))
    x=a_list[1]
    a_list.pop(1)
    print("\nCompare A: ",", ".join(a_list))
    return x


def choice_b():
    b=random.choice(game_data)
    b_list=[]
    for i in b.values():
        b_list.append(str(i))
    y=b_list[1]
    b_list.pop(1)
    print("Compare B: ",", ".join(b_list))
    return y

score=0
game=True
while game:
    a_num = int(choice_a())
    b_num = int(choice_b())
    a_b=input("\nWho has more followers? Tyoe 'A' or 'B': ")
    if a_b=="A" or a_b=="a":
        if a_num>b_num:
            score+=1
            print(f"\nYou're right! Current score: {score}")
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
            game=False

    elif a_b=="B" or a_b=="b":
        if b_num>a_num:
            score+=1
            print(f"\nYou're right! Current score: {score}")
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
            game=False
    else:
        print("\nDraw!")