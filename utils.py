def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def simple(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_power_of_five(number):
    if number <= 0:
        return False
    while number % 5 == 0:
        number /= 5
    return number == 1
