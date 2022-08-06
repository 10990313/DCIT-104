# 10990313
# I certify that I Ferguson Domabaara wrote this code all by myself.

number = int(input("Please type in a number: \n"))

def prime_checker(value):
    is_prime = False
    num_factors = 0;
    for x in range(1, value + 1):
        if value % x == 0:
            num_factors += 1
    if num_factors == 2:
            is_prime = True;
    return is_prime
    
def prime_sum(number):
    sum = 0;
    for x in range(1, number + 1):
        if prime_checker(x) == True:
            sum += x
    print(f"The sum of the prime numbers below {number} is {sum}.")
    
prime_sum(number)
