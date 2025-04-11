# Bibliotecas
import textwrap

# Algoritmo

# Variáveis

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    valor_deposito = int(input("Insira o valor (R$): "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    else:
        print("Valor inválido. Insira um valor positivo.")

def sacar():
    global saldo, limite, numero_saques, extrato

    valor_saque = int(input("Insira o valor (R$): "))

    if valor_saque > saldo:
        print("Saque não autorizado, saldo insuficiente.")
    elif valor_saque > limite:
        print("Saque não autorizado, limite de R$ 500,00 por saque.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Saque não autorizado, limite de saque diário é de 3 saques por dia.")
    elif valor_saque <= 0:
        print("Saque não autorizado, valor inválido.")
    else:
        saldo -= valor_saque
        numero_saques += 1
        print(f"Você selecionou o valor R${valor_saque:.2f}. Efetuando o saque... Saque autorizado.")
        extrato.append(f"Saque:    R$ {valor_saque:.2f}")

def mostrar_extrato():
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Nenhuma movimentação registrada.")
    print(f"Seu saldo atual é: R$ {saldo:.2f}")
    print(f"Saques restantes hoje: {LIMITE_SAQUES - numero_saques}")

def main():
    start = textwrap.dedent("""\
            Iniciando sistema bancário.
    """)

    menu = textwrap.dedent("""\
        \nPor favor selecione uma das opções para prosseguir:

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair

        => """)

    print(start)

    while True:
        escolha = int(input(menu))

        if escolha == 1:
            print("Opção de depósito selecionada.")
            depositar()

        elif escolha == 2:
            print("Opção de saque selecionada.")
            sacar()

        elif escolha == 3:
            print("Opção de extrato selecionada.")
            mostrar_extrato()

        elif escolha == 4:
            print("Obrigado por utilizar nosso sistema.")
            break

        else:
            print("Opção inválida.")

main()
