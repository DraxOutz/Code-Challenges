Usuarios = {
    "Ryan": "Senha123"
}

Tentativas = 3

Usuario = input("Digite seu nome de usuário: ")

if Usuario in Usuarios:
    while Tentativas > 0:
        Senha = input("Digite sua senha: ")
        if Senha == Usuarios[Usuario]:
            print("Login realizado com sucesso!")
            break
        else:
            Tentativas -= 1
            print(f"Senha incorreta, tentativas restantes: {Tentativas}")
    else:
        print("Você excedeu o número de tentativas.")
else:
    print("Usuário não existe.")
