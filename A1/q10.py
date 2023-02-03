import math
import time
from memory_profiler import profile

"""
For question 10, I picked Bhaskara I's sine approximation formula,
and Taylor polynomial of degree 3 and degree 5.

I have attached a screenshot of my result for sin(pi/3).

It appears that there isn't much significant difference for memory consumption between those 3 methods.
But it appears that Taylor polynomial of degree 5 generates the best result,
followed by Bhaskara's method and Taylor polynomial of degree 3.

Note: I used memory_profiler package to measure memory consumption,
and time package to measure time spent on each function.
"""

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

print("\n")
print("The value of sin(pi/3) = 0.86602540378 (approx.)")
print("\n")
t0= time.time()
print("Result of sinBhaskara: " , sinBhaskara(math.pi/3))
t1 = time.time()
print("Time spent on Bhaskara approximation: ", t1 - t0, "seconds")
print("\n")

t2= time.time()
print("Result of Taylor polynomial, degree 3: " , taylor3(math.pi/3))
t3 = time.time()
print("Time spent on Taylor polynomial, degree 3: ", t3 - t2, "seconds")
print("\n")

t4= time.time()
print("Result of Taylor polynomial, degree 5: " , taylor5(math.pi/3))
t5 = time.time()
print("Time spent on Taylor polynomial, degree 5: ", t5 - t4, "seconds")

