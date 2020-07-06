menorTempo = 2^63-1

def busca(tempoA,tempoB,tempoTotal):
    
    global menorTempo
    
    if tempoTotal >= menorTempo: 
         return
    if tempoA == T or tempoB == T:
         if tempoTotal + T < menorTempo:
              menorTempo = tempoTotal + T
              return
    
    if (tempoA > 0) and (tempoB > 0):
             if tempoA > tempoB: 
                 busca(tempoA-tempoB, 0, tempoTotal + tempoB)
             else:
                 busca(0, tempoB-tempoA, tempoTotal + tempoA)
    else:
         if (tempoA == 0) and (tempoB != 0):
             busca(A, tempoB, tempoTotal)
         else:
             if (tempoB == 0)  and (tempoA != 0):
                 busca(tempoA, B, tempoTotal)
                 
T = int(input("Tempo de preparo do Miojo: "))
A = int(input("Tempo da primeira ampulheta: "))
B = int(input("Tempo da segunda ampulheta: "))
busca(A,B,0)
busca(A,0,0)
busca(0,B,0)
if (menorTempo==2^63-1):
    print("Possivelmente, não existe solução para o problema")
else:
    print("Menor tempo de preparo: ")
    print(menorTempo)
             
    
