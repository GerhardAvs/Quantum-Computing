"""Flip the following biased coin 100 times. 
Calculate the total numbers of heads and tails, and then 
check the ratio of the number of heads and the number of tails.


BiasedCoin = (Head = 0.6) (Tail = 0.4)


Do the same experiment 1000 times.

Do the same experiment 10,000 times.

Do the same experiment 100,000 times.

Do your results get close to the ideal case
"""

from random import randrange

experiment = [100, 1000, 10000, 100000]

for i in experiment:
    Head = Tail = 0
    for i in range(i):
        if randrange(100) < 60:
            Head += 1
        else:
            Tail += 1
    print(f"The biased coin flipped {Head + Tail}, Head = {Head} and Tail = {Tail}")