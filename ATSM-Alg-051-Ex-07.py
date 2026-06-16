#ATSM-Alg-051-Ex-07
import random 

def sorteia_dado():
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    for i in range(1000000):
        x = random.randint(1, 6)
        if x == 1:
            x1 += 1
        elif x == 2:
            x2 += 1
        elif x == 3:
            x3 += 1
        elif x == 4:
            x4 += 1
        elif x == 5:
            x5 += 1
        elif x == 6:
            x6 += 1

    return x1, x2, x3, x4, x5, x6

def main():
    print(sorteia_dado())
main()