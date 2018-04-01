import math

def even_number (value):
    return value/2

def odd_number (value):
    return ((3 * (value)) + 1)

def main ():

    value = 0
    chain_value = 0
    highest_chain_value = 0
    value_with_highest_chain_value = 0

    for number in range(1, 1000000):

        chain_value = 0
        value = number

        if number % 2 == 0:
            continue

        while value != 1:

            if value % 2 == 0:
                chain_value += 1
                value = even_number(value)
            else:
                chain_value += 1
                value = odd_number(value)

        if highest_chain_value < chain_value:
            highest_chain_value = chain_value
            value_with_highest_chain_value = number

    print(value_with_highest_chain_value)
    print(highest_chain_value)

if __name__ == "__main__":
    main()