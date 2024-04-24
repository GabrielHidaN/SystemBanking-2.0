import textwrap

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
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo , extrato

def sacar (*, saldo, valor,extrato, limite, numero_saques, limite_saques ):
    if numero_saques < limite_saques:
        if valor > 0 and valor <= limite:
            if valor <= saldo:
                saldo -= valor
                extrato += f"Saque:\tR$ {valor:.2f}\n"
                print("\n=== Saque realizado com sucesso! ===")
            else:
                print("\n@@@ Operação falhou! Saldo Insuficiente Para concluir essa  Operação. @@@")
        else:
            if valor < 0:
                print("\n@@@ Operação falhou! O valor informado é inválido , O  Valor deve ser maior que R$ 0,00 . @@@")
            elif valor > 500:
                print("\n@@@ Operação falhou! O valor informado é inválido , O  valor deve ser abaixo de R$ 500,00 . @@@")
    else:
        print("\n@@@ Você Não tem Mais Saques Disponiveis Hoje. Volte amanhã e tente Novamente!")
    return saldo , extrato

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 500
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques_diarios = 3
    usuarios = []
    contas = []
    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        if opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo , valor=valor , extrato= extrato , limite= limite , numero_saques= numero_saques, limite_saques= limite_saques_diarios)


main()
