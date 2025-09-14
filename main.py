from calculator import somar, subtrair, multiplicar, dividir

def menu():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

def main():
    menu()
    escolha = input("Digite a opção (1/2/3/4): ")

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", somar(a, b))
    elif escolha == '2':
        print("Resultado:", subtrair(a, b))
    elif escolha == '3':
        print("Resultado:", multiplicar(a, b))
    elif escolha == '4':
        try:
            print("Resultado:", dividir(a, b))
        except ValueError as e:
            print("Erro:", e)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
