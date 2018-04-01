def read_file_of_ints (two_dimensional_array):

    data_file = open('resource_files/problem_11_number.txt', 'r')

    while True:
        line = data_file.readline()

        if not line:
            break

        words = line.split()
        two_dimensional_array.append(words)

    data_file.close()

def multiply_horizontal (two_dimensional_array, highest_value):

    for index in range(0, len(two_dimensional_array)):
        for sub_index in range(0, len(two_dimensional_array) - 4):
            value = 1
            value *= int(two_dimensional_array[index][sub_index])
            value *= int(two_dimensional_array[index][sub_index+1])
            value *= int(two_dimensional_array[index][sub_index+2])
            value *= int(two_dimensional_array[index][sub_index+3])

            if(highest_value < value):
                highest_value = value

    return highest_value

def multiply_vertical (two_dimensional_array, highest_value):

    for index in range(0, len(two_dimensional_array)):
        for sub_index in range(0, len(two_dimensional_array) - 4):
            value = 1
            value *= int(two_dimensional_array[sub_index][index])
            value *= int(two_dimensional_array[sub_index+1][index])
            value *= int(two_dimensional_array[sub_index+2][index])
            value *= int(two_dimensional_array[sub_index+3][index])

            if(highest_value < value):
                highest_value = value

    return highest_value

def multiply_LL_to_UR (two_dimensional_array, highest_value):

    for index in range(0, len(two_dimensional_array)):
        for sub_index in range (0, len(two_dimensional_array)):
            
            value = 1
            if(index > 4 and sub_index < len(two_dimensional_array) - 4):
                value *= int(two_dimensional_array[sub_index][index])
                value *= int(two_dimensional_array[sub_index+1][index-1])
                value *= int(two_dimensional_array[sub_index+2][index-2])
                value *= int(two_dimensional_array[sub_index+3][index-3])

            if(highest_value < value):
                highest_value = value

    return highest_value


def multiply_UL_to_LR (two_dimensional_array, highest_value):

    for index in range(0, len(two_dimensional_array)):
        for sub_index in range (0, len(two_dimensional_array)):
            
            value = 1
            if(index < len(two_dimensional_array) - 4 and sub_index < len(two_dimensional_array) - 4):
                value *= int(two_dimensional_array[sub_index][index])
                value *= int(two_dimensional_array[sub_index+1][index+1])
                value *= int(two_dimensional_array[sub_index+2][index+2])
                value *= int(two_dimensional_array[sub_index+3][index+3])

            if(highest_value < value):
                highest_value = value

    return highest_value

def main ():

    highest_value = 0
    two_dimensional_array = []
    read_file_of_ints(two_dimensional_array)

    highest_value = multiply_horizontal(two_dimensional_array, highest_value)
    highest_value = multiply_vertical(two_dimensional_array, highest_value)
    highest_value = multiply_LL_to_UR(two_dimensional_array, highest_value)
    highest_value = multiply_UL_to_LR(two_dimensional_array, highest_value)

    print(highest_value)

if __name__ == "__main__":
    main()