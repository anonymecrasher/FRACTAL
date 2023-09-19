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
    if n > 0:
        n += somme(n-1)
    return n

def puissance(x, n):
    if n == 0:
        return 1
    n -= 1
    elif n > 0:
        x *= puissance(x, n)
    return x

def main():
    print(somme(3))
    
    
## Programme principal
if __name__ == '__main__':
    main()
