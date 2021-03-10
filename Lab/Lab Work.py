### price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise they need to put down 20%.
### print the down payment

"""hp= 1000000
goodcredit=True
if goodcredit:
    downpayment= 0.1*hp
else:
    downpayment= 0.2*hp
print(f'downpayment: ${downpayment}')"""

### If temperature is grater than 30, its a hot day other wise if it's less than 10; it's a cold day; otherwise, it's neither hot or cold.

"""tempval=float(input('Enter the current temperature in celsius:'))
if tempval > 30:
    print("It's a hot day!")
elif tempval < 10:
    print("It's a cold day!")
else:
    print("Its a moderate day!")"""

### If name is less than 3 character long name must be at east 3 characters otherwise if it's more than 50 characters name must be maximum
### of 50 characters otherwise name looks good!

"""username = input("Enter the name:")
if len(username) < 3:
    print("Name must be atleast 3 characters")
elif len(username) > 50:
    print("Name must be less than 50 characters")
else:
    print("Name looks Good!!")"""

### Weight Converter
"""weight= int(input("Enter the weight of the person:"))
unit=input("(L)bs or (k)g:")
if unit.upper() == "L":
    converted_Lbs = weight * 0.45
    print(f"The person weight is {converted_Lbs} kilos")
elif unit.upper() == "k":
    converted_Lbs = weight * 0.45
    print(f"The person weight is {converted_Lbs} pounds")
else:
    print(f"Please enter the appropriate character as k fo kg or l for lbs!!")"""

