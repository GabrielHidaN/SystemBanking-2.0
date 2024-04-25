import textwrap
import os
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [c]\tNova conta
    [l]\tListar contas
    [u]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    os.system('cls')
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo , extrato

def sacar (*, saldo, valor,extrato, limite, numero_saques, limite_saques ):
    os.system('cls')
    if numero_saques < limite_saques:
        if valor > 0 and valor <= limite:
            if valor <= saldo:
                saldo -= valor
                extrato += f"Saque:  R$ {valor:.2f}\n"
                print("\n=== Saque realizado com sucesso! ===")
                numero_saques += 1

            else:
                print("\n@@@ Operação falhou! Saldo Insuficiente Para concluir essa  Operação. @@@")
        else:
            if valor < 0:
                print("\n@@@ Operação falhou! O valor informado é inválido , O  Valor deve ser maior que R$ 0,00 . @@@")
            elif valor > 500:
                print("\n@@@ Operação falhou! O valor informado é inválido , O  valor deve ser abaixo de R$ 500,00 . @@@")
    else:
        print("\n@@@ Você Não tem Mais Saques Disponiveis Hoje. Volte amanhã e tente Novamente!")
    return saldo , extrato , numero_saques

def exibir_extrato(saldo , / , * , extrato):
    os.system('cls')
    saldo = saldo
    saldoTotal = f'Seu Saldo Atual é R$ {saldo:.2f} \n'
    return   saldoTotal , extrato
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 500
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato  = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato , numero_saques = sacar(saldo=saldo , valor=valor , extrato= extrato , limite= limite , numero_saques= numero_saques, limite_saques= LIMITE_SAQUES)

        elif opcao == 'e':
            if len(extrato) == 0:
                print('sem extrato')
            else:
                extratos = exibir_extrato(saldo , extrato= extrato)
                extratos = list(extratos)
                for  i in extratos:
                    print(i)



main()
