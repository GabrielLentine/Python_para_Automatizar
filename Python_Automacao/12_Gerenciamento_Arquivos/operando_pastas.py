from pathlib import Path # monta caminhos
import shutil # cópia de pastas, zip, extração

base = Path(__file__).parent # pasta do script
origem = base / "meus_arquivos" # pasta a copiar
destino_dir = base / "meus_arquivos_backup"  # backup no disco

shutil.copytree(origem, destino_dir, dirs_exist_ok=True) # copia pasta inteira
print(f"Pasta copiada para: {destino_dir}")

arquivo_teste = base / "teste.txt" # arquivo ao lado do .py
shutil.move(arquivo_teste, destino_dir) # move para o backup
print(f"Arquivo movido para: {destino_dir / arquivo_teste.name}")

deletar_pasta = base / "meus_arquivos" # pasta original
shutil.rmtree(deletar_pasta, True) # apaga pasta e conteúdo; True ignora erros
print(f"Pasta deletada: {deletar_pasta}")

nome_arquivo_zip = base / "meus_arquivos_backup" # nome do .zip sem extensão
shutil.make_archive(
    str(nome_arquivo_zip),# caminho base do zip (sem .zip)
    "zip", # formato
    root_dir=str(base), # pasta raiz dos caminhos
    base_dir="meus_arquivos_backup", # subpasta que entra no zip
)
caminho_zip = nome_arquivo_zip.with_suffix(".zip") # caminho completo do .zip
print(f"ZIP criado: {caminho_zip}")

pasta_extraida = base / "meus_arquivos_backup_extraido" # onde extrair
pasta_extraida.mkdir(parents=True, exist_ok=True) # cria se não existir
shutil.unpack_archive(caminho_zip, extract_dir=str(pasta_extraida)) # descompacta
print(f"ZIP extraído em: {pasta_extraida}")
