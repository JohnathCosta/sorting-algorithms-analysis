import time

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  #pivo último elemento
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

entrada_base = [ ]
vetores_crescente = []
vetores_decrescente = []

vetor_original = entrada_base.copy()
vetor_crescente = sorted(entrada_base)
vetor_decrescente = sorted(entrada_base, reverse=True)

print("Original:  ", entrada_base)
print("Crescente:", vetor_crescente)
print("Decrescente:", vetor_decrescente)
print("\n")


print("Quick Sort - Tempo para vetores ORIGINAIS\n")
for n in range(10, 201, 10):
    entrada = entrada_base * (n // 10)
    entrada_copy = entrada.copy()
    start = time.time()
    quick_sort(entrada_copy, 0, len(entrada_copy) - 1)
    end = time.time()
    vetores_crescente.append(entrada_copy.copy())
    vetores_decrescente.append(sorted(entrada_copy.copy(), reverse=True))
    print(f"Tamanho n = {n} | Tempo original: {end - start:.6f} segundos")


print("\nQuick Sort - Tempo para vetores ordenados (crescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_crescente[i]
    vetor_copy = vetor.copy()
    start = time.time()
    quick_sort(vetor_copy, 0, len(vetor_copy) - 1)
    end = time.time()
    print(f"Tamanho n = {n} | Tempo ordenado crescente: {end - start:.6f} segundos")


print("\nQuick Sort - Tempo para vetores ordenados (decrescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_decrescente[i]
    vetor_copy = vetor.copy()
    start = time.time()
    quick_sort(vetor_copy, 0, len(vetor_copy) - 1)
    end = time.time()
    print(f"Tamanho n = {n} | Tempo ordenado decrescente: {end - start:.6f} segundos")
