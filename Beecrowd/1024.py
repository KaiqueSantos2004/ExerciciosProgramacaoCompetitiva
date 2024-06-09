def criptografar(M: list) -> list:
    novapalavra = []
    #primeira passada
    for i in M:
        if i.isdigit():
            novapalavra.append(i)
            continue
        elif i == ' ':
            novapalavra.append(i)
            continue
        elif i.isalnum():
            novapalavra.append(chr( ord(i)+3))
        else:
            novapalavra.append(i) 
            
    #segunda passada
    tamanho_palavra = len(novapalavra)
    for i in range(tamanho_palavra//2):
        aux = novapalavra[i]
        novapalavra[i] = novapalavra[tamanho_palavra - 1 -i]
        novapalavra[tamanho_palavra - 1 -i] = aux
        
        
    #terceira passada:
    metade = len(M)//2
    for i in range(metade,len(novapalavra)):
        novapalavra[i] = chr(ord(novapalavra[i])-1)
        
        
    return ''.join(novapalavra)
    

N = int(input(""))


for i in range(N):
    M = input("")
    X =criptografar(M)
    print(X)
    
