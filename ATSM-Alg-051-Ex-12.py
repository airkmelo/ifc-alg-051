#ATSM-Alg-051-Ex-12

def encaixa(a, b):

    c1 = len(str(a))
    c2 = len(str(b))
    c3 = min(c1, c2)
    c4 = str(a)
    c5 = str(b)
    x = 0
    for i in range(1, (c3+1)):
        
        if c4[-i] == c5[-i]:
            x=x+1
            if x == c3:
                z = True
        else: 
            z = False
    
    return z

def main():
    x = int(input())
    y = int(input())
    if encaixa(x, y) == True:
        print(f"{x} {y} => encaixa")
    elif encaixa(x, y) == False:
        print(f"{x} {y} => nao encaixa")
main()
