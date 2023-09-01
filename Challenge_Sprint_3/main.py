from lib.subalgoritmos import *
from time import sleep
execs = ['Cadastrar dados pessoais', 'Cadastrar dados da bike', 'Ver/Selecionar plano', 'Perguntas frequentes',
         'Fechar o programa']
opc_menu = 1

print(f"""
{linha(61)}
|| Bem-vindo ao programa responsável pela contratação do   ||
|| seguro de bikes via Porto Seguro.                       ||
|| Desenvolvido por: CycleX                                ||
{linha(61)}
""")
while opc_menu != 0:
    menu('MENU PRINCIPAL', execs)
    opc_menu = trat_erro("Escolha uma opção: ")
    match opc_menu:
        case 0:
            cabecalho("Finalizando programa.")
        case _:
            exibir_invalido()
    sleep(1.5)
