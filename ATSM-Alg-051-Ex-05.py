#ATSM-Alg-051-Ex-05

def potencia(x, y):
    y = int(y)
    res = 1
    for i in range(y):
        res = res * x
    return res

def main():

    i = float(input())
    l = float(input())
    print(potencia(i, l))     
main()