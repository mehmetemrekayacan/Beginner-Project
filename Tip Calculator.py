print("Wellcome to Tip Calculator.")
bill=float(input("What was the total bill?\n"))
people=int(input("How many people split the bill?\n"))
per_bill=int(input("What percentage tip would you like to give? 10, 12 and 15\n"))
each_bill=(bill+(per_bill*bill)/100)/people
print(f"Each person should pay: {each_bill}")