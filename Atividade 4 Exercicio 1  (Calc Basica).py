def calculadora():
    print("=== Calculadora Simples ===")
    print("Operações disponíveis:")
    print("+ para Adição")
    print("- para Subtração")
    print("* para Multiplicação")
    print("/ para Divisão")

  
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero não é permitida.")
            return
    else:
        print("Operação inválida.")
        return

    print(f"Resultado: {resultado}")


calculadora()