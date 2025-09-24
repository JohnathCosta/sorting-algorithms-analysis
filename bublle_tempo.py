import time

def bubble_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end = time.time()
    return arr, end - start

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


print("Bubble Sort - Tempo para vetores originais\n")
for n in range(10, 201, 10):
    entrada = entrada_base * (n // 10)
    ordenado, tempo = bubble_sort(entrada.copy())
    vetores_crescente.append(ordenado.copy())
    vetores_decrescente.append(sorted(ordenado.copy(), reverse=True))
    print(f"Tamanho n = {n} | Tempo original: {tempo:.6f} segundos")


print("\nBubble Sort - Tempo para vetores ordenados(crescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_crescente[i]
    _, tempo = bubble_sort(vetor.copy())
    print(f"Tamanho n = {n} | Tempo ordenado crescente: {tempo:.6f} segundos")


print("\nBubble Sort - Tempo para vetores ordenados(decrescente)\n")
for i, n in enumerate(range(10, 201, 10)):
    vetor = vetores_decrescente[i]
    _, tempo = bubble_sort(vetor.copy())
    print(f"Tamanho n = {n} | Tempo ordenado decrescente: {tempo:.6f} segundos")


