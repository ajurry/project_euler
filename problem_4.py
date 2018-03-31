def is_palendrome (a, b):

    string_forward = str(a * b)
    string_backward = string_forward[::-1]

    if string_forward == string_backward:
        return True

    return False



def main ():
    
    a = 999
    b = 999

    acceptable_number = []

    while a != 1 and b != 1:
        
        if is_palendrome(a, b):
            acceptable_number.append(a*b)

        b -= 1

        if b == 1:
            a -= 1
            b = 999

    acceptable_number.sort()
    for val in acceptable_number:
        print(val)

if __name__ == "__main__":
    main()