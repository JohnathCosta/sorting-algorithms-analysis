import time

def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10


entrada_base = [27287, 74058, 30845, 64876, 97470, 59348, 25483, 90564, 39644, 78264]
vetores_crescente = []
vetores_decrescente = []

print("Original:", entrada_base)
print("Crescente: ", sorted(entrada_base))
print("Decrescente:", sorted(entrada_base, reverse=True))
print("\n")

print("Radix Sort - Tempo para vetores ORIGINAIS\n")
for n in range(10, 201, 10):
    vetor = entrada_base * (n // 10)
    vetor_copy = vetor.copy()
    start = time.time()
    radix_sort(vetor_copy)
    end = time.time()
    vetores_crescente.append(vetor_copy.copy())
    vetores_decrescente.append(sorted(vetor_copy.copy(), reverse=True))
    print(f"Tamanho n = {n} | Tempo original: {end - start:.6f} segundos")


print("\nRadix Sort - Tempo para vetores ordenados (crescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_crescente[i]
    vetor_copy = vetor.copy()
    start = time.time()
    radix_sort(vetor_copy)
    end = time.time()
    print(f"Tamanho n = {n} | Tempo ordenado crescente: {end - start:.6f} segundos")


print("\nRadix Sort - Tempo para vetores ordenados (decrescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_decrescente[i]
    vetor_copy = vetor.copy()
    start = time.time()
    radix_sort(vetor_copy)
    end = time.time()
    print(f"Tamanho n = {n} | Tempo ordenado decrescente: {end - start:.6f} segundos")
