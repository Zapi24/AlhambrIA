# Función para verificar si un número es primo
def es_primo(n):
    """Verifica si un número n es primo."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Función para generar la secuencia de Fibonacci hasta el 50º número
def fibonacci(n):
    """Genera los primeros n números de la secuencia de Fibonacci."""
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# Generar los primeros 50 números de la secuencia de Fibonacci
fibonacci_50 = fibonacci(50)

# Filtrar solo los números primos
primos_fibonacci = [num for num in fibonacci_50 if es_primo(num)]

# Imprimir la lista de números primos en la secuencia de Fibonacci
print(primos_fibonacci)
