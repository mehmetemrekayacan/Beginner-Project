import random

choice_you=input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n")

choice_AI=random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



image=[rock,paper,scissors]


if choice_you=="0":
    print("Your choice is Rock.")
    print(image[int(choice_you)])
    if choice_AI==0:
        print("AI choice is Rock.")
        print(image[choice_AI])
        print("Draw!")
    elif choice_AI==1:
        print("AI choice is Paper.")
        print(image[choice_AI])
        print("You lose! AI wins the game...")
    elif choice_AI==2:
        print("AI choice is Scissors.")
        print(image[choice_AI])
        print("Congratulations!! You win this round of rock-paper-scissors..")
elif choice_you=="1":
    print("Your choice is Paper.")
    print(image[int(choice_you)])
    if choice_AI==0:
        print("AI choice is Rock.")
        print(image[choice_AI])
        print("Congratulations!! You win this round of rock-paper-scissors..")
    elif choice_AI==1:
        print("AI choice is Paper.")
        print(image[choice_AI])
        print("Draw!")
    elif choice_AI==2:
        print("AI choice is Scissors.")
        print(image[choice_AI])
        print("You lose! AI wins the game...")
elif choice_you=="2":
    print("Your choice is Scissors.")
    print(image[int(choice_you)])
    if choice_AI==0:
        print("AI choice is Rock.")
        print(image[choice_AI])
        print("You lose! AI wins the game...")
    elif choice_AI==1:
        print("AI choice is Paper.")
        print(image[choice_AI])
        print("Congratulations!! You win this round of rock-paper-scissors..")
    elif choice_AI==2:
        print("AI choice is Scissors.")
        print(image[choice_AI])
        print("Draw!")
