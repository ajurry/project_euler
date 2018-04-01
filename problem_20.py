import math

total_sum = 0
total_factorial = math.factorial(100)
total_factorial_in_str = str(total_factorial)

for character in total_factorial_in_str:
    total_sum += int(character)

print(total_factorial_in_str)
print(total_sum)