class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()
    
    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1
    
    def __str__(self):
        return f'{self._nome} | {self.ano} | {self._likes} Curtidas'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'{self._nome} | {self.ano} | {self.duracao} minutos | {self._likes} Curtidas'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self._nome} | {self.ano} | Temporadas: {self.temporadas} | {self._likes} Curtidas'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]
    
    def __len__(self):
        return len(self._programas)
    
    @property
    def listagem(self):
        return self._programas
    

vingadores = Filme('Vingadores: Guerra Infinita', '2018', '160')
atlanta = Serie('Atlanta', '2018', '2')
tmep = Filme('Todo mundo em pânico', '1999', '100')
demolidor = Serie('Demolidor', '2016', '2')

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
