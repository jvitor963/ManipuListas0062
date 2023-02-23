# remove iten da lista
pendencias = ["exercitar", "estudar", "limpar", "escovar", "beber"]
print("Relação de pendências: ",pendencias)
print("-" * 80)
item = input("Digite a pendência a remover: ")
pendencias.remove(item)
print("Pendências atuais: ",pendencias)