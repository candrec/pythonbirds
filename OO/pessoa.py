class Pessoa:
    def __init__(self,nome=None,idade=41):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(p)}'


if __name__ == '__main__':
    p = Pessoa('Carlos')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'André'
    print(p.nome)
    print(p.idade)
