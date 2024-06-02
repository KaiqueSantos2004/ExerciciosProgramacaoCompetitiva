
N, M = map(int, input("Digite numero e quantidade de entusiasmo máximo: ").split(" "))
while True:
    sapos = list(map(int,input("Digite o entusiasmo dos Sapos: ").split(" ")));
    if len(sapos) == N:
        break
    else:
        print("Digite uma lista de " + str(N ) + " Números");

sequencias = 0
soma = 0

for i in range(N):
    
    for j in range(i,len(sapos)):
        soma += sapos[j];
        if soma == M:
            sequencias +=1
            soma = 0
            break
        if soma > M:
            soma = 0
            break
              
print(sequencias);


'''
for i in range(0,len(sapos)):
    numero = numero + sapos[i];
    if numero == M:
        sequencias += 1;
        numero = sapos[i-1]
        i = i-1
    elif numero>M :
        numero = sapos[i];
        if numero == M:
            sequencias +=1
             
'''
