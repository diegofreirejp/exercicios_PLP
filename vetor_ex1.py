def main():
    #vetor = ["onça", "leão", "tigre"]
    #vetor2 = []

    #print(vetor[2])

    #for i in range(4):
    #    vetor2.append(input("Digite o nome do animal: "))
    #print(vetor[2])

    #for elementos in vetor2:
    #    print(elementos)

    # lê um vetor de 8 posições e, em seguida, lê dois valores X e Y quaisquer correspondentes a duas posições no vetor
    # . O programa então imprime a soma dos valores encontrados nas respectivas posições X e Y.

    vetor = [0] * 8

    for i in range(8):
        vetor.append(int(input("Digite o valor a ser colocado: ")))

    x = int(input("Digite um valor x de 1 a 8: "))
    y = int(input("Digite um valor y de 1 a 8: "))

    soma = vetor[x] + vetor[y]

    print(soma)


if __name__ == "__main__":
    main()