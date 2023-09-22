## importation des modules
import time


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
    
def factoriel(n):
    if n > 0:
        return n * factoriel(n-1)
    return 1

def compte_chiffres(n):
    if n <= 9:
        return 1
    else:
        return 1 + compte_chiffres(n//10)
        
def main():
    print(somme(3))
    t1 = time.perf_counter()
    puissance(2, 90)
    t1 = time.perf_counter() - t1
    t2 = time.perf_counter()
    puissance_base_multiple(2, 90)
    t2 = time.perf_counter() - t2
    t3 = time.perf_counter()
    puissance_recursiv_multiple(2, 90)
    t3 = time.perf_counter() - t3
    print('', t1,'\n',t2,'\n',t3)
    
## Programme principal
if __name__ == '__main__':
    main()
