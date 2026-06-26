"""If the following vectors are valid quantum states defined with real numbers, 
then what can be the values of a and b?

|v> = (a,-0.1, -0.3, 0.4, 0.5)
and
|u> = (1/SQRT(2), 1/SQRT(b), -1/SQRT(3))
"""

v = [-0.1, -0.3, 0.4, 0.5]
suma = 0


print('Ejercicio A')
for numero in v:
    print(f'({numero})**2 +', end=" ")
    suma = suma + numero ** 2
print(' - 1 = -(a**2)')
print(f'{suma - 1} = -(a**2)')
print(f'a = {(-1*(suma-1))**0.5}')

suma = suma + (-1*(suma-1))**0.5
print(suma)

u = [1/(2**0.5), -1/(3**0.5)]
suma = 0
faltante = '(1/b**0.5)**2'


print('\nEjercicio B')
for j in u:
    print(f'({j})**2 +', end=" ")
    suma = suma + j**2
print(f' = 1 - {faltante}')

print(f'{suma} = 1 - {faltante}')
print(f'{suma-1} = - {faltante}')
print(f'{-(suma-1)} = {faltante}')
suma = -(suma-1)

print(f'{suma**0.5} = {faltante[0:10]}')
print(f'{faltante[3:9]} = 1/({suma**0.5})')
print(f'{faltante[3]} = {(1/suma**0.5)**2}')