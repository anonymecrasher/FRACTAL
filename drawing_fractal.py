import turtle as t

def arbre(n, l):
    
    if n > 0:
        t.forward(l)
        t.left(45)
        t.forward(l/3)
        t.left(180)
        t.forward(l/3)
        t.left(180)
        arbre(n-1,l/3)
        t.left(180)
        t.left(90)
        t.forward(l/3)
        t.left(180)
        t.forward(l/3)
        t.left(180)
        arbre(n-1,l/3)
        t.left(45)
        t.forward(l)
        t.left(180)
        
        
        
        
        
        
        
        
        
        
def main():
    t.speed(1)
    t.left(90)
    arbre(3, 150)
main()
