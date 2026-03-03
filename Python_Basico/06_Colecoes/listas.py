frutas = ["Maçã", "Banana", "Laranja", "Pera"]
print(frutas[1]) # Banana
print(frutas[-1]) # Pera

frutas.append("Melancia") # adicionando algo a mais dentro de uma lista
print(frutas[-1]) # Melancia

frutas.remove("Melancia") # removendo algo dentro de uma lista
print(frutas)

print(len(frutas)) # 4

frutas.insert(1, "Uva") # inserir a uva no Index 1, mas sem substituir a "Banana"

fruta_removida = frutas.pop(0) # remove e retorna itens através do Index
print(f"A fruta {fruta_removida} foi removida.")
print(frutas)

frutas.sort() # ordenar uma lista (por padrão, em ordem alfabética)
print(frutas)

print(frutas.index("Banana")) # retorna o Index de determinado valor (se ele estiver na lista)

print(frutas.count("Maçã")) # quantidade de itens dentro de uma lista (no caso, o valor é 1)

frutas2 = frutas.copy()
frutas2.append("Caju")
frutas2.append("Limão")
print(frutas2)
print(frutas)

frutas.clear() # limpar a lista
frutas2.clear() # limpar a lista
