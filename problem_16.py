import math

total_sum = 0
total_pow = pow(2,1000)
total_pow_in_str = str(total_pow)

for character in total_pow_in_str:
    total_sum += int(character)

print(total_sum)