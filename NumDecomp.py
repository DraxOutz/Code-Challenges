Numero = input("Digite um número que tenha até 4 dígitos: ")

# garante que é número
if not Numero.isdigit():
    print("❌ Digite apenas números.")
else:
    Numero = list(Numero)

    posicoes = {
        1: "Unidade",
        2: "Dezena",
        3: "Centena",
        4: "Unidade de milhar",
    }

    # inverte a string pra unidade ser o último dígito
    Numero = Numero[::-1]

    for i, n in enumerate(Numero, start=1):
        index = posicoes[i]
        print(f"O número {n} está na posição de {index}")
