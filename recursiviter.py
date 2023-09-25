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
def padovan(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return padovan(n-2)+padovan(n-3)
    
def factoriel(n):
    if n > 0:
        return n * factoriel(n-1)
    return 1

def compte_chiffres(n):
    if n <= 9:
        return 1
    else:
        return 1 + compte_chiffres(n//10)

def rech_dico_recur(liste, el):
    if len(liste_nombre) == 1:
        return 0
    else:
        if liste[len(liste)//2] < el:
            return len(liste)//2 + rech_dico_recur(liste[((len(liste)//2)+1):], el)
        elif liste[len(liste)//2] > el:
            return rech_dico_recur(liste[:((len(liste)//2)+1)], el)



def main():
    pass
    
## Programme principal
if __name__ == '__main__':
    main()
    
