class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.falando:
            print(f"{self.nome} está falando, não pode comer")
            return
        elif self.comendo:
            print(f"{self.nome} já está comendo {alimento}")
            return
        print(f"{self.nome} comendo {alimento}")
        self.comendo = True

    def pararComer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo nada")
        else:
            print(f"{self.nome} para de comer")
            self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} está comendo, não pode falar")
            return
        elif self.falando:
            print(f"{self.nome} já está falando sobre {assunto}")
            return
        print(f"{self.nome} falando sobre {assunto}")
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f"{self.nome} não está falando")
        else:
            print(f"{self.nome} para de falar")
            self.falando = False
