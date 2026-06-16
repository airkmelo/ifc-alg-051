#ATSM-Alg-051-Ex-09

def eh_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        x = True
    else :
        x = False
    return x
def main():
    y = int(input("Insira o ano: "))
    print(eh_bissexto(y))

main()