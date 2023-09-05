from lib.subalgoritmos import *
import os
from time import sleep

funcionalidades = ['Cadastrar dados pessoais', 'Cadastrar dados da bike', 'Ver/Selecionar plano', 'Perguntas frequentes',
         'Fechar o programa']
dados = {'Dados Pessoais': {'Nome': "", 'Email': "", 'Telefone': "", 'CPF': ""},
        'Dados Bike': {'Marca': "", 'Modelo': "", 'Chassi': "", 'Valor': 0.0}}
acessorio = {'Tipo do acessório': "", 'Marca do acessório': "",
            'Modelo do acessório': "", 'Preço do acessório': 0.0}
opc_menu = 1
plano = ""

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
    menu('MENU PRINCIPAL', funcionalidades)
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
        case 3:
            opc_plano = 1
            os.system('cls')
            while opc_plano != 0 and plano == "":
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
                        plano = 'Pedal essencial'
                    case 2:
                        plano = 'Pedal leve'
                    case 3:
                        plano = 'Pedal elite'
                    case 4:
                        os.system('cls')
                        cabecalho("INFORMAÇÕES SOBRE PLANOS")
                        print(f"""\033[1m--> Pedal Essencial:\033[0m plano gratuito que oferece 
reparo e/ou troca de câmaras de ar, correntes, 
coroas, manetes de freios, além de 
lubrificação de correntes.
--------------------------------------------------
\033[1m--> Pedal leve:\033[0m mesmas garantias do plano Pedal 
Essencial, com um benefício a mais: transporte do 
segurado e sua bike em caso de quebra ou acidente, 
com limite de \033[1m50 km\033[0m. 
--------------------------------------------------
\033[1m--> Pedal elite:\033[0m Tem tudo o que o plano Pedal 
Essencial oferece, com um benefício a mais: 
transporte do segurado e sua bike em caso de 
quebra ou acidente, com limite de \033[1m150 km\033[0m.
{linha(50)}""")
                        enter = input("Pressione ENTER para voltar")
                    case 5:
                        cabecalho('VOLTANDO...')
                        sleep(1.5)
                    case _:
                        exibir_invalido()
                if opc_plano != 4:
                    os.system('cls')
                if plano != "":
                    cabecalho(f"{plano} selecionado!!!")
        case 4:
            print("")
        case 5:
            cabecalho("Finalizando programa...")
            cabecalho("Desenvolvido por: CycleX")
        case _:
            exibir_invalido()
