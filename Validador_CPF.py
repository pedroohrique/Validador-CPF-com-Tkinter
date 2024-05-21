class ValidadorCPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def _calcula_digito(self, cpf_parcial, multiplicadores):
        somatoria = sum(int(digito) * multiplicador for digito, multiplicador in zip(cpf_parcial, multiplicadores))
        resto = somatoria % 11
        return 0 if resto < 2 else 11 - resto

    def obtem_primeiro_digito(self):
        cpf_parcial = self.cpf[:9]
        multiplicadores = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        primeiro_digito = self._calcula_digito(cpf_parcial, multiplicadores)
        return cpf_parcial + str(primeiro_digito)

    def obtem_segundo_digito(self):
        cpf_parcial = self.obtem_primeiro_digito()
        multiplicadores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        segundo_digito = self._calcula_digito(cpf_parcial, multiplicadores)
        return cpf_parcial + str(segundo_digito)

    def verifica_sequencia(self):
        return self.cpf == self.cpf[0] * len(self.cpf)

    def valida_cpf(self):
        if len(self.cpf) != 11 or not self.cpf.isdigit() or self.verifica_sequencia():
            return False
        return self.cpf == self.obtem_segundo_digito()