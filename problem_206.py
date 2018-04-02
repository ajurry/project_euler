import math

def create_template_list(number_list):
    for val in range(1, 10):
        number_list += [str(val)]
        number_list += [str(0)]

    number_list += [str(0)]

def number_loop(number_list):

    for a in range(0, 10):
        number_list[1] = str(a)
        for b in range(0, 10):
            number_list[3] = str(b)
            for c in range(0, 10):
                number_list[5] = str(c)
                for d in range(0, 10):
                    number_list[7] = str(d)
                    for e in range(0, 10):
                        number_list[9] = str(e)
                        for f in range(0, 10):
                            number_list[11] = str(f)
                            for g in range(0, 10):
                                number_list[13] = str(g)
                                for h in range(0, 10):
                                    number_list[15] = str(h)
                                    for i in range(0, 10):
                                        number_list[17] = str(i)

                                        string = ''.join(number_list)
                                        if(math.sqrt(int(string)).is_integer()):
                                            print(string)
                                            return

                                        
        

def main():
    number_list = []
    string = ''
    create_template_list(number_list)
    number_loop(number_list)


if __name__ == "__main__":
    main()




