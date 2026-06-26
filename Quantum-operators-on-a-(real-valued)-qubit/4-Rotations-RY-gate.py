"""Comience con el estado |0>
    Aplicar R(pi/4) 7 veces y dibujalo
"""
[x,y]=[1,0]

draw_quantum_state(x,y,"v0")

sqrttwo = 2**0.5
oversqrttwo = 1/sqrttwo

R = [ [oversqrttwo, -1*oversqrttwo], [oversqrttwo,oversqrttwo] ]

#
# your code is here
#
# 
def rotar(x,y):
    NewX = R[0][0]*x + R[0][1]*y
    NewY = R[1][0]*x + R[1][1]*y
    return NewX, NewY
    
for i in range(7):
    [x,y]= rotar(x,y)
    draw_quantum_state(x,y,f"v{i+1}")
