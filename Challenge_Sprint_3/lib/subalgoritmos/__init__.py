import os
def linha(tam) -> str:
    return '=' * tam

def cabecalho(txt) -> None:
    print("")
    print(linha(50))
    print(txt.center(50))
    print(linha(50))

def menu(titulo, execucoes) -> None:
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

def exibir_invalido() -> None:
    print("\033[031m--> ERRO: Por favor, digite uma opção válida.\033[m\n")

def cadastro_geral(tipo_cadastro, d: dict) -> dict:
    cabecalho(f'CADASTRO {tipo_cadastro}')
    for k in d.keys():
        d[k] = cadastro_individual(k)
    return d

def cadastro_individual(dado: str) -> str or float:
    if dado.find('Valor') != -1:
        while True:
            valor = tratar_erro_num("Valor: R$ ")
            if valor > 2000 or valor == 2000:
                break
            else:
                print("\033[031m--> ERRO: O valor mínimo de uma bike para que seja assegurada é de R$2000.00!!\033[m\n")
    elif dado.find('Preço') != -1:
        valor = tratar_erro_num(f"{dado}: R$ ")
    else:
        valor = input(f"{dado}: ")
    return valor

def confirmar_dados(tipo_cadastro, d: dict) -> dict:
    alterar = "N"
    while alterar.upper() == 'N':
        os.system('cls')
        cont = 0
        valores = []
        cabecalho(f'CADASTRO {tipo_cadastro}')
        for k, v in d.items():
            if k.find('Valor') != -1 or k.find('Preço') != -1:
                print(f"{k}: R$ {v:.2f}")
                valores.append(f"{k}: R$ {v:.2f}")
            else:
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

def exibir_dados(tipo_cadastro, d: dict) -> None:
    cabecalho(tipo_cadastro)
    for k, v in d.items():
        if k.find('Valor') != -1 or k.find('Preço') != -1:
            print(f"{k}: R$ {v:.2f}")
        else:
            print(f"{k}: {v}")
    print(linha(50))

def exibir_descricao_plano(plano) -> None:
    if plano == 'Pedal essencial':
        print("""\033[1m--> Pedal Essencial:\033[0m plano gratuito que oferece 
reparo e/ou troca de câmaras de ar, correntes, 
coroas, manetes de freios, além de 
lubrificação de correntes.""")
    elif plano == "Pedal leve":
        print("""\033[1m--> Pedal leve:\033[0m mesmas garantias do plano Pedal 
Essencial(reparo e/ou troca de câmaras de ar, 
correntes, coroas, manetes de freios, além de 
lubrificação de correntes), com um benefício 
a mais: transporte do segurado e sua bike em 
caso de quebra ou acidente, com limite de 
\033[1m50 km\033[0m.""")
    else:
        print("""\033[1m--> Pedal elite:\033[0m mesmas garantias do plano Pedal 
Essencial(reparo e/ou troca de câmaras de ar, 
correntes, coroas, manetes de freios, além de 
lubrificação de correntes), com um benefício 
a mais: transporte do segurado e sua bike em 
caso de quebra ou acidente, com limite de 
\033[1m150 km\033[0m.""")