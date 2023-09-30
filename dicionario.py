def main():


    #cria um dicionário vazio
    dicionario = {}

    #le os dados da agenda
    while True:
        cpf = input("Digite o CPF: ")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        telefone = input("Digite o telefone: ")

        # adiciona os dados ao dicionario
        dicionario[cpf] = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone,
        }

        # pergunta se o usuario deseja continuar
        continuar = input("Deseja continuar? (s/n): ")
        if continuar != "s":
            break

    # Imprime os itens do dicionario
    for cpf, contato in dicionario.items():
        print(cpf, contato["nome"], contato["idade"], contato["telefone"])


if __name__ == "__main__":
    main()