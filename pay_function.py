def hourly(number):
    rate = 25
    pay = number * rate
    return pay

def full_time(exp):
    annual_pay = 25000
    if exp >= 2 and exp < 4:
        extra = 1.5
        bonus = 500
    elif exp >= 4 and exp < 10:
        extra = 2
        bonus = 1000
    elif exp >= 10:
        extra = 3
        bonus = 1500
    else:
        extra = 1
        bonus = 200
    annual_pay = (annual_pay * extra) + bonus
    return annual_pay
    
