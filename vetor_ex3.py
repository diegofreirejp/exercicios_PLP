def main():

    vetorA = []
    vetorB = []
    vetorC = []

    for i in range(3):
        vetorA.append(int(input("Digite o número que deseja inserir na posição do vetor A ")))
        vetorB.append(int(input("Digite o número que deseja inserir na posição do vetor B ")))

    for i in range(3):
        vetorC.append(vetorA[i] - vetorB[i])

    for elementos in vetorC:
        print(elementos)



if __name__ == "__main__":
    main()