letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def coding(text_x,shift_x,ed_x):
    if ed_x=="encode":
        caesar=[]
        for i in text_x:
            if i!=" ":
                x=letters.index(i)+shift_x
                a=letters[x]
                caesar.append(a)
            if i==" ":
                space=[" "]
                caesar+=space
        print(f"Here is the encoded result: {''.join(caesar)}")
    elif ed_x=="decode":
        cipher=[]
        for j in text_x:
            if j!=" ":
                y=(letters.index(j)-shift_x)
                b=letters[y]
                cipher.append(b)
            if j==" ":
                space=[" "]
                cipher+=space
        print(f"Here is the decoded result: {''.join(cipher)}")

hack=True
while hack:
    ed=input("Type 'encode' to encrypt, type 'decode' to decrypt: ")

    text=input("Type your message: ")

    shift=int(input("Type the shift number:"))

    coding(text,shift,ed)

    yes_no=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if yes_no=="no":
        hack=False