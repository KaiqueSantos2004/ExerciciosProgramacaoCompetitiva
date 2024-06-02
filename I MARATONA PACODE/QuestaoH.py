
N = int(input("Digite o Numero de Opções: "));
i = 0;
menor = 1
galaxias = []
for i in range(N):
    galaxias.append(int(input(" Número de Galaxias Galaxia: ")))
    
while menor in galaxias:
    menor +=1
print(menor)

'''
N = int(input("Digite o Numero de Opções: "));
menor = 1

while True:
    galaxias = list(map(int, input("Digite os Números de Galáxias: ").split(" ")))
    if len(galaxias) == N:
        break
    else:
        print("Digite em linha!!!")
    
while menor in galaxias:
    menor +=1
        
print(menor)
'''
