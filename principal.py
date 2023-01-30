import time
from classes import *

while True:
    try:
        arq = open('./entrada_usuario.txt', 'r', encoding='utf-8')
        leitura = arq.readlines()
        entrada_do_usuario = leitura[0].rstrip()
        #print(entrada_do_usuario)
        if entrada_do_usuario:
            cpf = ClasseCpf.valida_entrada(entrada_do_usuario)
            print(cpf)
        arq.close()
    except Exception as erro:
        print(erro)
    time.sleep(1)
