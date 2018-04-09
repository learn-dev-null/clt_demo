
import random
import numpy as np

def roulette(sample_size=1000):
    sum = 0
    for i in range(sample_size):
        val = random.randint(0, 36)
        if val == 30:
            sum += 36
        else:
            sum -= 1

    return sum / sample_size

def clt(sample_size=1000, number_of_samples=1000):
    means = []
    for i in range(number_of_samples):
        means.append(roulette(sample_size))
    return means

def simulate():
    roulette(1000000)

#simulate()

#clt(sample_size=1, number_of_samples=10000):
