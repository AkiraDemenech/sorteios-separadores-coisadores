

from random import random
from os import system,mkdir
from time import localtime,time
ano_atual	= localtime().tm_year
matr_digit	= len(ano_atual.__repr__()) #4
marcador	= '\t'
resultados	= 'Sorteios'
retirada	= '_monitoria_'
listagem	= '_cursos_'
cores	= '_cores_'
tipo	= '.txt'
qtd_equipes	= 6#8

class Estudante:

	def __str__ (self,hide=True):
		a = self.curso + self.separador + str((self.matricula,self.turma)[hide]) + self.separador
		try:
			return a + self.nome
		except AttributeError:
			return a + 'None'
	
	def __repr__ (self):
		return '%s(%s)' %(self.__class__.__name__,str(self).__repr__())#,self.turma,self.curso.__repr__()) 

	def __eq__ (self,outro):
		return not self.__ne__(outro)
	def __ne__ (self,outro):
		#return self.__lt__(outro) or self.__gt__(outro)
		try:
			if self.nome != outro.nome:
				return True
		except AttributeError:
			if type(outro) != Estudante:
				return True
		return self.turma != outro.turma  or self.curso != outro.curso # or self.matricula != outro.matricula
	def __le__ (self,o):
		try:
			return self.nome.__le__(o.nome)
		except AttributeError:
			return self.matricula.__le__(o.matricula)
	def __ge__ (self,o):
		try:
			return self.nome.__ge__(o.nome)
		except AttributeError:
			return self.matricula.__ge__(o.matricula)
	def __gt__ (self,o):
		return not self.__le__(o)
	def __lt__ (self,o):
		return not self.__ge__(o)
	
	def __init__ (self, registro=None, separador=marcador, turma=ano_atual, curso=None):
		self.separador = separador

#		if type(registro) == str:
		try:
			registro = separar(registro,self.separador)
		except IndexError:
			raise RuntimeError('Informações para Estudante não-encontradas')
#			print(registro,'insuficiente e inadequado')
		try:
#			err = tuple(registro)
			self.nome = registro.pop(len(registro) - 1).upper()
			self.matricula = registro.pop(len(registro) - 1)#[len(registro) - 2]
			try:
				turma = int(self.matricula[:matr_digit])#4])
			except ValueError:
				print('Matrícula',self.matricula,'malformada')
			curso = registro.pop(len(registro) - 1)#[len(registro) - 3]
		except IndexError:
#			print('Elemento(s) faltante(s) em',err)
			pass
#		except AttributeError:
#			print('Falha geral de',registro)
		finally:
			self.matricular(turma,curso)

	def matricular (self,*em,eq=None):
		if eq != None:
			self.equipe = eq
		for e in em:
			if type(e) == int:
				self.turma = e
			else:
				self.curso = str(e).title()

	separador = matricula = equipe = None

def abrir (arq=None,arg='r',**args):
	try:
		return open(arq,arg,**args)
	except FileNotFoundError:
		open(arq,'w',**args).close()
		return abrir(arq,arg,**args)

def ler (a):
	try:
		b = abrir(a)
		c = b.read()
	except UnicodeDecodeError:
		b = abrir(a,encoding="utf-8")
		c = b.read()
	b.close()
	return c

def bordas (texto, soletras=False):
	i = 0
	j = []
	for inc in (1,-1):
		while True:
			if i >= len(texto):
				return 0,-1
			if soletras:
				if texto[i].isalpha():
					break
			else:
				if texto[i].isalnum():#.isspace():
					break
			i += inc
		j.append(i)
		i = len(texto) - 1
	return j

def normalizar (frase,radical=None):
	if type(frase) in (set,tuple,list):
		if radical == None:
			radical = True
		ol = []
		for l in frase:
			try:
				ol.append(normalizar(l,radical))
			except Exception:
				pass#ando pano para qualquer exceção da execução (ignorando qualquer linha "vazia")
		if radical:
			ol.sort()
		return type(frase)(ol)
	i,f = bordas(frase,radical)
	return frase[i:f+1]

def listar (cursos=listagem,extencao=tipo):#,exclusao=retirada):#deslistar()):

#	if type(cursos) == str:
	if not type(cursos) in (list,set,tuple):
		o = ler(cursos+extencao)
		try:
			cursos = tuple(eval(o))#normalizar(o.read().splitlines())
		except Exception as se:
			print('Escreva corretamente a lista de cursos em',cursos+extencao,'ou altere o endereço para leitura\n\tSintaxe atual:\n'+o)
			raise se
#	exclusao = deslistar(exclusao,extencao)
	for curso in cursos:
		c = 0
		d = ler(curso+extencao).splitlines()
		if '.' in curso:
			curso = curso[:curso.find('.')]
		for l in d:
			try:
				e = Estudante(l,curso=curso)
				c += 1
#				print(e.nome)#.__str__(True))
			except RuntimeError:
				pass
			else:
#				if not e in exclusao:
				yield e
		print(curso,c)
	return 

def deslistar (remocao=retirada,extencao=tipo):
	if not type(remocao) in (list,set,tuple):
		remocao,d = [],ler(retirada+extencao).splitlines()
		for l in d:
			try:
				e = Estudante(l)
				remocao.append(e)
			except RuntimeError:
				continue
	else:
		if type(remocao) != list:
			remocao = list(remocao)
		d = len(remocao)
		while d > 0:
			d += -1
			if type(remocao[d]) != Estudante:
				remocao[d] = Estudante(remocao[d])

	return remocao

