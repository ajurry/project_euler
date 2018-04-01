def read_file_of_ints (array_of_ints):

    int_file = open('resource_files/problem_8_number.txt', 'r')

    while True:
        line = int_file.readline()

        if not line:
            break

        for character in line:
            if character != '\n':
                array_of_ints.append(character)

    int_file.close()
        
def find_largest_number (array_of_ints, numbers_to_multiply):

    current_highest = 1
    array = []

    for index in range (0, len(array_of_ints) - numbers_to_multiply):

        value = 1
        array = []

        for sub_index in range (index, index + numbers_to_multiply):
            value = value * int(array_of_ints[sub_index])
            
        if current_highest < value:
            current_highest = value
    
    return current_highest


def main ():

    numbers_to_multiply = 13
    array_of_ints = []

    read_file_of_ints(array_of_ints)

    print(find_largest_number(array_of_ints, numbers_to_multiply))
    
    

if __name__ == "__main__":
    main()