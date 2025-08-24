import hashlib

login = input("Insira seu dado de login: ")
senha = input("Insira sua senha: ")

def CriptografarSenha(senha):
    senha = senha.encode()  # Senha convertida para bytes
    hash_objeto = hashlib.sha256(senha)  # Objeto que contém o cálculo do hash
    hash_hex = hash_objeto.hexdigest()  # Hash SHA-256 em formato legível
    return hash_hex

senhaarmazenada = CriptografarSenha(senha)
TentativasRestantes = 3

def ColocarSenha():
    global TentativasRestantes
    senha_input = input("Re-insira sua senha: ")
    senha_input_hash = CriptografarSenha(senha_input)

    if senha_input_hash == senhaarmazenada:
        print("Senha correta.")
    else:
        TentativasRestantes -= 1
        if TentativasRestantes > 0:
            print(f"Senha incorreta. Tentativas restantes: {TentativasRestantes}")
            ColocarSenha()
        else:
            print("Número de tentativas esgotado. Acesso negado.")

ColocarSenha()
