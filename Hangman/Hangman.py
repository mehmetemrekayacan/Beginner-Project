import random
import artss
import wordss

words= wordss.word_list

word=random.choice(words)

liste=[]

for x in range(0,len(word)):
    liste+="_"

hang=7

print(f"{' '.join(liste)}")

used_letter=[]

game=True
while game:
    guess = input("Guess the word's letter:")   
    used_letter.append(guess)
    if guess in liste:
        print(f"You have already guessed {guess}")
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                liste[i]=guess
        print(f"{' '.join(liste)}")
        print(f"used words: {' , '.join(used_letter)}")
    else:
        hang-=1
        print(artss.stages[hang])
        print("you have",hang,"left.")
        print(f"{' '.join(liste)}")
        print(f"used words: {' , '.join(used_letter)}")
    if "_" not in liste:
        print(word)
        print("You win!")
        game=False
    if hang==0:
        print(word)
        print("You lose!")
        game=False
