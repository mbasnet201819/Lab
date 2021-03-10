### WAP to convert sec to day, hour, minutes and seconds

second = float(input("Enter the time in seconds: "))

day= (((second//60)//60)//24)
print(f"Total day for given seconds: {day}")

hour= ((second//60)//60)
print(f"Total hours for given seconds: {hour}")

minute = (second)//60
print(f"Total minute for given seconds: {minute}")