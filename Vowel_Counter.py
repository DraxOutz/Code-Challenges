Palavra = input("Digite uma palavra: ").upper()  
Vogais = 0

Letras = {"A", "E", "I", "O", "U"}  

for txt in Palavra:
    if txt in Letras:
        Vogais += 1

print(f"A palavra: {Palavra} possui {Vogais} vogais.")
