from excecoes import LanceInvalido

class Usuario:
    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira
    
    def propor_lance(self, leilao, valor):
        if valor > self.__carteira:
            raise LanceInvalido('O valor do lance não pode ser superior ao da carteira!')

        lance = Lance(self, valor)
        leilao.propor(lance)

        self.__carteira -= valor
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def carteira(self):
        return self.__carteira    

class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor
    

class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0
        self.menor_lance = 0

    def propor(self, lance: Lance):
        if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:
            if not self.__lances:
                self.menor_lance = lance.valor
            
            self.maior_lance = lance.valor
        
            self.__lances.append(lance)
        else:
            raise LanceInvalido('O mesmo usuário não pode propor dois lances seguidos!')
    
    @property
    def lance(self):
        return self.__lances[:]
