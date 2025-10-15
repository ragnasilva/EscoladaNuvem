from datetime import datetime

data_atual = datetime(2025, 10, 11)

data_nascimento_str = input("Digite sua data de nascimento (formato DD/MM/AAAA): ")

data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

dias_vividos = (data_atual - data_nascimento).days

print(f"Você está vivo há {dias_vividos} dias.")