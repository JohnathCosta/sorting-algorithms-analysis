import time

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        L = arr[:meio]
        R = arr[meio:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


entrada_base = [50, 60, 61, 46, 85, 18, 52, 84, 85, 68] 
vetores_crescente = []
vetores_decrescente = []

vetor_original = entrada_base.copy()
vetor_crescente = sorted(entrada_base)
vetor_decrescente = sorted(entrada_base, reverse=True)

print("Original:  ", entrada_base)
print("Crescente:", vetor_crescente)
print("Decrescente:", vetor_decrescente)
print("\n")


print("Merge Sort - Tempo para vetores ORIGINAIS\n")
for n in range(10, 201, 10):
    entrada = entrada_base * (n // 10)
    entrada_copy = entrada.copy()
    start = time.time()
    merge_sort(entrada_copy)
    end = time.time()
    vetores_crescente.append(entrada_copy.copy())
    vetores_decrescente.append(sorted(entrada_copy.copy(), reverse=True))
    print(f"Tamanho n = {n} | Tempo original: {end - start:.6f} segundos")


print("\n Merge Sort - Tempo para vetores ordenados (crescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_crescente[i]
    vetor_copy = vetor.copy()
    start = time.time()
    merge_sort(vetor_copy)
    end = time.time()
    print(f"Tamanho n = {n} | Tempo ordenado crescente: {end - start:.6f} segundos")


print("\nMerge Sort - Tempo para vetores ordenados (decrescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_decrescente[i]
    vetor_copy = vetor.copy()
    start = time.time()
    merge_sort(vetor_copy)
    end = time.time()
    print(f"Tamanho n = {n} | Tempo ordenado decrescente: {end - start:.6f} segundos")
