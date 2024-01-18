from validate_docbr import CPF, CNPJ

class Documento:
    
    @staticmethod
    def criar_documento(documento):
        if len(documento) == 11:
            return Doc_Cpf(documento)
        elif len(documento) == 14:
            return Doc_Cnpj(documento)
        else:
            raise ValueError('Quantidade de dígitos incorreta!')


class Doc_Cpf:
    def __init__(self, documento):
        if self.validar(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido!')
    
    def __str__(self):
        return self.formatar()

    def validar(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formatar(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class Doc_Cnpj:
    def __init__(self, documento):
        if self.validar(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido!')
    
    def __str__(self):
        return self.formatar()

    def validar(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formatar(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
