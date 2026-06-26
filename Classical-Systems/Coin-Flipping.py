""" Simulating FairCoin in Python
Flip a fair coin 100 times. Calculate the total number of heads and tails, 
and then check the ratio of the number of heads and the number of tails.

Do the same experiment 1000 times.

Do the same experiment 10,000 times.

Do the same experiment 100,000 times.

Do your results get close to the ideal case (the numbers of heads and tails are equal)?"""

from random import randrange

experiment = [100, 1000, 10000, 100000]
for j in experiment:
    Head = Tail = 0
    for i in range(j):
        if(randrange(2) == 1):
            Head += 1
        else:
            Tail += 1
    print(f"The coin flipped {Head + Tail}, Head = {Head} and Tail = {Tail}")