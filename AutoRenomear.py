import os
import shutil

Pasta = r"C:\Users\Ryan\Downloads\RenomearArquivos" #Pasta Local
Number = 1
Nome_Escolhido = "Teste"

print(os.listdir(Pasta)) #Pastas presentes no sistema

for item in os.listdir(Pasta):
    caminho_antigo = os.path.join(Pasta, item) #Caminho Antigo
    print(caminho_antigo)
    if os.path.isfile(caminho_antigo): #Verificar se não é uma pasta
        nome, extensao = os.path.splitext(item) #Dividir o formato e o nome
        novo_nome = Nome_Escolhido + str(Number) + extensao #Novo nome do arquivo + extensão
        caminho_novo = os.path.join(Pasta, novo_nome) #Novo local do arquivo
        os.rename(caminho_antigo, caminho_novo) #Renomear arquivo
        Number += 1 #Adicionar +1
        
