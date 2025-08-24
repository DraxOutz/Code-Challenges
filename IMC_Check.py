import math

Peso = float(input("Digite seu peso (kg): "))
Altura = float(input("Digite sua altura (cm): ")) / 100  

IMC = Peso / (Altura ** 2)

Valores = {
    1: "Abaixo do peso",
    2: "Peso normal",
    3: "Sobrepeso",
    4: "Obesidade"
}

Calculo = math.ceil((IMC - 18.5) / 5) + 1
Calculo = max(1, min(Calculo, 4))
Valor = Valores[Calculo]

print(f"Seu IMC é {IMC:.2f}, você está {Valor}")
