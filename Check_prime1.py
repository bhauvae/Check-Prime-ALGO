import timeit

t1 = timeit.timeit()

n = int(input("enter the number to check for prime: "))
for i in (2, n):
    if n % i == 0:
        break
else:
    print("The number is prime")

t2 = timeit.timeit()
print("Run time: ", t2 - t1)
