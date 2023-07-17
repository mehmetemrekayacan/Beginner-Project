
first_number=float(input("What is the first number?: "))

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def divide(x,y):
    return x/y

result = 0
cal=True
while cal:
    print("+\n-\n*\n/")
    operator=input("Pick a operation: ")
    next_number=float(input("What is the next number?: "))
    if operator=="+":
        result = addition(first_number,next_number)
    elif operator=="-":
        result = subtraction(first_number,next_number)
    elif operator=="*":
        result = multiplication(first_number,next_number)
    elif operator=="/":
            if first_number==0 or next_number==0:
                print ("Cannot Divide by zero")
                break
            else:
                result = divide(float(first_number), float(next_number))
    print(f"{first_number}{operator}{next_number}={result}")
    y_n=input(f"Type 'y' to continue calculating with {result}, or type 'n' to finish calculation: ")
    if y_n=="n":
        cal=False
    else:
        first_number=result


            


