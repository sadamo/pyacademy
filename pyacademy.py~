#coding: utf-8

from academy.disciplina import Disciplina
from academy.aluno import Aluno
from academy.docente import Docente


jao = Aluno("Jão", "04/02/1934")
print jao.nome, jao.matricula

maria = Aluno("Maria", "12/09/1989")
print maria.nome, maria.matricula


vantuil = Docente("Vantuil", "07/02/1934")

micro = Disciplina("Microprocessadores I", "nabo", "ELT005", 48, vantuil)

print "A disciplina %s (%s) \"%s\" possui %d vagas" % (micro.nome, micro.sigla, micro.descricao, micro.vagas)

micro.matricula = [jao, maria]

print "agora a disciplina %s (%s) \"%s\" possui %d vagas" % (micro.nome, micro.sigla, micro.descricao, micro.vagas)

#micro.desmatricula(matricula = [jao.matricula, maria.matricula])

print "agora a disciplina %s (%s) \"%s\" possui %d vagas" % (micro.nome, micro.sigla, micro.descricao, micro.vagas)

print "o professor é: %s" % micro.docente.nome


micro.avaliar([jao, maria])

print "%s nota: %d" %(jao.nome, jao.disciplina['media'])
print "%s nota: %d" %(maria.nome, maria.disciplina['media'])

