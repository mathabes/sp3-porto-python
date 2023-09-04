from lib.subalgoritmos import *
import os
from time import sleep

execs = ['Cadastrar dados pessoais', 'Cadastrar dados da bike', 'Ver/Selecionar plano', 'Perguntas frequentes',
         'Fechar o programa']
dados = {'Dados Pessoais': {'Nome': "", 'Email': "", 'Telefone': "", 'CPF': ""},
        'Dados Bike': {'Marca': "", 'Modelo': "", 'Chassi': "", 'Valor': 0.0}}
acessorio = {'Tipo do acessório': "", 'Marca do acessório': "",
            'Modelo do acessório': "", 'Preço do acessório': 0.0}
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
    opc_menu = int(tratar_erro_num("Escolha uma opção: "))
    match opc_menu:
        case 1:
            dados['Dados Pessoais'] = cadastro_geral('DADOS PESSOAIS', dados['Dados Pessoais'])
            dados['Dados Pessoais'] = confirmar_dados('DADOS PESSOAIS', dados['Dados Pessoais'])
            cabecalho("Cadastro de dados pessoais finalizado!!!")
        case 2:
            dados['Dados Bike'] = cadastro_geral('DADOS BIKE', dados['Dados Bike'])
            dados['Dados Bike'] = confirmar_dados('DADOS BIKE', dados['Dados Bike'])
            while True:
                possui_acessorio = input("Sua bike possui algum acessório? [S/N]: ")
                if possui_acessorio.upper() == 'S' or possui_acessorio.upper() == 'N':
                    break
                else:
                    exibir_invalido()
            if possui_acessorio.upper() == 'S':
                quant_acessorio = int(tratar_erro_num("Quantos?: "))
                for i in range(quant_acessorio):
                    dados[f'Acessório {i + 1}'] = acessorio
                    dados[f'Acessório {i + 1}'] = cadastro_geral(f'ACESSÓRIO {i + 1}', dados[f'Acessório {i + 1}'])
                    dados[f'Acessório {i + 1}'] = confirmar_dados(f'ACESSÓRIO {i + 1}', dados[f'Acessório {i + 1}'])
            if possui_acessorio.upper() == 'N':
                os.system("cls")
            cabecalho("Cadastro de dados da bike finalizado!!!")
        case 5:
            cabecalho("Finalizando programa...")
            cabecalho("Desenvolvido por: CycleX")
        case _:
            exibir_invalido()
