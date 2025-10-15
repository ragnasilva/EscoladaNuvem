def verificar_senha():
    senha = input("Digite sua senha: ")

    tem_tamanho_minimo = len(senha) >= 8

    
    tem_numero = any(char.isdigit() for char in senha)

    if tem_tamanho_minimo and tem_numero:
        print("✅ Senha válida! Atende aos critérios de segurança.")
    else:
        print("❌ Senha inválida!")
        if not tem_tamanho_minimo:
            print("- A senha deve ter pelo menos 8 caracteres.")
        if not tem_numero:
            print("- A senha deve conter pelo menos um número.")


verificar_senha()