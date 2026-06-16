#ATSM-Alg-051-Ex-02

def imprime_n_vezes(nome, n):
    for i in range(n):
        print(nome)

def main():
    st = input()
    nr = int(input())
    imprime_n_vezes(st, nr)

main()