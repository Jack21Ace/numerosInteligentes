import numpy as np

cantidad = int(input("Ingrese la cantidad de elemntos"))
contador = 0

arr = np.random.randint(1, 10, cantidad)

print(arr)

for i in arr:
    contador = 0
    for x in range(1, i):
        if i%x==0:
            contador+=1
    if contador %2!=0:
        print(f"el numero {i}, no es inteligente")
    else:
        print(f"el numero {i}, si es inteligente")
