## importation des modules

## Déclaration des fonction

def fonction_1(i=0):
    if i < 3:
        print(i)
        fonction_1(i+1)

def fonction_4(i):
    if i > 0:
        print(i)
        fonction_4(i-1)

def somme(n):
    som = n
    if n > 0:
        som += somme(n-1)
    return som

def puissance(x, n):
    n -= 1
    pui = x
    if n > 0:
        pui *= puissance(x, n)
    return pui

def main():
    print(somme(3))
    
    
## Programme principal
if __name__ == '__main__':
    main()
