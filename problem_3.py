import math

def is_prime_number(number, prime_numbers):

    is_prime = True

    for prime_number in prime_numbers:

        if number % prime_number == 0:
            is_prime = False
            return 1

        if number < pow(prime_number, 2) :
            if(is_prime):
                prime_numbers += [number]
                return number

    return 1

def find_factor(maximum):
    
    prime_numbers = [2]
    current_number = 3

    while maximum != 1:
        number = is_prime_number(current_number, prime_numbers)
        current_number += 1

        if number != 1:
            if maximum % number == 0:
                print(number)
                maximum /= number
        
def main ():
    maximum = 600851475143
    find_factor(maximum)

if __name__ == "__main__":
    main()