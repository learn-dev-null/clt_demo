# Using inspiration and code from http://ocw.mit.edu/6-0002F16

# We will use the Buffon-Laplace Method to estimate
# the size of π
# run with `python estimate_pi.py`

import random
import numpy as np


def estimatePi(trials, numPoints=1000):
    estimatedPis = []
    for iTrial in range(trials):
        inCircleCount = 0
        for i in range(numPoints):
            x = random.random()
            y = random.random()

            # Equation for circle
            isInCircle = (x*x + y*y)**0.5 <= 1.0
            if isInCircle:
                inCircleCount += 1

        estimatedPi = 4 * (inCircleCount / float(numPoints)) # Buffon-Laplace Method π = 4 * areaOfCircle / areaOfSquare
        estimatedPis.append(estimatedPi)
    estimatedPis = np.array(estimatedPis)
    mean = estimatedPis.mean()
    std = estimatedPis.std()
    print(f'estimated pi: {mean} and std: {std}')
    return (mean, std)

def simulationForPi(precision, trials):
    std = precision
    while std >= precision/2:
        currentEstimate, std = estimatePi(trials)
        print("trials", trials)
        trials *= 2
    return currentEstimate

simulationForPi(0.005, 100)
