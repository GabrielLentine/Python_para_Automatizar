from pathlib import Path

caminho_arquivo = Path(r"Python_Automacao\12_Gerenciamento_Arquivos\teste.txt")
print(caminho_arquivo) # caminho relativo (o arquivo está no mesmo diretório que o 'caminho.py')

caminho_arquivo2 = Path(r"E:\PYTHON\Python_Basico_Aulas\Python_Automacao\12_Gerenciamento_Arquivos\teste.txt")
print(caminho_arquivo2) # caminho absoluto (o arquivo vem desde a raíz do computador)

caminho_absoluto = caminho_arquivo.absolute()
print(caminho_absoluto) # transforma o caminho relativo em absoluto (o arquivo vem desde a raíz do computador)

print(f"Caminho existe: {caminho_arquivo.exists()}") # verifica se o arquivo existe (True ou False)
print(f"Caminho existe: {caminho_arquivo2.exists()}") # verifica se o arquivo existe (True ou False)

print(f"É arquivo: {caminho_arquivo.is_file()}") # verifica se o caminho é um arquivo (True ou False)
print(f"É arquivo: {caminho_arquivo2.is_file()}") # verifica se o caminho é um arquivo (True ou False)

print(f"É diretório: {caminho_arquivo.is_dir()}") # verifica se o caminho é um diretório (True ou False)
print(f"É diretório: {caminho_arquivo2.is_dir()}") # verifica se o caminho é um diretório (True ou False)

print(f"É absoluto: {caminho_arquivo.is_absolute()}") # verifica se o caminho é absoluto (True ou False)
print(f"É absoluto: {caminho_arquivo2.is_absolute()}") # verifica se o caminho é absoluto (True ou False)

if caminho_arquivo.exists():
    print(caminho_arquivo.open().read()) # lê o arquivo e retorna o conteúdo
else:
    print("Arquivo não encontrado")

caminho_arquivo.unlink() # remove o arquivo

nova_pasta = Path("Nova_Pasta")
nova_pasta.mkdir(exist_ok=True) # cria uma nova pasta (se a pasta já existir, não cria novamente)

novas_pastas_conjuntas = Path("Pasta_1/Pasta_2/Pasta_3")
novas_pastas_conjuntas.mkdir(parents=True, exist_ok=True) # cria uma nova pasta (se a pasta já existir, não cria novamente)

nova_pasta.rmdir() # remove a pasta

iterar_pasta = Path("nome_da_pasta")
for arquivo in iterar_pasta.iterdir(): # o iterdir é usado p/ iterar sobre todos os arquivos e pastas dentro da pasta
    print(arquivo)

iterar_pasta_filtro = Path("nome_da_pasta")
for arquivo in iterar_pasta_filtro.glob("*.txt"): # o glob é usado p/ filtrar arquivos específicos (como apenas .txt, por exemplo)
    print(arquivo)
