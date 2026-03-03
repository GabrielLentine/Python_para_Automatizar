fruta = "Melancia"
print(fruta[0]) # M
print(fruta[-1]) # a (de trás pra frente)
print(fruta[0:3]) # 'Mel' (os três primeiros caracteres)
print(fruta[:6]) # 'Melanc' (os seis primeiros caracteres)

frase = "Eu amo Python!"
frase_tamanho = len(frase) # tamanho (em caracteres) da string
print(f"A frase '{frase}' tem {frase_tamanho} caracteres.")

print(frase.count("o")) # 2 (duas vezes que 'o' aparece na frase)
print(frase.find("m")) # 4 (sempre vai retornar a primeira ocorrência)

if 'Python' in frase:
    print("'Python' está na frase")
else:
    print("'Python' não está na frase")

print(frase.lower()) # tudo em minúsculo
print(frase.upper()) # tudo em maiúsculo
print(frase.capitalize()) # primeira letra em maiúscula
print(frase.strip()) # remove espaços laterais
print(frase.replace("o", "x")) # troca uma letra (primeira "") por outra (segunda "")
print(frase.title()) # a primeira letra de cada palavra em maiúscula
