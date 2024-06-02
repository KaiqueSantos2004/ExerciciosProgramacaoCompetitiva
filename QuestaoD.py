
n = int(input("Digite um número: "));

valores = []
valores.insert(0,n);
while n!=1:
    if n%2 ==0:
        n=n//2
        valores.append(n);
    elif n%2 !=0:
        n = (n*3)+1
        valores.append(n);


print(" ".join(map(str,valores)))