import math
import time
from memory_profiler import profile

# Bhaskara I's sine approximation.
# x is in radian
@profile
def sinBhaskara(x):
    return (16*x * (math.pi - x)) / ((5*math.pi**2) - (4*x * (math.pi - x)))

# degree 3 of Taylor polynomial to approximate sine
# I precomputed factorials (3!=6)
@profile
def taylor3(x):
    return x - (x**3/6)

# degree 5 of Taylor polynomial to approximate sine
# I precomputed factorials (3!=6, 5! =120)
@profile
def taylor5(x):
    return x - (x**3/6) + (x**5/120)

t0= time.time()
print("sinBhaskara: " , sinBhaskara(math.pi/3))
t1 = time.time()
print("Time elapsed: ", t1 - t0, "seconds") # CPU seconds elapsed (floating point)
print("taylor3: " , taylor3(math.pi/3))
print("taylor5: " , taylor5(math.pi/3))

