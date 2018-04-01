def set_number_dictionary(number_dictionary):

    number_dictionary[1] = "one"
    number_dictionary[2] = "two"
    number_dictionary[3] = "three"
    number_dictionary[4] = "four"
    number_dictionary[5] = "five"
    number_dictionary[6] = "six"
    number_dictionary[7] = "seven"
    number_dictionary[8] = "eight"
    number_dictionary[9] = "nine"

    number_dictionary[10] = "ten"
    number_dictionary[11] = "eleven"
    number_dictionary[12] = "twelve"
    number_dictionary[13] = "thirteen"
    number_dictionary[14] = "fourteen"
    number_dictionary[15] = "fifthteen"
    number_dictionary[16] = "sixteen"
    number_dictionary[17] = "seventeen"
    number_dictionary[18] = "eigthteen"
    number_dictionary[19] = "nineteen"

    number_dictionary[20] = "twenty"
    number_dictionary[30] = "thirty"
    number_dictionary[40] = "fourty"
    number_dictionary[50] = "fifty"
    number_dictionary[60] = "sixty"
    number_dictionary[70] = "seventy"
    number_dictionary[80] = "eighty"
    number_dictionary[90] = "ninety"

    number_dictionary[100] = "hundred"
    number_dictionary[1000] = "thousand"

def thousand_converter(value, number_dictionary, words):

    number = value / 1000
    if number != 0:
        if number_dictionary.has_key(number)
            words += [number_dictionary[number]]
            words += [number_dictionary[1000]]
        elif
            hundreds_converter(value, number_dictionary, words)

    return
    
def hundreds_converter(value, number_dictionary, words):
    
    number = value / 100
    if number != 0:
        if number_dictionary.has_key(number)
            words += [number_dictionary[number]]
            words += [number_dictionary[100]]
        elif
            hundreds_converter(value, number_dictionary, words)
    return

def tens_converter(value, number_dictionary, words):
    
    number = value / 10
    if number != 0:
        if number_dictionary.has_key(number)
            words += [number_dictionary[number]]
        elif
            less_than_twnety_converter(value, number_dictionary, words)
    return

def less_than_twenty_converter(value, number_dictionary, words):
    return

def main ():
    value = 2001
    words = []
    number_dictionary = {}
    set_number_dictionary(number_dictionary)
    thousand_converter(value, number_dictionary, words)
    print(words)




if __name__ == "__main__":
    main()