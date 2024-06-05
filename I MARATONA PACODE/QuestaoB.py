area_original, pedacos = map(int,input("Digite a area original e o numero de pedacos: ").split());

while True:
    tamanho_pedacos = list(map(int,input("Tamanho dos pedaços: ")));
    if tamanho_pedacos == pedacos:
        break
    else:
        print("Digite o tamanho dos pedaços em linha ! ")

area_nova = sum(tamanho_pedacos)

if area_nova == area_original:
    print("Tudo certo!")
else :
    print("Deu ruim!")
