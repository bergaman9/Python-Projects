import time

def countdown(x):
    if x == 0:
        print("done!")
        return
    else:
        print(f"{x}...")
        countdown(x-1)

def power(num, pwr):
    if pwr == 0:
        return 1

    else:
        return num * power(num, pwr-1)


def factorial(num):
    if num == 0:
        return 1

    else: 
        return num * factorial(num-1)


countdown(3)
print(factorial(4))
print(power(5, 3))
