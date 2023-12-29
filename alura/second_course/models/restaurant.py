from models.avaliacao import Avaliacao

class Restaurant: 
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
    
    def __str__(self) : 
        return f'{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {self.ativo.ljust(25)} | {str(self.media_avaliacoes).ljust(25)}'
    
    @property
    def ativo(self) :
        return 'Ativo' if(self._ativo) else 'Inativo'

    def alterarEstado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if(nota > 5 or nota <1): 
            print('Valor inválido, apenas notas de 1 a 5 serão consideradas')
            return
    
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)
    
    @property
    def media_avaliacoes(self): 
        if(not self._avaliacoes): 
            return '-'
        
        soma = sum(avaliacao.nota for avaliacao in self._avaliacoes)
        return round(soma/len(self._avaliacoes), 1)
        