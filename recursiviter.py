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
    
    elif n > 0:
        
        x *= puissance(x, n-1)
    return x

def puissance_base_multiple(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n > 1:
        x *= puissance_base_multiple(x, n-1)
        return x

def puissance_recursiv_multiple(x,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return puissance_recursiv_multiple(x,n/2) ** 2
    elif n % 2 == 1:
        return x * (puissance_recursiv_multiple(x,(n-1)/2) ** 2)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
       return fibonacci(n-1) + fibonacci(n-2)
    

def main():
    print(somme(3))
    print(puissance(2, 8))
    print(puissance_base_multiple(2, 8))
    print(puissance_recursiv_multiple(2, 8))
    
## Programme principal
if __name__ == '__main__':
    main()
    