def separar (linha=None,div=marcador,extra=[],menos=[None]):

	if type(linha) == str:
		return normalizar(linha).split(div)

	if type(linha) == dict:
#		if menos == None:
#			menos = deslistar()
		if div == marcador:
			div = qtd_equipes
#		q = div
		for equipe in extra:
			q = len(equipe)
			while q > 0:
				q += -1
				if equipe[q] in menos:
					print('Remoção:',equipe.pop(q))
#		equipes = ([],)*div
		equipes = extra
		q = int(div*random())
		while len(equipes) < div:#q > 0:
			equipes.append([])
#			q -= 1
		for c in linha:
			print(c)
			for t in linha[c]:
				print(t,type(linha[c][t]))
				t = list(linha[c][t])
				e = div - 1
				while e > 0:
					if len(equipes[q]) > len(equipes[e]):
						q = e
					e -= 1 
#				for e in linha[c][t]:
				while len(t) > 0:
					e = t.pop(int(len(t)*random()))
					e.matricular(eq=q)
					equipes[q].append(e)
#					print(e.nome)
					q -= 1
					if q < 0:
						q = div-1
					
		return equipes

	if linha == None:
		linha = list(listar())
	
	if div == marcador:
		div = {}
#	else:
#		print('mantido dicionário',div)

#	linha = list(linha)
	print(len(linha),'estudantes nos cursos')

	for a in linha:
		if not a.curso in div:
			div[a.curso] = {}
		if not a.turma in div[a.curso]:
			div[a.curso][a.turma] = []
		try:
			if a in extra[a.curso][a.turma] or a in menos:
#				print('já presente',a)
				continue
		except Exception:#KeyError:
			pass
		div[a.curso][a.turma].append(a)
#		else:
#			print('já presente',a)

	return div

def notas (arq=''):
	for c in ('start notepad','open -t','nano'):
		if system(c+' '+arq) == 0:
			break		

def fechar (equipes=None,nomes=cores,pasta=resultados,extencao=tipo):
	if equipes == None:
		equipes = separar(separar())
	if not type(nomes) in (tuple,list,set):
		try:
			nomes = list(eval(ler(nomes+extencao)))
			nomes.sort()
			nomes.reverse()
		except Exception as se:
			print('Escreva corretamente a lista de cores em',nomes+extencao,'ou altere o endereço para leitura\n\tSintaxe atual:\n'+ler(nomes+extencao))
			raise se
	b = len(equipes)
	if len(nomes) < b:
		print(len(nomes),'cores insuficientes para as',b,'equipes')
	geral = []
	try:
		mkdir(pasta)
	except FileExistsError:
		pass
	res = pasta + ('/%d%02d%02d%02d%02d%02d.equipes' %localtime()[:6]) + extencao
	a = abrir(res, 'w', encoding="utf-8")
	while b > 0:
		b += -1
		equipes[b].sort()
		c = '%s\t [%d pessoas]' %(nomes[b],len(equipes[b]))
		print(b,c)
		a.write('\n\n'+c)
		geral.extend(equipes[b])
		for c in equipes[b]:	
			c.matricular(eq=nomes[c.equipe])
			if c.equipe != nomes[b]:
				print(c,'inconsistente %s != %s'%(nomes[b],c.equipe))
				c.matricular(eq=nomes[b])
			a.write('\n'+str(c))
					
	geral.sort()
	c = '%d estudantes na Lista Geral' %len(geral)
	print(c)
	a.write('\n\n\n'+c)
	for c in geral:
		a.write('\n'+c.equipe+c.separador+str(c))
	a.close()
	return res

if __name__ == '__main__':
	print('\tINÍCIO\t',*localtime()[:6])
	t = time()
	notas(fechar())
	t = time() - t
	print(t,'segundos gastos\n\tFINAL\t',*localtime()[:6])
	input()

'''	
#print(Estudante(Estudante('').__str__()))
print(Estudante(' -.  0a12300123 asfjaosfas fafjnaosfjnaf 10241-').__repr__())
print(Estudante(' -.  0a12300123	asfjaosfas fafjnaosfjnaf aj fanfa ,a ,, ').__str__(True))
print(Estudante(' -.  woiaf	012300123	asfjaosfas fafjnaosfjnaf aj fanfa ,a ,, '))
'''
"""
pasta = 'Google Drive\\Estudantil\\Grêmio\\Gincana e um pouco mais\\Equipes.py\\2020\\'
estudantes = []
for curso in ('biotec','tinfem'):
	for tipo in ('.txt','_calouros.txt'):
		o = open(pasta+curso+tipo,"r")#,encoding="utf-8")
		estudantes.extend(o.read().splitlines())
		o.close()
a = len(estudantes)
while a > 0:
	a += -1
	estudantes[a] = Estudante(estudantes[a])
'''	print(estudantes[a].__str__(True))
input()'''
a = list(listar())
print(len(a),'estudantes')
print(separar({}))
a = separar(separar())
input()
for e in a:
	print(e)
input()

a = separar()
for c in a:
	print(c)
	for t in a[c]:
		print(t)
		for e in a[c][t]:
			print(e.nome)
#input()"""