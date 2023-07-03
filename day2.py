print("Welcome to the tip calculator!")
total = float(input("Enter the total amount? "))
PerTip = int(input("What percentage of tip do you want to give?"))
members = int(input("enter the total members?"))
tip = (PerTip * total) / 100
totalamount = (total + tip) / members
final = round(totalamount, 2)
print(f"Each person has to pay {final}")