def init_hanoi(n):
    t1,t2,t3 = [], [], []
    for i in range(n, 0, -1):
        t1.append(i)
    return (t1, t2, t3)
    


def hanoi(n, depart, arrivee, intermediaire, ini = False):
    depart -= 1
    arrivee -= 1
    intermediaire -= 1
    if ini == True:
        hanoii = init_hanoi(n)
    if n == 1:
        temp = hanoii[depart][len(hanoii[depart])-1]
        hanoii[depart].remove(temp)
        hanoii[arrivee].append(temp)
    return hanoii
        
        
    

def main():
    print(hanoi(1, 1, 3, 2, True))
    
