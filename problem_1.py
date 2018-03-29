i = 0
total = 0
val = 1000

while i != 1000:

    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i

    i = i + 1

print(total)