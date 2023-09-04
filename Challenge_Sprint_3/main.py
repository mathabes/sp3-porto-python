from lib.subalgoritmos import *
import os
from time import sleep

execs = ['Cadastrar dados pessoais', 'Cadastrar dados da bike', 'Ver/Selecionar plano', 'Perguntas frequentes',
         'Fechar o programa']
cadastro = {'Dados Pessoais': {'Nome': "", 'Email': "", 'Telefone': "", 'CPF': ""},
            'Dados Bike': {'Marca': "", 'Modelo': "", 'Chassi': "", 'Valor': 0.0},
            'Acessórios Bike': {'Tipo do acessório': "", 'Marca do acessório': "",
                                'Modelo do acessório': "", 'Valor do acessório': 0.0}}
opc_menu = 1
os.system('cls')
print(f"""
{linha(61)}
|| Bem-vindo ao programa responsável pela contratação do   ||
|| seguro de bikes via Porto Seguro.                       ||
|| Desenvolvido por: CycleX                                ||
{linha(61)}
""")
sleep(3)
while opc_menu != 5:
    menu('MENU PRINCIPAL', execs)
    opc_menu = trat_erro_num("Escolha uma opção: ")
    match opc_menu:
        case 1:
            cadastro['Dados Pessoais'] = cadastro_geral('DADOS PESSOAIS', cadastro['Dados Pessoais'])
            cabecalho("Cadastro de dados pessoais finalizado!!!")
        case 2:
            cadastro['Dados Bike'] = cadastro_geral('DADOS BIKE', cadastro['Dados Bike'])
            cabecalho("Cadastro de dados da bike finalizado!!!")
        case 5:
            cabecalho("Finalizando programa...")
            cabecalho("Desenvolvido por: CycleX")
        case _:
            exibir_invalido()
            sleep(2.5)
            os.system('cls')
