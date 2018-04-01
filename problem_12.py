import math

def find_divisor(value):

    total_divisors = 0

    if value % 2 != 0:
        return False

    index = 1
    while index < math.sqrt(value + 1):

        if value % index == 0:
            total_divisors += 2
        
        index += 1

    if total_divisors >= 500:
        print(total_divisors)
        return True

    return False        

def create_triangle_number(value, index):
    value += index
    return value

def main ():

    value = 0
    index = 1

    while True:
        value = create_triangle_number(value, index)
        
        if find_divisor(value):
            print(value)
            return

        index += 1

if __name__ == "__main__":
    main()