# mostre o primeiro e o último elemento de uma lista
lista_animais = "Cachorro", "Gato", "Ovelha"
print(lista_animais[0])
print(lista_animais[-1])

# Adicione, Remova, Troca e Tamanho
lista_livros_programacao = ["Python", "Java", "C++"]

lista_livros_programacao.append("JavaScript")
print(lista_livros_programacao)

lista_livros_programacao.remove("Java")
print(lista_livros_programacao)

lista_livros_programacao[0] = "Go"
print(lista_livros_programacao)

print(len(lista_livros_programacao))

# Ocorrências e Índice
lista_nomes = [ "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Giovana", "Hugo", "Isabela", "João", "Carla",
          "Lucas", "Mariana", "Nuno", "Olivia", "João", "Pedro", "Carla", "Rafael", "Ana" ]

print(lista_nomes.count("Carla"))
print(lista_nomes.index("Carla"))
