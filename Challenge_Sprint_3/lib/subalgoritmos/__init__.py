def linha(tam) -> str:
    return '=' * tam


def cabecalho(txt) -> None:
    print(linha(61))
    print(txt.center(61))
    print(linha(61))


def menu(titulo, execucoes):
    cabecalho(titulo)
    c = 1
    for i in execucoes:
        print(f'{c} - {i}')
        c += 1
    print(linha(61))


def trat_erro(msg):
    n = 0
    while True:
        try:
            n = int(input(msg))
            break
        except ValueError:
            print("\033[031m--> ERRO: Por favor, digite um número.\033[m\n")
            continue
    return n


def exibir_invalido():
    print(f"\033[031m--> ERRO: Por favor, digite uma opção válida.\033[m\n")

def cadastros(dados: dict):
    cabecalho()

