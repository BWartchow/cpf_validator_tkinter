""" Arquivo Main - backend"""
import time # para temporizar funções
from classes import *

# ESTE É O ARQUIVO SERVER-SIDE PARA SER EXECUTADO EM PARALELO COM interface.py #

while True:
    try:
        # Lê o arquivo onde GUI registra entrada do usuário:
        with open(ClasseRegistros.ENTR, 'r', encoding='utf-8') as arq:
            leitura = arq.readlines()
        # Zera a entrada do usuário:
        open(ClasseRegistros.ENTR, 'w').close()
        #print(f'Li isso: {leitura}')
        # SE tiver lido algo:
        if leitura:
            # Formata o que leu:
            entrada_do_usuario = leitura[0].rstrip()
            #print(f'Li isso aqui: {entrada_do_usuario}')
            # SE tem algo lido:
            if entrada_do_usuario:
                # Chama método que valida entrada e se ok instancia objeto:
                cpf = ClasseCpf.valida_entrada(entrada_do_usuario)
                print(cpf)
                if cpf:
                    # Verifica se os dígitos validadores são de um Cpf válido:
                    testa = ClasseCpf.verifica_digitos(cpf)
                    # Escreve retorno da validação para comunicar com a GUI:
                    with open(ClasseRegistros.RESP, 'w', encoding='utf-8') as arq:
                        arq.write(f'{testa}')
                    if 'in' in testa:
                        # Registra com append o CPF inválido no log de erro:
                        with open(
                            ClasseRegistros.REG_INV, 'a', encoding="utf-8") as arq:
                            arq.write(f'{testa} - {ClasseRegistros.data_e_hora()}\n')
                    else:
                        # Registra com append o CPF válido nos resultados:
                        ClasseRegistros.escrever_registro_valido(testa)
    except Exception as erro:
        # Aqui vem parar as raise exception da execução do módulo de classes:
        print(erro)
        with open(ClasseRegistros.RESP, 'w', encoding='utf-8') as arq:
            arq.write(f'{erro}')
    time.sleep(2)

###############################################################################

""" casos_de_teste = (
                    '00000000000',
                    '11111111111',
                    '22222222222',
                    '33333333333',
                    '44444444444',
                    '55555555555',
                    '66666666666',
                    '77777777777',
                    '88888888888',
                    '99999999999',
                    '123',
                    '',
                    '1234567891011112',
                    'abc',
                    'abcdefghijklmno',
                    '@.-',
                    '...-',
                    '11144477735',
                    '111.444.777-35',
                    '600.812.360-34',
                    '739.619.160-20',
                    '319.237.040-87',
                    '06321110035',
                    '95139332027',
                    '98753917006',
                    '22255511163',
                    '99988877756',
                    '66633344422')
 """
