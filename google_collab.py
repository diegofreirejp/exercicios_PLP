# Programa 01 - Linguagem Python - Programação Estruturada
# Autor: Diego Freire Farias - Data: 18.08.2023 - Linguagem: Python

# NOTA 29.09:. Nesse arquivo estão todos os programas que fizemos no google collab no dia 18.09

# Leitura dos Dados
Nota1 = (float(input("Informe o valor da primeira nota: ")))
Nota2 = (float(input("Informe o valor da segunda nota: ")))

# Calcular a Média das Notas.
Med = (Nota1+Nota2) / 2

if (Med < 7):
    Rep = "Aprovado"
else:
    Rep = "Reprovado"

    print("Você foi ", Rep)
    print(" com a média ", Med)
    
# Funçoes

def calcMedia(n1, n2):
    return (n1 + n2) / 2

def verifSit(Med):
    if (Med >= 7):
        return "Aprovado"
    else:
        return "Reprovado"

    # Leitura dos Dados
    Nota1 = (float(input("Informe o valor da primeira nota: ")))
    Nota2 = (float(input("Informe o valor da segunda nota: ")))

    # Calcular a Média das Notas.
    media = calcMedia(Nota1, Nota2)
    resp = verifSit(media)

    print("A sua média foi ", media)
    print("E a sua situação é ", resp)


  # Leitura dos Dados
produto = (float(input("Informe o valor do produto: ")))
desconto = (float(input("Informe o valor do desconto em porcentagem: ")))

novoDesc = desconto / 100

valorDesc = produto * novoDesc
valorProduto = produto - valorDesc

print("O valor a se pagar é: ", valorProduto)


cigarros = (float(input("Quantos cigarros o fumante em questão fuma por dia? ")))
anosFumando = (float(input("Por quantos anos ele já fumou? ")))

def DiasPerdidos(cig, anos):
  dias = anos * 365
  cigTotal = cigarros * dias
  tempoPerdidoMin = cigTotal * 10;
  tempoPerdidoHr = tempoPerdidoMin/60
  tempoPerdidoDia = tempoPerdidoHr/24
  return tempoPerdidoDia

tempo = DiasPerdidos(cigarros, anosFumando)
if(tempo>366):
  tempoAnos = tempo/365
  print("O fumante em questão perdeu", tempoAnos, " anos de vida")
else:
  print("O fumante em questão perdeu ", tempo, " dias de vida.")
