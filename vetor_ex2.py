def main():
# Faça um programa em Python que receba do usuario
# um vetor com 10 posições. Em seguida devera ser
# impresso o maior e o menor elemento do vetor.

    vetor = []

    for i in range(10):
        vetor.append(int(input("Digite o número que você quer inserir no vetor.")))

    maior_elemento = vetor[0]
    menor_elemento = vetor[0]
    for elemento in vetor:
        if (elemento > maior_elemento):
            maior_elemento = elemento
        if (elemento < menor_elemento):
            menor_elemento = elemento


    print("Esse é o menor elemento: ", menor_elemento)
    print("Esse é o maior elemento: ", maior_elemento)



if __name__ == "__main__":
    main()