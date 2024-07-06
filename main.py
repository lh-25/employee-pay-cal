# In the main program, create a loop to start and quit the program 
# Evertime it runs, it'll ask for a employee name and type (salary or hourly)
# if type = hourly, ask for number of hours worked and use the hourly function in a variable 
# if type = salary, ask for years worked and use the full-time function in a variable
# Anything else, print off "You are unemployeed!"
# At the loop end, print off the employees name and their pay-rate
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
    

