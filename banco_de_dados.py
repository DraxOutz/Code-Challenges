import sqlite3

# Cria o banco de dados com esse nome se não existir, ou abre se já existir.
banco = sqlite3.connect("database.db")
cursor = banco.cursor()

# cria tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    senha BLOB NOT NULL
)   
""")

# Criar um novo usuario
def Create_User(Email, Senha):  
    try:
        cursor.execute(
            "INSERT INTO usuarios (email, senha) VALUES (?, ?)",
            (Email, Senha)
        )
        banco.commit()
    except sqlite3.IntegrityError:
        print("⚠️ Usuário já existe!")
    except Exception as e:
        print("Erro ao criar usuário:", e)

# Criar uma nova coluna se necessário
def CreateNewData(Nome, Valor):
    try:
        cursor.execute(f"ALTER TABLE usuarios ADD COLUMN {Nome} TEXT DEFAULT '{Valor}'")
        banco.commit()
    except sqlite3.OperationalError:
        pass  # coluna já existe

# Checar algum dado na tabela
def Check_Data(email, data):
    cursor.execute(f"SELECT {data} FROM usuarios WHERE email = ?", (email,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return False


def user_exists(email):
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    result = cursor.fetchone()  # pega a primeira linha
    
    banco.close()
    
    return result is not None  # True se existe, False se não

# Atualizar dado
def Update_Data(Email, data, Value):
    cursor.execute(
        f"UPDATE usuarios SET {data} = ? WHERE email = ?",
        (Value, Email)
    )
    banco.commit()

# banco.close() só no fim do programa
