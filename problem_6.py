import math

squared_sum = 0
sum_squares = 0
maximum = 100

for number in range(0, maximum + 1):
    sum_squares += pow(number,2)

for number in range(0, maximum + 1):
    squared_sum += number

squared_sum = pow(squared_sum, 2)

print(squared_sum - sum_squares)