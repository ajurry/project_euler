old_1 = 1
old_2 = 1
new = 0
total = 0
max = 4000000

while new < max:
    new = old_1 + old_2
     
    if new % 2 == 0:
        total += new

    old_2 = old_1
    old_1 = new

print(total)