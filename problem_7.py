import math

def is_prime_number(number, prime_numbers):

    for prime_number in prime_numbers:

        if number % prime_number == 0:
            return

        if number < pow(prime_number, 2) :
            prime_numbers += [number]
            return

def main ():
    value = 3
    prime_numbers = [2]
    maximum = 10001

    while len(prime_numbers) != maximum:
        is_prime_number(value, prime_numbers)
        value += 2

    print(prime_numbers[maximum - 1])



if __name__ == "__main__":
    main()