def read_file_of_ints (two_dimensional_array):

    data_file = open('resource_files/problem_13_number.txt', 'r')

    while True:
        line = data_file.readline()

        if not line:
            break

        words = line.split()
        two_dimensional_array.append(words)

    data_file.close()

def main ():

    final_str = ''
    highest_value = 0
    two_dimensional_array = []
    read_file_of_ints(two_dimensional_array)

    for value in range(0, len(two_dimensional_array)):
        highest_value += int(two_dimensional_array[value][0])

    int_in_string = str(highest_value)
    print(int_in_string)


if __name__ == "__main__":
    main()