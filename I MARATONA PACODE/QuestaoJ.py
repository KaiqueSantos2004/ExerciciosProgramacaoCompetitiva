N,X = map(int,input("Digite o numero de livros e o preco total maximo: ").split());


while True:
    precos = list(map(int, input("Digite os precos dos livros :").split()));
    if len(precos) == N:
        break;
    else :
        print("Digite " +str(N) +  " precos de cada livro em linha!") 
        
while True:
    paginas = list(map(int,input("Digite o Número de paginas de cada livro: ").split()));
    if len(paginas) == N:
        break
    else:
        print("Digite " + str(N) + "  numero de paginas em linha ");
        

maior_paginas = 0
     
for i in range(N):
    preco_atual = 0
    paginas_atual = 0
    for j in range(i,N):
        preco_atual += precos[j]
        paginas_atual += paginas[j]
        if preco_atual > X:
            preco_atual -= precos[j];
            paginas_atual -= paginas[j];
            continue
        if paginas_atual > maior_paginas:
            maior_paginas = paginas_atual;
            
print(maior_paginas)