import datetime

# ARQUIVO COM AS CLASSES CPF E REGISTRO DE ENTRADAS #

class ClasseCpf:
    """ Classe referente ao Cadastro de Pessoa Física - CPF """

    def __init__(self, cpf) -> None:
        """ Método construtor do objeto de tipo Classe CPF"""

        self.cpf = cpf

    """ Um método estático não precisa de uma instância da classe para ser
    chamado, por isso ele foi escolhido para validar a entrada de dados,
    sendo que o objeto só será instanciado uma vez que a entrada seja válida!"""

    @staticmethod
    def valida_entrada(entrada_do_usuario: str):
        """ Static Method de instanciação do objeto de tipo Cpf
            após a validação da entrada do usuário"""

        return ClasseCpf.instancia_cpf(entrada_do_usuario)

    @classmethod
    def instancia_cpf(cls, entrada_do_usuario: str):
        """ Class Method de de validação da entrada do usuário"""

        entrada_recebida = entrada_do_usuario.replace('.','').replace('-','')
        # trata a string para pontos e traços e retorna uma cópia sem estes

        if not entrada_recebida.isnumeric():
        # verifica se a string tratada é inválida (não é do tipo numérica)
            msg = 'Entrada inválida! Digite apenas números nos formatos aceitos.'
            ClasseRegistros.escrever_registro_invalido(entrada_recebida, msg)
            # Usa Classe Registros para escrever log de erro
            #print(msg)
            raise CpfException(msg)

        if len(entrada_recebida) != 11:
        # verifica se a string tratada é inválida (possui tamanho diferente de 11)
            msg = 'Entrada inválida! Necessário 11 números nos formatos aceitos.'
            ClasseRegistros.escrever_registro_invalido(entrada_recebida, msg)
            # Usa Classe Registros para escrever log de erro
            #print(msg)
            raise CpfException(msg)

        # FALTA TRATAR DÍGITOS IGUAIS
        return cls(entrada_do_usuario)

    def __str__(self) -> str:
        """ Método mágico modificado com string de retorno do objeto de tipo Cpf"""

        mascara = f'CPF {self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'
        return f"{mascara}"

###############################################################################

class ClasseRegistros(ClasseCpf):
    """ Classe herdada da ClasseCpf para registro de entradas válidas e onválidas"""

    def __init__(self, cpf) -> None:
        """ Método construtor de classe """
        super().__init__(cpf)
        self.registro_invalido = './entrada_invalida.log'
        self.registros_validos = './cpfs_validos.txt'

    @staticmethod
    def escrever_registro_invalido(entrada: str, msg:str):
        """ Método para escrever registros inválidos no log de erros """

        # usa o append (a) para não apagar nenhum registro anterior
        arq = open('./entrada_invalida.log', 'a', encoding="utf-8")
        test = datetime.datetime.now()
        s1 = test.strftime("%d/%m/%Y - %H:%M:%S.%f")[:-2]
        arq.write(f'{entrada}: {msg} - {s1}\n')
        # Para colocar data e hora nos arquivos em formato dd/mm/aaaa - hh:mm:ss.mmmm

###############################################################################

class CpfException(Exception):
    pass





#metodo estático para data
