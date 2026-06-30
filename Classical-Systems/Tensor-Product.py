# A tensor B

A = [[-1, 0 ,1], [-2,-1,2]]
B = [[0,2],[3,-1],[-1,1]]
AB = []
lista = []

for k in range(6):
    lista = []
    if k<3:
        for i in range(3):
            for j in range(2):
                print(f'{A[0][i]} x {B[k][j]} = {A[0][i] * B[k][j]}')
                lista.append(A[0][i] * B[k][j])
        AB.append(lista)
    else:
        for i in range(3):
            for j in range(2):
                print(f'{A[1][i]} x {B[k-3][j]} = {A[1][i] * B[k-3][j]}')
                lista.append(A[1][i] * B[k-3][j])
        AB.append(lista)
print('A tensor B: ')
for i in range(6):
    print(AB[i])
    