#coding: utf-8

from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class Semestre(object):

	_ID = 1 

	def _semestre_nome(self, datetime):
		mes = datetime.month
		
		if mes < 6:
			return '1'
		else:
			return '1'

	def __init__(self):
		self.id = self._ID; self.__class__._ID += 1
		self.nome = "Semestre " + str(date.today().year) + self._semestre_nome(datetime)
		self.alunos = []
		self.disciplinas = []
		self.data_inicio = datetime.today()
		self.data_final = self.data_inicio + relativedelta(months=6)
		
