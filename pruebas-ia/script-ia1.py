def fibonacci(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def es_primo(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

fib_list = fibonacci(50)
primos_fib = [x for x in fib_list if es_primo(x)]

print("La lista de los primeros 50 números de la secuencia de Fibonacci es:")
print(fib_list)

print("\nLa lista de los primos de la secuencia de Fibonacci es:")
print(primos_fib)
