class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno {aluno.nome} adicionado à turma {self.nome}.")

    def listar_alunos(self):
        print(f"Turma {self.nome}:")
        for aluno in self.alunos:
            print(f" - {aluno}")

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = []
        self.alunos = []

    def adicionar_turma(self, turma):
        self.turmas.append(turma)
        print(f"Turma {turma.nome} adicionada ao curso {self.nome}.")

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno {aluno.nome} adicionado ao curso {self.nome}.")

    def listar_estrutura(self):
        print(f"Curso: {self.nome}")
        for turma in self.turmas:
            turma.listar_alunos()


aluno1 = Aluno("Lucas", 16)
aluno2 = Aluno("Maria", 17)

turma_a = Turma("Turma A")
curso_info = Curso("Informática")

curso_info.adicionar_turma(turma_a)
curso_info.adicionar_aluno(aluno1)
curso_info.adicionar_aluno(aluno2)

turma_a.adicionar_aluno(aluno1)
turma_a.adicionar_aluno(aluno2)

curso_info.listar_estrutura()
