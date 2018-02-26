#==============================================================================
# Simulation: Estimating Pi on A Dartboard
# Related article: https://medium.com/@andrew.chamberlain/how-to-estimate-pi-at-the-bar-c8f65c592e95
# by Andrew Chamberlain, Ph.D.
# achamberlain.com
#==============================================================================

import numpy as np

np.random.seed(100)

n = 10000
k = 0

for i in range(n):
    x = np.random.uniform(low=-1,high=1,size=1)
    y = np.random.uniform(low=-1,high=1,size=1)
    z = (x**2 + y**2)**0.5
    if z <= 1:
        k = k + 1
    else:
        k = k

pi = 4*k/n
print(pi)
