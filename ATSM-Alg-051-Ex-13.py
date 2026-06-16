#ATSM-Alg-051-Ex-13

def encaixa(a, b):

    c1 = len(str(a))
    c2 = len(str(b))
    c3 = max(c1, c2)
    c6 = min(c1, c2)
    c4 = str(a)
    c5 = str(b)
    x = 0
    
    if c1 > c2:
        if c5 in c4:
            z = True
        else: 
            z = False
    else:
        if c4 in c5:
            z = True
        else: 
            z = False
    return z

def main():
    x = int(input())
    y = int(input())
    a = len(str(x))
    b = len(str(y))
    if encaixa(x, y) == True and a>b:
        print(f"{x} {y} => a é um segmento de b")
    elif encaixa(x, y) == True and b>a:
        print(f"{x} {y} => b é um segmento de a")
    else:
        print(f"{x} {y} => um nao e segmento do outro")

main()