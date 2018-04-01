index = 3
val_1 = 1
val_2 = 1

while True:

    value_to_check = val_1 + val_2
    value_to_check_in_string = str(value_to_check)

    if len(value_to_check_in_string) == 1000:
        print(index)
        break
    
    val_1 = val_2
    val_2 = value_to_check
    index += 1
