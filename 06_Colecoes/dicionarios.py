pessoa = {
    "nome": "Gabriel",
    "idade": 19,
    "cidade": "São Paulo",
    "profissoes": ["Programador", "Editor"]
}
print(pessoa) # Gabriel, 19, São Paulo

print(pessoa["nome"]) # Gabriel

# del pessoa["cidade"] # removendo a cidade
# print(pessoa)

print(pessoa["profissoes"]) # somente as profissões
print(pessoa["profissoes"][0]) # Programador

pessoa["profissoes"].append("Jovem Aprendiz")
print(pessoa["profissoes"])

print(pessoa.keys()) # nome, idade, cidade, profissões
print(pessoa.values()) # [Gabriel, 19, [Programador, Editor, Jovem Aprendiz]]

valores = list(pessoa.values())
print(valores[1]) # 19

print(pessoa.items()) # retorna chaves-valores (ótimo p/ loops)

print(pessoa.get("telefone", "Não existe")) # "Não existe" caso não houve a chave telefone
