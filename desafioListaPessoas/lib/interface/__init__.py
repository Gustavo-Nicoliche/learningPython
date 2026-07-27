def linha(tam=42):
    return '-' * tam


def header(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg): 
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mVocê só pode digitar um número que corresponda a uma das opções.\033[m')
        else:
            return n

def menu(lista):
    header('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Digite sua opção: ') 
    return opc