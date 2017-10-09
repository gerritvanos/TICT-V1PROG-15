#A
b = 7
def verdubbelB(b):
    b = b + b
    return b

b = verdubbelB(b)

print(b)
#B
import datetime
time = datetime.datetime.today()
print(time.strftime(("%H:%M:%S")))

#C
def f(y):
 return 2*y + 1

def g(x):
 return 5 + x + 10

print(f(3)+g(3))