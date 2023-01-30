import tkinter as tk

def enviar_cpf():
    arq = open('./entrada_usuario.txt', 'w', encoding="utf-8")
    arq.write(entrada.get())
    arq.close()

# Cria janela de interface para usuário, objeto da classe Tkinter
janela = tk.Tk()

# Configura título da janela
janela.title("Validador de CPF")

# Fixa o tamanho da janela
janela.geometry('600x334')
janela.resizable(width=False, height=False)

image = tk.PhotoImage(file="./fundo.png")
image = image.subsample(1, 1)
labelimage = tk.Label(image=image)
labelimage.place(x=0, relwidth=1.0, relheight=1.0)

label = tk.Label(janela,text="Bem-vindo ao Validador de CPF do Senac",font=("Arial",20,'bold'),bg='#1EB7D9')
label.pack(pady=(0,5), fill="x")

label = tk.Label(janela,text="Insira o CPF no campo abaixo e clique no botão ENVIAR:",font=("Arial",15),bg='white')
label.pack(pady=(0,5))

label = tk.Label(janela,text="Formatos válidos: 000.000.000-00 ou 00000000000",font=("Arial",10, 'italic'),bg='white')
label.pack()

entrada = tk.Entry(janela, font=("Arial", 20), border=5)
entrada.pack(pady=5)

botao_enviar = tk.Button(janela, text="Enviar", font=("Arial", 20), bg='blue', fg='white', activebackground="green", activeforeground="white", command=enviar_cpf)
botao_enviar.pack(pady=15)

botao_fechar = tk.Button(janela, text="Fechar", font=("Arial", 18), bg='red', fg='white', activebackground="purple", activeforeground="white", command=janela.destroy)
botao_fechar.pack(side="bottom", pady=10)

janela.mainloop()
