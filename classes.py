""" Módulo com as Classes CPF e Registro de Arquivos """

import datetime # para adicionar data e hora nos arquivos

# ESTE ARQUIVO É UM MÓDULO, NÃO É EXECUTADO DIRETAMENTE NO TERMINAL #

###############################################################################


class ClasseCpf:
    """ Classe referente ao Cadastro de Pessoa Física - CPF """

    def __init__(self, cpf: str) -> None:
        """ Método construtor do objeto de tipo Classe CPF"""
        self.cpf = cpf

    # Um método estático não precisa de uma instância da classe para ser
    # chamado, por isso ele foi escolhido para validar a entrada de dados,
    # sendo que o objeto só será instanciado uma vez que a entrada seja válida!

    @staticmethod
    def valida_entrada(entrada_do_usuario: str):
        """ Static Method de instanciação do objeto de tipo Cpf
            após a validação da entrada do usuário"""
        entrada_recebida = entrada_do_usuario.replace('.', '').replace('-', '')
        # trata a string para pontos e traços e retorna uma cópia sem estes
        if not entrada_recebida.isnumeric():
            # verifica se a string tratada é inválida (não é do tipo numérica)
            msg= 'Entrada inválida! Digite apenas números nos formatos aceitos.'
            ClasseRegistros.escrever_registro_invalido(entrada_recebida, msg)
            # Usa Classe Registros para escrever log de erro
            # print(msg)
            raise Exception(msg)
        if len(entrada_recebida) != 11:
            # verifica se a string tratada é inválida
            # (possui tamanho diferente de 11)
            msg= 'Entrada inválida! Necessário 11 números nos formatos aceitos.'
            ClasseRegistros.escrever_registro_invalido(entrada_recebida, msg)
            # Usa Classe Registros para escrever log de erro
            # print(msg)
            raise Exception(msg)
        if len(set(entrada_recebida)) == 1:
            # if digitos iguais -> set retira os dígitos repetidos:
            msg= 'Entrada inválida! Números todos iguais não são um CPF válido.'
            ClasseRegistros.escrever_registro_invalido(entrada_recebida, msg)
            # Usa Classe Registros para escrever log de erro
            # print(msg)
            raise Exception(msg)
        return ClasseCpf.instancia_cpf(entrada_recebida)

    @classmethod
    def instancia_cpf(cls, entrada_do_usuario: str):
        """ Class Method que instancia o objeto de tipo cpf"""
        # É chamada pelo staticmethod acima, se entrada do usuário for válida.
        return cls(entrada_do_usuario)

    def __str__(self) -> str:
        """ Magic method modificado com str de retorno do objeto de tipo Cpf"""
        S = f'CPF {self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'
        return f"{S}"
        # Quando imprime o objeto, mostra formatado com pontos e traço

    def __del__(self) -> None:
        """Magic method modificado com retorno para deleçao do objeto"""
        print('Objeto tipo Cpf deletado.')

    def verifica_digitos(self):
        """ Método que calcula os dígitos verificadores e valida enfim o CPF"""
        cpf_teste = []
        for caractere in self.cpf:
            if caractere == "." or caractere == "-":
                continue
            cpf_teste.append(caractere)
        # Verificação do primeiro dígito:
        multiplicador1 = 10
        soma1 = 0
        for item in range(0, 9):
            soma1 += (multiplicador1 * int(cpf_teste[item]))
            multiplicador1 -= 1
        #print(f'Soma = {soma1}')
        resto1 = soma1 % 11
        #print(f'Resto = {resto1}')
        if resto1 < 2: # o dígito é igual a 0 (Zero)
            digito01 = 0
            print(f'Primeiro dígito verificador = {digito01}')
        elif resto1 >= 2: # o dígito v. é igual a 11 menos o resto da divisão"
            digito01 = (11 - resto1)
            print(f'Primeiro dígito verificador = {digito01}')
        # Verificação do segundo dígito:
        multiplicador2 = 11
        soma2 = 0
        for item in range(0, 10):
            soma2 += (multiplicador2 * int(cpf_teste[item]))
            multiplicador2 -= 1
        #print(f'Soma = {soma2}')
        resto2 = soma2 % 11
        #print(f'Resto = {resto2}')
        if resto2 < 2: # o dígito é igual a 0 (Zero)
            digito02 = 0
            print(f'Segundo dígito verificador = {digito02}')
        elif resto2 >= 2: # o dígito v. é igual a 11 menos o resto da divisão"
            digito02 = (11 - resto2)
            print(f'Segundo dígito verificador = {digito02}')
        # Teste dos dígitos verificadores:
        if int(cpf_teste[-2]) == digito01 and int(cpf_teste[-1]) == digito02:
            print("CPF válido!")
            M = f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'
            return f'CPF {M} - CPF válido!'
        else:
            print("Este não é um CPF válido...")
            M = f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'
            return f'CPF {M} - CPF inválido!'

###############################################################################


class ClasseRegistros():
    """ Classe para registro de entradas válidas e inválidas"""

    # Criação de constantes para facilitar manutenção do código:
    REG_INV = './erros.log'
    REG_VAL = './resultado.txt'
    ENTR = './entrada.txt'
    RESP = './resposta.txt'

    def __init__(self) -> None:
        """ Método construtor de classe """
        # Arquivo de log com todos os CPFs inválidos e suas mensagens de erro:
        self.registro_invalido = open(
                            ClasseRegistros.REG_INV, encoding='utf-8').close()
        # Arquivo com todos os CPFs válidos testados:
        self.registros_validos = open(
                            ClasseRegistros.REG_VAL, encoding="utf-8").close()
        # Arquivo que recebe entrada do usuário:
        self.recebe_entrada = open(
                                ClasseRegistros.ENTR, encoding='utf-8').close()
        # Arquivo que devolve validação da entrada do usuário:
        self.retorno = open(ClasseRegistros.RESP, encoding='utf-8').close()

    @staticmethod
    def escrever_registro_invalido(entrada: str, msg: str):
        """ Método para escrever registros inválidos no log de erros """
        # usa o append (a) para não apagar nenhum registro anterior
        with open(ClasseRegistros.REG_INV, 'a', encoding="utf-8") as arq:
            arq.write(f'{entrada}: {msg} - {ClasseRegistros.data_e_hora()}\n')

    @staticmethod
    def escrever_registro_valido(entrada: str):
        """ Método para escrever registros válidos no resultado """
        # usa o append (a) para não apagar nenhum registro anterior
        with open(ClasseRegistros.REG_VAL, 'a', encoding="utf-8") as arq:
            arq.write(f'{entrada} - {ClasseRegistros.data_e_hora()}\n')

    @staticmethod
    def data_e_hora():
        """Para colocar data e hora em formato dd/mm/aaaa - hh:mm:ss.mmmm"""
        agora = datetime.datetime.now()
        data = agora.strftime("%d/%m/%Y - %H:%M:%S.%f")[:-2]
        return f'Data e horário do regidtro: {data}'

    @classmethod
    def instancia_registro(cls, entrada: str):
        """ Chama construtor da classe Registro"""
        return cls(entrada)

    def __str__(self) -> str:
        """ Magic method modificado com str de retorno do objeto Registro"""
        return f'Recebido: {self}'

    def __del__(self) -> None:
        """Magic method modificado com retorno para deleçao do objeto"""
        print('Objeto tipo Registro deletado.')

###############################################################################
