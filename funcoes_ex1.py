
def main():
    A = int(input("Digite o número A: "))
    B = int(input("Digite o número B: "))

    resultado = soma(A, B)

    print(resultado)

def soma(numero1, numero2):
    adicao = numero1 + numero2
    return adicao


if __name__ == "__main__":
    main()