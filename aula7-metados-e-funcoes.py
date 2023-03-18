def soma(n1, n2):
    result = n1 + n2
    return result

def imprime_oi():
    print('Oi')

def tem_sete_itens(arg):
    if len(arg) <= 7:
        return True
    else:
        return False

print(soma(6,2))

imprime_oi()

print(tem_sete_itens('1234567'))
