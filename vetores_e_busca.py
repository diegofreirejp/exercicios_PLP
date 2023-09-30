# Programa em Python que receba 6 números inteiros e mostre:
# Os numeros pares digitados;
# A soma dos números pares digitados;
# Os números ímpares digitados;
# A quantidade de números ímpares

def main():
    numeros = []
    numeros_pares = []
    numeros_impares = []
    somas_pares = 0

    # Na linguagem Java, isso aqui se lê como um (for i=0; i < 6; i++){}
    for i in range(6):
        # Aqui, vai botar no vetor numeros[] um int e com uma mensagem escrito o que está no input.
        numeros.append(int(input("Digite o número: ")))

    maior_numero = numeros[0]
    menor_numero = numeros[0]

    # Aqui se lê: para cada NÚMERO no vetor NÚMEROS, fazer o seguinte:
    for numero in numeros:
        # Se esse NÚMERO tiver resto = 0,
        if numero % 2 == 0:
            # NÚMERO será adicionado ao vetor numeros_pares.
            numeros_pares.append(numero)
            # e Somas_pares vai ter o valor de NÚMERO adicionao ao seu valor.
            somas_pares += numero
        #Caso não tiver,
        else:
            # NÚMERO será adicionado ao vetor numeros_impares.
            numeros_impares.append(numero)

    for numero in numeros:
        if numero > maior_numero:
            numero == maior_numero
        if numero < menor_numero:
            numero == menor_numero

    print("Os numeros digitados foram: ")
    for numero in numeros:
        print(numero)

    print("A soma de todos os numeros pares digitados foi de: ")
    print(somas_pares)

    print("Os numeros PARES digitados foram: ")
    for numero in numeros_pares:
        print(numero)

    print("Os numeros IMPARES digitados foram: ")
    for numero in numeros_impares:
        print(numero)

    print("O maior número digitado foi: ", max(numeros))
    print("O menor número digitado foi: ", min(numeros))




if __name__ == "__main__":
    main()