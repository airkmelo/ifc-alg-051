#ATSM-Alg-051-Ex-10

def conta_digitos(n, d):
    n = str(n)
    d = str(d)
    x = n.count(d)
    return x

def main():
    nbm = int(input("Insira seu numero: "))
    dgt = int(input("Insira seu digito entre 0 e 9: "))
    print(conta_digitos(nbm, dgt))
main()