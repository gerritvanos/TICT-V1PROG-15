def pay(wage,hours):
    if hours>0 and hours<=40:
        payment = hours*wage
    elif hours>40 and hours<=60:
        payment = (hours-40)*wage*1.5 + (40*wage)
    elif hours >60:
        payment = (hours - 41) * wage * 1.5 + (40 * wage) + (hours -60)*wage*2.0
    return payment
print(pay(10,35))
print(pay(10,45))
print(pay(10,61))