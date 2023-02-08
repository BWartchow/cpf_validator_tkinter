""" Módulo Tkinter para criar Interface Gráfica do usuário - GUI """

import tkinter as tk
from tkinter import messagebox # para interação do backend com o usuário
import time # para temporizar funções
from classes import *

# ESTE É O ARQUIVO CLIENT-SIDE PARA SER EXECUTADO EM PARALELO COM O main.py #

###############################################################################

# FUNÇÕES RELACIONADAS À GUI:


def recebe_retorno():
    """ Recebe o retorno da validação da entrada pelo servidor"""
    # Lê o retorno do servidor:
    with open(ClasseRegistros.RESP, 'r', encoding='utf-8') as arq:
        leitura = arq.readlines()
    # Zera o retorno:
    open(ClasseRegistros.RESP, 'w').close()
    # SE tiver lido algo:
    if leitura:
        # Formata o que leu:
        resposta_servidor = leitura[0].rstrip()
        # SE tem algo lido:
        if resposta_servidor:
            if 'in' in resposta_servidor:
                # messagebox de erro:
                messagebox.showerror('Erro!', f'{resposta_servidor}')
            else:
                # messagebox de cpf válido:
                messagebox.showinfo('Validação:', resposta_servidor)


def enviar_cpf():
    """ Função que envia CPF digitado para o servidor"""
    # Captura o campo entry e escreve o que há nele no arquivo entrada:
    with open(ClasseRegistros.ENTR, 'w', encoding='utf-8') as arq:
        arq.write(entrada.get())
    time.sleep(4)
    # Lê arquivo de retorno do campo entry pelo servidor:
    recebe_retorno()


def sair():
    """ Dá ao usuário a opção de sair da GUI"""
    # messagebox para confirmar encerramento da aplicação:
    alerta = messagebox.askquestion('Fechar Validador', 'Deseja mesmo sair?',
                                    icon='question')
    if alerta == 'yes':
        # encerra aplicação:
        janela.destroy()
    else:
        # retorna para aplicação:
        messagebox.showinfo('Bem-vindo de volta',
                            'Bem-vindo de volta ao Validador')


###############################################################################

# Cria janela de interface para usuário, objeto da classe Tkinter:
janela = tk.Tk()
# Configura título da janela:
janela.title('Validador de CPF')
# Fixa o tamanho da janela:
janela.geometry('600x334')
janela.resizable(width=False, height=False)
#Configura ícone da janela:
janela.iconbitmap('senac.ico')
# Configura plano de fundo:
image = tk.PhotoImage(file='./fundo.png')
image = image.subsample(1, 1)
labelimage = tk.Label(image=image)
labelimage.place(x=0, relwidth=1.0, relheight=1.0)

###############################################################################

# Cria label de título:
TITLE = 'Bem-vindo ao Validador de CPF do Senac-tech'
label_titulo = tk.Label(janela, text=TITLE,
                        font=('Arial', 16, 'bold'), bg='#1EB7D9')
label_titulo.pack(fill='x')

# Cria label de instruções:
TXT = 'Insira o CPF no campo abaixo e clique em ENVIAR para validá-lo:'
label_instrucao = tk.Label(janela, text=TXT,
                           font=('Arial', 12), bg='white')
label_instrucao.pack(pady=(0, 5))

# Cria label de observações:
OBS = 'Formatos aceitos: XXX.XXX.XXX-XX ou XXXXXXXXXXX'
label_obs = tk.Label(janela, text=OBS,
                     font=('Arial', 10, 'italic'), bg='white')
label_obs.pack()

###############################################################################

# Cria campo para digitar o CPF:
entrada = tk.Entry(janela, font=('Arial', 20), border=5)
entrada.pack(pady=5)

# Cria botão para enviar o que há no campo entrada para validação:
botao_enviar = tk.Button(janela, text='Enviar', font=('Arial', 16), bg='blue',
                         fg='white', activebackground='green',
                         activeforeground='white', command=enviar_cpf)
botao_enviar.pack(pady=15)

# Cria botão para dar ao usuário a opção de sair do programa:
botao_fechar = tk.Button(janela, text='Fechar', font=('Arial', 14), bg='red',
                         fg='white', activebackground='purple',
                         activeforeground='white', command=sair)
botao_fechar.pack(side='bottom', pady=10)

###############################################################################

# Executa a GUI:
janela.mainloop()
