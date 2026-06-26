"""What are the probabilities of observing the states 0
 and 1
 if the system is in (-3/5, -4/5) OR (3/5, -4/5) OR (1/SQRT(3), -SQRT(2)/SQRT(3))"""

# Define the states (the third one uses **0.5 for the square root)
state1 = [-3/5, -4/5]
state2 = [3/5, -4/5]
state3 = [1 / 3**0.5, -(2**0.5) / 3**0.5]

# Direct calculation and print
for i, state in enumerate([state1, state2, state3], 1):
    p0 = state[0]**2
    p1 = state[1]**2
    print(f"State {i} -> P(|0⟩): {p0:.2%}, P(|1⟩): {p1:.2%}")