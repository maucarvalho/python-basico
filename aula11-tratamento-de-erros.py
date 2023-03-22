try:
    a = 1200 / 0
except Exception as erro:
    print('Não é possível fazer a operação: ', erro)

###############################

import time

def abre_arquivo():
    try:
        arquivo = open('arquivo-mau.txt')
        return True
    except Exception as error:
        print('Aconteceu algum erro.', error)
        return False

while not abre_arquivo():
    print('Tentando abrir o Arquivo')
    time.sleep(5)

print('Finalmente consegui abrir o Arquivo!')