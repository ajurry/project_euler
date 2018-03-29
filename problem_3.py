# is_prime = True
# number = 3
# prime_numbers = [2]
# maximum = 600851475143

# while number*2 < maximum:
    
#     for prime_number in prime_numbers[:]:
#         if number % prime_number == 0:
#             is_prime = False
#             break
    
#     if is_prime:
#         prime_numbers.append(number)

#     is_prime = True
#     number += 1

# for prime_number in reversed(prime_numbers):
#     if maximum % prime_number == 0:
#         print(prime_numbers)       
#         break 

import math
# Fermat's Factorization
# N = a^2 + b^2

value_to_find = 600851475143
a = math.ceil(math.sqrt(value_to_find))
b = 0

while True:
    b = abs((math.pow(a,2) - value_to_find))

    if (math.sqrt(b)).is_integer():
        break
    
    a += 1

print(b)

