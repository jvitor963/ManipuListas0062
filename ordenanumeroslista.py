# ordena números em lista
numeros = [43,54,22,56,4,6]
print("Lista Original:")
for n in numeros:
    print(n,end=" ")
print("\n_________________")
print("Lista Crescente:")
numeros.sort()
for n in numeros:
    print(n,end=" ")
    print("\n______________")
print("Lista Decrescente:")
numeros.sort(reverse=True)
for n in numeros:
    print(n,end=" ")
    print("\n______________")