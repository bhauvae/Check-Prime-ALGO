import timeit
import math

t1 = timeit.timeit()

n = int(input("enter the number to check for prime: "))
m = math.floor(math.sqrt(n))

for i in (3, m + 1, 2):
    if n % i == 0:
        break
else:
    print("The number is prime")

t2 = timeit.timeit()

print("Run time: ", t2 - t1)
