def find_prime_factors(prime_numbers, number, prime_factors):

    for prime in prime_numbers:
        if number % prime == 0:
            if number in prime_numbers:
               prime_factors += [prime]
               break
        
            number = find_prime_factors(prime_numbers, number/prime, prime_factors)
            prime_factors += [prime]
            break


def is_prime_number(number, prime_numbers):

    is_prime = True

    for prime_number in prime_numbers:

        if number % prime_number == 0:
            is_prime = False
            break

    if(is_prime):
        prime_numbers += [number]
        return is_prime

def main ():

    number = 3
    maximum = 20
    prime_numbers = [2]
    prime_factors = []
    nums = {}
    local_nums = {}

    while number != maximum + 1:
        is_prime_number(number, prime_numbers)
        number += 1

    number = 1
    while number != maximum + 1:
        find_prime_factors(prime_numbers, number, prime_factors)
        print(prime_factors)        

        for factor in prime_factors:
            if local_nums.has_key(factor):
                local_nums[factor] += 1
            else:
                local_nums[factor] = 1

        for local_num in local_nums:
            if nums.has_key(local_num):
                if nums[local_num] < local_nums[local_num]:
                    nums[local_num] = local_nums[local_num]
            else:
                nums[local_num] = local_nums[local_num]

        prime_factors = []
        local_nums.clear()
        number += 1

    total = 1
    for value in nums:
        total *= pow(value, nums[value])
    print(total)



if __name__ == "__main__":
    main()

# BETTER WAY OF DOING THIS IS TO FIND PRIME FACTORS UP TO N
# MULTIPLY ALL PRIME NUMBERS
# FOR EACH VALUES THAT ISN'T PRIME AND ISN'T DIVISIBLE AND THE MA