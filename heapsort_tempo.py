import time

def heapify(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and arr[esq] > arr[maior]:
        maior = esq
    if dir < n and arr[dir] > arr[maior]:
        maior = dir
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # troca
        heapify(arr, i, 0)


entrada_base = [10,-74,-4,-38,-90,16,28,65,-55,19]
vetores_crescente = []
vetores_decrescente = []

vetor_original = entrada_base.copy()
vetor_crescente = sorted(entrada_base)
vetor_decrescente = sorted(entrada_base, reverse=True)

print("Original:  ", entrada_base)
print("Crescente:", vetor_crescente)
print("Decrescente:", vetor_decrescente)
print("\n")


print("Heap Sort - Tempo para vetores ORIGINAIS\n")
for n in range(10, 201, 10):
    entrada = entrada_base * (n // 10)
    entrada_copy = entrada.copy()
    start = time.time()
    heap_sort(entrada_copy)
    end = time.time()
    vetores_crescente.append(entrada_copy.copy())
    vetores_decrescente.append(sorted(entrada_copy.copy(), reverse=True))
    print(f"Tamanho n = {n} | Tempo original: {end - start:.6f} segundos")


print("\nHeap Sort - Tempo para vetores ORDENADOS (crescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_crescente[i]
    vetor_copy = vetor.copy()
    start = time.time()
    heap_sort(vetor_copy)
    end = time.time()
    print(f"Tamanho n = {n} | Tempo ordenado crescente: {end - start:.6f} segundos")


print("\nHeap Sort - Tempo para vetores ORDENADOS (decrescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_decrescente[i]
    vetor_copy = vetor.copy()
    start = time.time()
    heap_sort(vetor_copy)
    end = time.time()
    print(f"Tamanho n = {n} | Tempo ordenado decrescente: {end - start:.6f} segundos")
