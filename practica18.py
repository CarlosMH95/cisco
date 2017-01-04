import numpy as np
fila = 1
columna = 2

matriz = [[1,3,6],
    [5,7,9],
    [3,18,0]]

print (matriz[fila][columna])

arreglo = np.array(matriz)
print (arreglo)

valor_max = np.max(arreglo)
print (valor_max)

matriz = np.random.randint(1,50,(10,5))
print (matriz)

print (np.sum(matriz))

print (np.sum(matriz,axis = 1))

submatriz = matriz[1:6,2:5]
print (submatriz)
print (np.mean(submatriz))

submatriz = matriz[1:6,[1,3,4]]
print (submatriz)

print (np.transpose(submatriz))

#redimensionar matriz
matriz2 = np.reshape(matriz,(25,2))
print (matriz2)

matriz = np.random.randint(1,30,(6,5))
print (matriz)
print (np.sort(matriz, axis = 0))

#ordenamiento x columna segun indice
indices = np.argsort(matriz[:3],axis=0)
print (indices)

matriz_ordenada = matriz[indices,:]
print (matriz_ordenada)

matriz = [[1,3,6],
    [5,7,9],
    [3,18,0]]

arreglo = np.array(matriz,float)
print(arreglo)

arreglo = np.array(matriz,str)
print(arreglo)

matriz = np.random.randint(1,30,(6,5))
print (matriz)
matriz[matriz > 15]=-1
print (matriz)