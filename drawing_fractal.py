import turtle as t


def arbre(n, l, An):
    if n == 0:
        t.forward(l)
        t.left(180)
        t.forward(l)
        t.left(180)
    elif n > 0:
        t.forward(l)
        t.right(An)
        arbre(n-1, l *(2/3),An)
        t.left(2*An)
        arbre(n-1, l *(2/3),An)
        t.right(An)
        t.left(180)
        t.forward(l)
        t.left(180)

def carre(l):
    for i in range(4):
        t.forward(l)
        t.left(90)

def carre_fractal(n,l):
    if n == 0:
        carre(l)
    elif n > 0:
        carre_fractal(n-1,l/3)
        t.forward(l/3)
        carre_fractal(n-1,l/3)
        t.forward(l/3)
        carre_fractal(n-1,l/3)
        t.forward(l/3)
        t.left(90)
        t.forward(l/3)
        carre_fractal(n-1,l/3)
        t.forward(l/3)
        carre_fractal(n-1,l/3)
        t.forward(l/3)
        t.left(90)
        t.forward(l/3)
        carre_fractal(n-1,l/3)
        t.forward(l/3)
        carre_fractal(n-1,l/3)
        t.forward(l/3)
        t.left(90)
        t.forward(l/3)
        carre_fractal(n-1,l/3)
        t.forward(l/3)
        t.forward(l/3)
        t.left(90)
        
def courbe_de_koch(n, l):
    if n == 0:
        t.forward(l)
    elif n > 1:
        courbe_de_koch(n-1, l/3)
        t.Left(60)
        courbe_de_koch(n-1, l/3)
        t.right(120)
        courbe_de_koch(n-1, l/3)
        t.left(60)
        courbe_de_koch(n-1, l/3)
        
        
        
        
        
        
def main():
    t.speed(0)
    t.left(90)
    carre_fractal(4,400)
    t.done
    
    

main()
