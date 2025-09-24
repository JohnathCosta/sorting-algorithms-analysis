import time

def insertion_sort_str(arr):
    start = time.time()
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    end = time.time()
    return arr, end - start

base = ['J', 'O', 'H', 'N', 'A', 'T', 'H', 'S', 'I', 'L']

vetor_original = base.copy()
vetor_crescente = sorted(base)
vetor_decrescente = sorted(base, reverse=True)

print("Original:  ", vetor_original)
print("Crescente:", vetor_crescente)
print("Decrescente:", vetor_decrescente)
print("\n")


print("Insertion Sort - Tempo para vetores ORIGINAIS (caracteres aleatórios)\n")
for n in range(10, 201, 10):
    vetor = base * (n // 10)
    _, tempo = insertion_sort_str(vetor.copy())
    print(f"Tamanho n = {n} | Tempo original: {tempo:.8f} segundos")


print("\nInsertion Sort - Tempo para vetores ordenado (crescente)\n")
for n in range(10, 201, 10):
    vetor = sorted(base * (n // 10))
    _, tempo = insertion_sort_str(vetor.copy())
    print(f"Tamanho n = {n} | Tempo ordenado crescente: {tempo:.8f} segundos")


print("\nInsertion Sort - Tempo para vetores ordenado (decrescente)\n")
for n in range(10, 201, 10):
    vetor = sorted(base * (n // 10), reverse=True)
    _, tempo = insertion_sort_str(vetor.copy())
    print(f"Tamanho n = {n} | Tempo ordenado decrescente: {tempo:.8f} segundos")
