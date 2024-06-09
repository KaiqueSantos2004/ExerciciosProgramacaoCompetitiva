def calcularLeds(V:list) -> int:
    x=0
    for i in V:
        match i:
            case 1:
                x+=2
            case 2:
                x+=5
            case 3:
                x+=5
            case 4:
                x+=4
            case 5:
                x+=5
            case 6:
                x+= 6
            case 7:
                x+=3
            case 8:
                x+=7
            case 9:
                x+=6
            case 0:
                x+=6
    return x



N = int(input("Digite o número de Casos: "))

for i in range (N):
    V = list(map(int, input("Digite o número que deseja escrever com LEDS: ") ))
    print(str(calcularLeds(V))+ " leds")  
      