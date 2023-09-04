import os
def linha(tam) -> str:
    return '=' * tam

def cabecalho(txt) -> None:
    print("")
    print(linha(50))
    print(txt.center(50))
    print(linha(50))

def menu(titulo, execucoes):
    cabecalho(titulo)
    c = 1
    for i in execucoes:
        print(f'{c} - {i}')
        c += 1
    print(linha(50))

def trat_erro_num(msg) -> float:
    n = 0
    while True:
        try:
            n = float(input(msg))
            break
        except ValueError:
            print("\033[031m--> ERRO: Por favor, digite um número.\033[m\n")
            continue
    return n

def exibir_invalido():
    print("\033[031m--> ERRO: Por favor, digite uma opção válida.\033[m\n")

def cadastro_geral(tipo_cad, dados: dict) -> dict:
    cabecalho(f'CADASTRO {tipo_cad}')
    for k in dados.keys():
        dados[k] = cadastro_individual(k)
    dados = confirmar_dados(tipo_cad, dados)
    return dados

def cadastro_individual(dado: str):
    if dado.find('Valor') == -1:
        valor = input(f"{dado}: ")
    else:
        while True:
            valor = trat_erro_num("Valor: ")
            if valor > 2000 or valor == 2000:
                break
            else:
                print("\033[031m--> ERRO: O valor mínimo de uma bike para que seja assegurada é de R$2000.00!!\033[m\n")
    return valor

def exibir_dados(dados: dict):
    for k, v in dados.items():
        print(f"{k}: {v}")

def confirmar_dados(tipo_cad, dados: dict):
    alterar = "N"
    while alterar.upper() == 'N':
        os.system('cls')
        cont = 0
        valores = []
        cabecalho(f'CADASTRO {tipo_cad}')
        for k, v in dados.items():
            print(f"{k}: {v}")
            valores.append(f"{k}: {v}")
        print(linha(50))
        while True:
            alterar = input("Confirme seus dados ['S' para continuar || 'N' para alterar]: ")
            if alterar.upper() == 'S' or alterar.upper() == 'N':
                break
            else:
                exibir_invalido()
        if alterar.upper() == "N":
            menu("ALTERAR DADOS", valores)
            while True:
                opc_alterar = trat_erro_num("Qual dado você deseja alterar?: ")
                if opc_alterar in [1, 2, 3, 4]:
                    break
                else:
                    exibir_invalido()
            for k in dados.keys():
                cont += 1
                if opc_alterar == cont:
                    dados[k] = cadastro_individual(k)
        if alterar.upper() == "S":
            os.system("cls")
    return dados
                