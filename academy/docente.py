#coding: utf-8

from pessoa import Pessoa

class Docente(Pessoa):

	_ID = 1

	def __init__(self, nome, nascimento):
		Pessoa.__init__(self, nome, nascimento, "docente")
		self.id = self._ID; self.__class__._ID += 1
		self.disciplina = []

#	def avaliar(self, alunos)
#	"""
#	Método para avaliação do aluno
#	"""
#	lista_alunos = []
#	
#		lista_alunos.append(alunos)
#	else:
#		lista_alunos = alunos
#	for aluno in lista_alunos:



