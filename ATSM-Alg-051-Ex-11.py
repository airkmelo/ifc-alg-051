#ATSM-Alg-051-Ex-11

def conta_digitos(n, d):
    n = str(n)
    d = str(d)
    x = n.count(d)
    return x


def main():
    nbm = int(input("Insira seu numero: "))
    nb2 = int(input("Insira seu outro numero: "))
    z = 0
    for i in range(1, 10):
        x = conta_digitos(nbm,i)
        y = conta_digitos(nb2,i)
        if x == y:
            z += 1
            if z == 9:
                c = 1
        else: 
            c = 0
    if c == 1:
        print("Permutação")
    else:
        print("Não é permutação")
main()