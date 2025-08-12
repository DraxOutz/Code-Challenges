Palavra = input("Digite para verificar se a String tem números.")
Tem_Numero = "não possui"

for txt in Palavra:
    if txt.isdigit():
        Tem_Numero = "possui"
        break  # Para o loop assim que achar um número

print(f"A palavra: {Palavra} {Tem_Numero} número.")
