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
    opc_menu = trat_erro("Escolha uma opção: ")
    match opc_menu:
        case 5:
            cabecalho("Finalizando programa.")
        case _:
            exibir_invalido()
            sleep(2)
            os.system('cls')
