def linha(tam=61) -> str:
    return '=' * tam


def cabecalho(txt) -> None:
    print(linha())
    print(txt.center(61))
    print(linha())


def menu(titulo, execucoes):
    cabecalho(titulo)
    c = 1
    for i in execucoes:
        print(f'{c} - {i}')
        c += 1
    print(linha())


def trat_erro(msg):
    n = 0
    while True:
        try:
            n = int(input(msg))
            break
        except ValueError:
            print("\033[031m--> ERRO: Por favor, digite um número.\033[m")
            continue
    return n
