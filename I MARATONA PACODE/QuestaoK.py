
import sys
N = int(input("Digite o tamanho do vetor: "));
while True :
    K= list(map(int,input("Digite a lista: ").split(" ")));
    if len(K) == N:
        break;
    else:
        print("Digite uma lista de tamanho " +  str(N) );
 
'''  Minha solução(Nível de complexidade 2):
maior = K[0];
for i in range (len(K)):
    aux = 0;
    for j in range(i,len(K)):
        aux += K[j]
        if aux > maior:
            maior = aux
print(maior)
''' 

'Solução com Algoritmo De Kadane (Nível de Complexidade 1):'
maior_local = 0
maior_total = -sys.maxsize 

for i in range(0, len(K)):
    maior_local = maior_local + K[i]
    if maior_total < maior_local:
        maior_total = maior_local
    if maior_local < 0:
        maior_local = 0;
        
print(maior_total);
            
        
