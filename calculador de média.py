def calcular_media():
    """Calcula a média aritmética de números fornecidos pelo usuário."""
    numeros = []
    
    print("=== CALCULADORA DE MÉDIA ===")
    print("Digite os números (pressione Enter sem digitar nada para calcular)")
    
    while True:
        entrada = input("Digite um número: ").strip()
        
        if entrada == "":
            break
        
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Erro! Digite um número válido.")
    
    if not numeros:
        print("Nenhum número foi digitado!")
        return
    
    media = sum(numeros) / len(numeros)
    
    print(f"\n--- Resultado ---")
    print(f"Números digitados: {numeros}")
    print(f"Quantidade: {len(numeros)}")
    print(f"Soma: {sum(numeros)}")
    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    calcular_media()