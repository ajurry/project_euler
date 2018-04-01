import math

def find_triple (triple_value):

    for k in range (0, triple_value):
        for j in range (0, triple_value):
            for i in range (0, triple_value):

                if k < j:
                    break
                
                if j < i:
                    break

                if (pow(i,2) + pow(j,2) == pow(k,2)):
                    if i+j+k == triple_value:
                        print(i*j*k)
                        return

def main ():
    triple_value = 1000
    find_triple(triple_value)
    
if __name__ == "__main__":
    main()