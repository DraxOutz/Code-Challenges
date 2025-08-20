import os #Serve pra interagir com o sistema operacional
import shutil #Serve pra mover, copiar ou deletar arquivos e pastas de forma prática.

# Pasta que você quer organizar
Pasta = r"C:\Users\Ryan\Downloads"

# Onde vão ficar os arquivos organizados
pastas_destino = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Vídeos": [".mp4", ".mkv", ".avi"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Músicas": [".mp3", ".wav"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Outros": []  # Caso não entre em nenhuma categoria
}

def organizar_arquivos(pasta):
    # Cria as pastas de destino se não existirem
    for nome in pastas_destino.keys(): # Cria o caminho completo da pasta
        caminho = os.path.join(pasta, nome)
        if not os.path.exists(caminho): # Verifica se a pasta já existe
            os.makedirs(caminho) # Se não existe, cria a pasta

    # Percorre todos os arquivos da pasta
    for arquivo in os.listdir(pasta): # Lista todos os itens da pasta
        caminho_arquivo = os.path.join(pasta, arquivo)  # Caminho completo do arquivo

        # Ignora pastas
        if os.path.isdir(caminho_arquivo):
            continue # Pula para o próximo item

        _, extensao = os.path.splitext(arquivo) # Divide o nome e a extensão
        extensao = extensao.lower()  # Transforma em minúscula pra evitar erros

        movido = False # Variável pra saber se o arquivo já foi movido
        for nome, extensoes in pastas_destino.items():
            if extensao in extensoes:
                destino = os.path.join(pasta, nome, arquivo)
                shutil.move(caminho_arquivo, destino)  # Move o arquivo
                print(f"Movido: {arquivo} → {nome}")  # Mostra no terminal
                movido = True
                break  # Sai do loop, já encontrou a categoria

        # Se não entrou em nenhuma categoria, joga em "Outros"
        if not movido:
            destino = os.path.join(pasta, "Outros", arquivo)
            shutil.move(caminho_arquivo, destino)
            print(f"Movido: {arquivo} → Outros")

organizar_arquivos(Pasta)