"""What are the probabilities of observing the states 0
 and 1
 if the system is in (-3/5, -4/5) OR (3/5, -4/5) OR (1/SQRT(3), -SQRT(2)/SQRT(3))"""

# Definimos los estados (el tercero usa **0.5 para la raíz cuadrada)
estado1 = [-3/5, -4/5]
estado2 = [3/5, -4/5]
estado3 = [1 / 3**0.5, -(2**0.5) / 3**0.5]

# Cálculo e impresión directa
for i, estado in enumerate([estado1, estado2, estado3], 1):
    p0 = estado[0]**2
    p1 = estado[1]**2
    print(f"Estado {i} -> P(|0⟩): {p0:.2%}, P(|1⟩): {p1:.2%}")
