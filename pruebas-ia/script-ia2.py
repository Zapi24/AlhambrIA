fibonacci = [0, 1]
n_fibonacci = len(fibonacci)

for i in range(n_fibonacci + 5):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

primes = []
for num in fibonacci:
    if num > 1 and all([num % i != 0 for i in range(2, int(num ** 0.5) + 1)]):
        primes.append(num)

primes[:50]
