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

def tratar_erro_num(msg) -> float:
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

def cadastro_geral(tipo_cadastro, d: dict) -> dict:
    cabecalho(f'CADASTRO {tipo_cadastro}')
    for k in d.keys():
        d[k] = cadastro_individual(k)
    return d

def cadastro_individual(dado: str):
    if dado.find('Valor') != -1:
        while True:
            valor = tratar_erro_num("Valor: ")
            if valor > 2000 or valor == 2000:
                break
            else:
                print("\033[031m--> ERRO: O valor mínimo de uma bike para que seja assegurada é de R$2000.00!!\033[m\n")
    elif dado.find('Preço') != -1:
        valor = tratar_erro_num("Valor: ")
    else:
        valor = input(f"{dado}: ")
    return valor

def exibir_dados(d: dict):
    for k, v in d.items():
        print(f"{k}: {v}")

def confirmar_dados(tipo_cadastro, d: dict):
    alterar = "N"
    while alterar.upper() == 'N':
        os.system('cls')
        cont = 0
        valores = []
        cabecalho(f'CADASTRO {tipo_cadastro}')
        for k, v in d.items():
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
                opc_alterar = int(tratar_erro_num("Digite a opção que deseja alterar: "))
                if opc_alterar in [1, 2, 3, 4]:
                    break
                else:
                    exibir_invalido()
            for k in d.keys():
                cont += 1
                if opc_alterar == cont:
                    d[k] = cadastro_individual(k)
        if alterar.upper() == "S":
            os.system("cls")
    return d
                