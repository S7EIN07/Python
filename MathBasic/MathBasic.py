class MathBasic:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            return 'Erro de divisão: Não é possível dividir por 0'
        return a / b
    