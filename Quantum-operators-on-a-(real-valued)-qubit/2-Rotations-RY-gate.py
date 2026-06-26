from math import sin,cos
from math import pi

rotation_angle = 2*pi/3
# the quantum state
quantum_state = [ cos(rotation_angle) , sin (rotation_angle) ]
print("The quantum state is",round(quantum_state[0],4),"|0> +",round(quantum_state[1],4),"|1>")

the_expected_number_of_zeros = 1000*cos(rotation_angle)**2
the_expected_number_of_ones = 1000*sin(rotation_angle)**2

# expected results
print("The expected value of observing '0' is",round(the_expected_number_of_zeros,4))
print("The expected value of observing '1' is",round(the_expected_number_of_ones,4))

"""draw_qubit()

draw_quantum_state(quantum_state[0],quantum_state[1],"|v>")"""