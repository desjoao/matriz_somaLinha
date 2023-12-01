matrix=[]
vetorSoma = []
soma = 0

for i in range(3):
    matrix.append([])
    for c in range(3):
        matrix[i].append([])

for i in range(3):
    for c in range(3):
        matrix[i][c] = int(input('Insira um valor: '))
        soma += float(matrix[i][c])
    vetorSoma.append(soma)
    soma = 0
    
print(matrix)
print(vetorSoma)
