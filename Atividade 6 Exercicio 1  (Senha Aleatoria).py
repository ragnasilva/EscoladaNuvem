import random
import string

def gerar_senha(tamanho):
    
    caracteres = string.ascii_letters + string.digits + string.punctuation

   
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


print("=== GERADOR DE SENHAS SEGURAS ===")
tamanho = int(input("Digite o tamanho desejado para a senha: "))

senha_gerada = gerar_senha(tamanho)
print(f"Sua senha segura é: {senha_gerada}")