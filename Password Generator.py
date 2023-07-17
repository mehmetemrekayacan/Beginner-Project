import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

x_letters= int(input("How many letters would you like in your password?\n")) 
x_symbols = int(input("How many symbols would you like?\n"))
x_numbers = int(input("How many numbers would you like?\n")) 

password_list=[]

for x in range(1,x_letters+1):
    password_list.append(random.choice(letters))
for y in range(1,x_symbols+1):
    password_list.append(random.choice(symbols))
for z in range(1,x_numbers+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password=""
for char in password_list:
    password+=char
print(f"Your password is: {password}")
    
