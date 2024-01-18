class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo: {self.__saldo} | Titular: {self.__titular}')
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('O valor solicitado ultrapassou o limite disponível.')

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'