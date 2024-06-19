import textwrap
import os
from datetime import datetime

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

def validar_cpf(cpfEnviado):

    resultado_digito_1 = 0

    cpfEnviado = cpfEnviado
    flag_cpf = None
    try:
        int(cpfEnviado)
        flag_cpf = True
    except ValueError:
        flag_cpf = None
        print('@@@ Cpf inválido! O Cpf deve conter esse formato [ 95946473026 ]')

    except:
        print('@@@ ERROR desconhecido @@@')
        flag_cpf = None

    if flag_cpf is True:

        noveDigitos = cpfEnviado[:9]

        regressar1 = 10
        for digito in noveDigitos:
          resultado_digito_1 += int(digito) * int(regressar1)
          regressar1 -= 1
        primeiroDigito = (resultado_digito_1 * 10) % 11

        primeiroDigito = primeiroDigito if primeiroDigito <= 9 else 0



        dezDigitos = noveDigitos + str(primeiroDigito)
        regressar2 = 11

        resultado2 = 0

        for digito in dezDigitos:
          resultado2 += int(digito) * regressar2
          regressar2 -= 1
        segundoDigito = (resultado2 * 10) % 11
        segundoDigito= segundoDigito if segundoDigito <= 9 else 0

        cpfGerado = f'{noveDigitos}{primeiroDigito}{segundoDigito}'


        if cpfEnviado == cpfGerado :
          valido = True
        else:
          valido = False

        return valido


def depositar(saldo, valor, extrato,data_e_hora_atuais, /):
    os.system('cls')

    if valor > 0:
        saldo += valor

        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("‘%d/%m/%Y %H:%M’")

        extrato += f'''
        ======================================================================
        Depósito:  R$ {valor:.2f}    Data e Hora Realizado: {data_e_hora_em_texto}
        ======================================================================
        '''

        print("\n=== Depósito realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo , extrato

def sacar (*, saldo, valor,extrato, limite, numero_saques, limite_saques,data_e_hora_atuais ):
    os.system('cls')

    if numero_saques < limite_saques:
        if valor > 0 and valor <= limite:
            if valor <= saldo:
                saldo -= valor

                data_e_hora_atuais = datetime.now()
                data_e_hora_em_texto = data_e_hora_atuais.strftime("‘%d/%m/%Y %H:%M’")

                extrato += f'''
        ======================================================================
        Saque:  R$ {valor:.2f}    Data e Hora Realizado:   {data_e_hora_em_texto}
        ======================================================================

                '''

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
    saldoTotal = f'''
        @@@@@ Seu Saldo Atual é R$ {saldo:.2f} @@@@@
    '''
    return   saldoTotal , extrato

def criar_usuario( usuarios , cpf_enviado , validate_cpf):

    cpf_user = cpf_enviado
    validate_cpf = validate_cpf
    usuarios = usuarios

    flag_authorization = True

    if validate_cpf is True:

        #Verificar se o cpf ja foi registrado

        if (len(usuarios) > 0 ):
            for user in usuarios:
                if cpf_user == user['cpf']:
                    print('@@@ Este CPF ja está registrado! @@@')
                    flag_authorization = None
                else:
                    flag_authorization = True


        if flag_authorization is True:
            name_user = input('\n Digite seu Nome \n => ')
            validate_name =  name_user.isdigit()

            if validate_name is False:
                os.system('cls')
                print('===== Endereço =====')
                state = input ('\n Digite o seu Estado \n => ')
                cep = input('\n Digite o seu CEP \n => ')
                os.system('cls')
                print('===== Contato =====')
                number_phone = input('\n Digite o seu Número de telefone \n =>')
                validade_number_phone = number_phone.isdigit()

                if validade_number_phone is True:
                    registrando_user = {'cpf': cpf_user , 'name': name_user ,   'phone': number_phone , 'adders': {'state': state , 'cep':  cep }}

                    return registrando_user
                else:
                    print('@@@ Número de Telefone Inválido. ex: 81997665123     @@@')

            else:
                print( '@@@ Nome Inválido , Você deve inserir um Nome Real @@@')
    else:
        print('@@@ CPF Inválido @@@')


def listar_contas(usuarios):
    ...
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    data_e_hora_atuais = ''

    usuarios = []
    numero_contas = 0
    contas = []

    while True:
        opcao = menu()
        #Deposito
        if opcao == 'd':
            os.system('cls')
            valor = input("Informe o valor do depósito: ")
            validacao = None
            try:
                valor = float(valor)
                validacao = True
            except ValueError:
                print("\n@@@ Você Deve Informar Um Valor Válido!")
                validacao = None
            except:
                print("\n@@@ Erro Desconhecido!")
                validacao = None

            if validacao == True:

                saldo, extrato  = depositar(saldo, valor, extrato,data_e_hora_atuais)
        #Saque
        elif opcao == 's':
            os.system('cls')
            valor = input("Informe o valor do saque: ")
            validacao = None
            try:
                valor = float(valor)
                validacao = True

            except ValueError:
                print("\n@@@ Você Deve Informar Um Valor Válido!")
                validacao = None
            except:
                print("\n@@@ Erro Desconhecido!")
                validacao = None

            if validacao == True:
                saldo, extrato , numero_saques = sacar(saldo=saldo , valor=valor ,  extrato= extrato , limite= limite , numero_saques= numero_saques,    limite_saques= LIMITE_SAQUES , data_e_hora_atuais=     data_e_hora_atuais)
        #Extrato
        elif opcao == 'e':
            os.system('cls')
            if len(extrato) == 0:
                print('@@@ Extratos Indisponível. Sem movimentações Recentes Na Conta! @@@')
            else:
                extratos = exibir_extrato(saldo , extrato= extrato)
                extratos = list(extratos)
                for  i in extratos:
                    print(i)
        #Nova Conta
        elif opcao == 'c':
            new_accont_cpf = input(f'Digite o CPF do Usuário que Deseja Abrir uma nova Conta\n =>')
            for user in usuarios:
                if new_accont_cpf == user['cpf']:
                    os.system('cls')
                    menu_new_accont = '''
                    [1]\t Conta Poupança
                    [2]\t Conta Corrente
                    =>
                    '''
                    return input(textwrap.dedent(menu_new_accont))

                else:
                    print('nao encontrado!')

        #Listar Contas
        elif opcao == 'l':
            ...
        #Novo Usuário
        elif opcao=='u':
            os.system('cls')
            print('===== Dados Pessoais =====\n')
            cpf_user = input('Digite Seu Cpf \n => ')
            str(cpf_user)



            validate_cpf = validar_cpf(cpfEnviado=cpf_user)
            new_user = criar_usuario(usuarios= usuarios , cpf_enviado= cpf_user,       validate_cpf=validate_cpf)
            if new_user is not None:
                 usuarios.append(new_user)
                 os.system('cls')
                 print(f'Usuário Registrado com Sucesso!')
        #Sair
        elif opcao == 'q':
            break

        else:
            print('opcoes invalidas')


main()
