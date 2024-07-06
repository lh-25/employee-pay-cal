from pay_function import *
account = int(input("1 - run or 2 - quit"))
while account != 2:

    employee_name = input("Enter employee name:")
    pay_type = input("Are you salary or hourly?").lower()
    if pay_type == "hourly":
        number = float(input("How many hours have yoou worked?"))
        pay = hourly(number)
    elif pay_type == "salary":
        exp = int(input("How many years have you worked?"))
        pay = full_time(exp)
    else:
        print("You are unemployeed!")

    print(employee_name, "your pay-rate is", pay)
    account = int(input("1 - run or 2 - quit"))
    

