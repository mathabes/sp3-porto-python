from lib.subalgoritmos import *
import os
from time import sleep

funcionalidades = ['Ver/Cadastrar dados pessoais', 'Ver/Cadastrar dados da bike', 'Ver/Selecionar plano', 'Fechar o programa']
dados = {'Dados Pessoais': {'Nome': "", 'Email': "", 'Telefone': "", 'CPF': ""},
        'Dados Bike': {'Marca': "", 'Modelo': "", 'Chassi': "", 'Valor': 0.0}}
acessorio = {'Tipo do acessório': "", 'Marca do acessório': "",
            'Modelo do acessório': "", 'Preço do acessório': 0.0}
quant_acessorio = 0
opc_plano = 0
plano_selecionado = ""
alterar_plano = ""
d_pessoais_cadastrados = False
d_bike_cadastrados = False
dados_restantes = []
finalizar_programa = ""

os.system('cls')
print(f"""
{linha(61)}
|| Bem-vindo ao programa responsável pela contratação do   ||
|| seguro de bikes via Porto Seguro.                       ||
|| Desenvolvido por: CycleX                                ||
{linha(61)}
""")
sleep(3)
while True:
    menu('MENU PRINCIPAL', funcionalidades)
    opc_menu = int(tratar_erro_num("Escolha uma opção: "))
    match opc_menu:
        case 1:
            if not d_pessoais_cadastrados:
                dados['Dados Pessoais'] = cadastro_geral('DADOS PESSOAIS', dados['Dados Pessoais'])
                dados['Dados Pessoais'] = confirmar_dados('DADOS PESSOAIS', dados['Dados Pessoais'])
                d_pessoais_cadastrados = True
                cabecalho("Cadastro de dados pessoais finalizado!!!")
            else:
                dados['Dados Pessoais'] = confirmar_dados('DADOS PESSOAIS', dados['Dados Pessoais'])
        case 2:
            if not d_bike_cadastrados:
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
                d_bike_cadastrados = True    
                cabecalho("Cadastro de dados da bike finalizado!!!")
            else:
                dados['Dados Bike'] = confirmar_dados('DADOS BIKE', dados['Dados Bike'])
                if quant_acessorio != 0:
                    for i in range(quant_acessorio):
                        dados[f'Acessório {i + 1}'] = confirmar_dados(f'ACESSÓRIO {i + 1}', dados[f'Acessório {i + 1}'])
        case 3:
            while True:
                if opc_plano != 4:
                    os.system('cls')
                if plano_selecionado == "":
                    cabecalho("SELECIONE SEU PLANO")
                    print(f"""1 --> Pedal essencial: O plano para você 
experimentar um dos serviços essenciais 
oferecidos, de acordo com as suas necessidades.
--------------------------------------------------
2 --> Pedal leve: Você gosta de pedalar e está 
buscando um plano de serviços intermediário? 
O Pedal leve da Porto é para você. 
--------------------------------------------------
3 --> Pedal elite: Conte com diversos serviços
capazes de elevar suas aventuras para o próximo
nível.
--------------------------------------------------
4 --> Saiba mais sobre nossos planos.
--------------------------------------------------
5 --> Voltar.
{linha(50)}""")
                    opc_plano = int(tratar_erro_num("Escolha uma opção: "))
                    match opc_plano:
                        case 1:
                            plano_selecionado = 'Pedal essencial'
                            break
                        case 2:
                            plano_selecionado = 'Pedal leve'
                            break
                        case 3:
                            plano_selecionado = 'Pedal elite'
                            break
                        case 4:
                            os.system('cls')
                            cabecalho("INFORMAÇÕES SOBRE PLANOS")
                            exibir_descricao_plano('Pedal essencial')
                            print('--------------------------------------------------')
                            exibir_descricao_plano('Pedal leve')
                            print('--------------------------------------------------')
                            exibir_descricao_plano('Pedal elite')
                            print(linha(50))
                            input("Pressione ENTER para voltar")
                        case 5:
                            cabecalho('VOLTANDO...')
                            sleep(1.5)
                            break
                        case _:
                            exibir_invalido()
                else:
                    cabecalho(f"{plano_selecionado} selecionado.")
                    exibir_descricao_plano(plano_selecionado)
                    print(linha(50))
                    while True:
                        alterar_plano = input("Deseja alterar seu plano? [S/N]: ")
                        if alterar_plano.upper() == 'S' or alterar_plano.upper() == 'N':
                            break
                        else:
                            exibir_invalido()
                    if alterar_plano.upper() == 'S':
                        plano_selecionado = ""
                    else:
                        break
            os.system('cls')
            if plano_selecionado != "":
                        cabecalho(f"{plano_selecionado} selecionado!!!")
        case 4:
            os.system('cls')
            if d_pessoais_cadastrados:
                exibir_dados('DADOS PESSOAIS', dados['Dados Pessoais'])
                sleep(0.7)
            else:
                dados_restantes.append('Cadastrar dados pessoais')
            if d_bike_cadastrados:
                exibir_dados('DADOS BIKE', dados['Dados Bike'])
                sleep(0.7)
                if possui_acessorio.upper() == 'S':
                    for i in range(quant_acessorio):
                        exibir_dados(f'ACESSÓRIO {i + 1}', dados[f'Acessório {i + 1}'])
                        sleep(0.7)
            else:
                dados_restantes.append('Cadastrar dados da bike')
            if plano_selecionado != "":
                cabecalho(f"{plano_selecionado} selecionado.")
                exibir_descricao_plano(plano_selecionado)
                print(linha(50))
                sleep(0.7)
            else:
                dados_restantes.append('Selecionar plano')
            if d_pessoais_cadastrados and d_bike_cadastrados and plano_selecionado != "":
                cabecalho("Contratação do seguro concluída!!!")
                break
            else:
                menu("Contratação incompleta. Ações em aberto:", dados_restantes)
                while True:
                    finalizar_programa = input("Deseja mesmo fechar o programa? [S/N]: ")
                    if finalizar_programa.upper() == 'S' or finalizar_programa.upper() == 'N':
                        break
                    else:
                        exibir_invalido()
                if finalizar_programa.upper() == 'S':
                    break
                else:
                    os.system('cls')
        case _:
            exibir_invalido()
cabecalho("Finalizando programa...")
cabecalho("Desenvolvido por: CycleX")
