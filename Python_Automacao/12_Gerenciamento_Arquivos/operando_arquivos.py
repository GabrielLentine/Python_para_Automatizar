from pathlib import Path  # Importa Path para montar caminhos de forma segura.
import shutil  # Importa shutil para usar a função de cópia de arquivos.

base = Path(__file__).parent  # Pega a pasta onde este arquivo .py está.
origem = base / "teste.txt"  # Define o caminho completo do arquivo de origem.
destino_dir = base / "backup"  # Define o caminho da pasta de destino (backup).
destino_dir.mkdir(exist_ok=True)  # Cria a pasta backup caso ela ainda não exista.
destino = destino_dir / "teste_backup.txt"  # Define o caminho completo do arquivo copiado.

shutil.copy(origem, destino)  # Copia o arquivo de origem para o destino.
print(f"Copiado para: {destino}")  # Exibe no terminal onde o arquivo foi salvo.