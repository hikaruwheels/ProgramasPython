def numerospares(numero):
    return (numero % 2 == 0)


print("Dime un numero")
num = int(input())
index = 1
while(index < num):
    
    index = index + 1
    
    if (numerospares(index)):
        print(index)
    