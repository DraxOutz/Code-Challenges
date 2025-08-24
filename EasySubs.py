from datetime import datetime

# -----------------------------
# Sistema de Assinaturas
# -----------------------------

# "Banco de dados" simples em memória
subscriptions = {}

# Funções principais
def add_subscription(user: str, plan: str):
    """Adiciona uma assinatura para o usuário."""
    if user in subscriptions:
        print(f"❌ Usuário '{user}' já possui uma assinatura ativa.")
        return
    subscriptions[user] = {
        "plano": plan,
        "criado_em": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    print(f"✅ Assinatura adicionada para {user} no plano {plan}.")


def delete_subscription(user: str):
    """Remove a assinatura de um usuário."""
    if user not in subscriptions:
        print(f"❌ Usuário '{user}' não possui assinatura.")
        return
    del subscriptions[user]
    print(f"🗑️ Assinatura de {user} removida com sucesso.")


def list_subscriptions():
    """Lista todas as assinaturas ativas."""
    if not subscriptions:
        print("📭 Nenhuma assinatura encontrada.")
        return
    print("\n📋 Assinaturas Ativas:")
    for user, data in subscriptions.items():
        print(f" - {user} | Plano: {data['plano']} | Criado em: {data['criado_em']}")
    print()


def update_subscription(user: str, new_plan: str):
    """Atualiza o plano de assinatura de um usuário."""
    if user not in subscriptions:
        print(f"❌ Usuário '{user}' não possui assinatura.")
        return
    subscriptions[user]["plano"] = new_plan
    print(f"🔄 Assinatura de {user} atualizada para o plano {new_plan}.")


# Dicionário de eventos (menu de ações)
Eventos = {
    1: add_subscription,
    2: delete_subscription,
    3: list_subscriptions,
    4: update_subscription
}


# -----------------------------
# Exemplo de uso (simulação)
# -----------------------------
if __name__ == "__main__":
    # Simulando entradas do usuário
    Eventos[1]("Ryan", "Premium")   # adicionar
    Eventos[1]("Lorena", "Básico")  # adicionar
    Eventos[3]()                    # listar
    Eventos[4]("Ryan", "Gold")      # atualizar
    Eventos[3]()                    # listar novamente
    Eventos[2]("Lorena")            # deletar
    Eventos[3]()                    # listar novamente
