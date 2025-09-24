import time

def counting_sort(arr):
    if not arr: 
        return
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    count = [0] * range_val
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, range_val):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


entrada_base = [1, 1, 2, 4, 4, 0, 3, 3, 6, 5]
vetores_crescente = []
vetores_decrescente = []

vetor_original = entrada_base.copy()
vetor_crescente = sorted(entrada_base)
vetor_decrescente = sorted(entrada_base, reverse=True)

print("Original:  ", entrada_base)
print("Crescente:", vetor_crescente)
print("Decrescente:", vetor_decrescente)
print("\n")


print("Counting Sort - Tempo para vetores ORIGINAIS\n")
for n in range(10, 201, 10):
    entrada = entrada_base * (n // 10)
    entrada_copy = entrada.copy()
    start = time.time()
    counting_sort(entrada_copy)
    end = time.time()
    vetores_crescente.append(entrada_copy.copy())
    vetores_decrescente.append(sorted(entrada_copy.copy(), reverse=True))
    print(f"Tamanho n = {n} | Tempo original: {end - start:.6f} segundos")


print("\nCounting Sort - Tempo para vetores ordenados (crescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_crescente[i]
    vetor_copy = vetor.copy()
    start = time.time()
    counting_sort(vetor_copy)
    end = time.time()
    print(f"Tamanho n = {n} | Tempo ordenado crescente: {end - start:.6f} segundos")


print("\nCounting Sort - Tempo para vetores ordenados (decrescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_decrescente[i]
    vetor_copy = vetor.copy()
    start = time.time()
    counting_sort(vetor_copy)
    end = time.time()
    print(f"Tamanho n = {n} | Tempo ordenado decrescente: {end - start:.6f} segundos")
