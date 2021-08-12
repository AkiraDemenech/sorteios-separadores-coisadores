


import __equipes__ as sorteador
ingressantes = sorteador.ano_atual
resultados=sorteador.resultados
tipo	 = sorteador.tipo
listagem = '_apadrinhamento_'
razao	 = 2,2	#calouro(a)(s)/veterano(a)(s)
geral	 = list(sorteador.listar(listagem,tipo))
turmas	 = sorteador.separar(geral)

def separar (estudantes=geral,proporcao=razao):
	if type(estudantes) != dict:
		estudantes = sorteador.separar(estudantes)
	grupos = {}
	for curso in estudantes:
		nova_turma = ingressantes
		if not nova_turma in estudantes[curso]:
#			c = len(estudantes[curso][nova_turma])
#		else:
			c = list(estudantes[curso])
			c.sort()
			nova_turma = c[len(c)-1]
		print('ingressantes em',curso,nova_turma)
#		print('Turma',nova_turma,'não encontrada em',curso,'e trocada então por',c)
		c = len(estudantes[curso][nova_turma])
		v = 0
		grupos[curso] = []
		rc,rv = proporcao
		velhas_turmas = []
		for turma in estudantes[curso]:
			if turma != nova_turma:
				v += len(estudantes[curso][turma])
				velhas_turmas.append(turma)
			print(curso,turma,'[%d pessoas]' %len(estudantes[curso][turma]))
		print(v,'estudantes das para apadrinhamento de',c,'ingressantes [~%f veterano(a)(s) por ingressante]' %(v/c))
		if v/c < rv/rc:
			print('\tProporção %d calouro(a)(s) : %d veterano(a)(s) insuficiente' %proporcao)
			while v/c < rv/rc:
				rc += 1
			print('\tAlterada para %d calouros(as) : %d veterano(a)(s)' %(rc,rv))
		while len(estudantes[curso][nova_turma]) > 0:
			g,v = [], []
			for r in range((rc,len(estudantes[curso][nova_turma]))[len(estudantes[curso][nova_turma])<2*rc]):
				g.append(estudantes[curso][nova_turma].pop(int(len(estudantes[curso][nova_turma])*sorteador.random())))#.nome)
#				g.insert(0,estudantes[curso][nova_turma].pop(int(len(estudantes[curso][nova_turma])*sorteador.random())))
#				g[0].matricular(eq=v)
			g.sort()
			grupos[curso].append([tuple(g),v])
#			grupos[curso][tuple(g)] = []
		g = 0
		grupos[curso].sort()
		velhas_turmas.sort()
		velhas_turmas.reverse()
		for turma in velhas_turmas:
			while len(estudantes[curso][turma]) > 0:
				v = estudantes[curso][turma].pop(int(len(estudantes[curso][turma])*sorteador.random()))
				v.padr = grupos[curso][g][0]#v.matricular(eq=grupos[curso][g][0])
				grupos[curso][g][1].append(v)
				g = (g+1)%len(grupos[curso])
			print(curso,turma)
	return grupos

def fechar (grupos=None, pasta=resultados, extencao=tipo):
	if grupos == None:
		grupos = separar()
	elif type(grupos) != dict:
		grupos = separar(grupos)
	estudantes = []
	try:
		sorteador.mkdir(pasta)
	except FileExistsError:
		pass
	res = pasta + ('/%d%02d%02d%02d%02d%02d.apadrinhamento' %sorteador.localtime()[:6]) + extencao
	a = sorteador.abrir(res, 'w', encoding="utf-8")
	for curso in grupos:
		a.write('\n\n%s\n' % curso)
		for c,v in grupos[curso]:
			t,s = '','\t'
			i = len(c)
			while i > 0:
				i += -1
				t = c[i].nome + s + t
				s = ', '
			a.write(t)
#			a.write(str(c).replace('(','\n').replace(')','\t'))
			v.sort()
			v.reverse()
			c = t
			t,s = '','\n'
			for vet in v:
				vet.padr = c#matricular(eq=c)
				estudantes.append(vet)
				t = '%s (%d)%s%s' %(vet.nome,vet.turma,s,t)
				s = ', '
			a.write(t)
	estudantes.sort()
	for v in estudantes:
		a.write('\n%s\t%s' %(str(v),v.padr))#equipe))
	a.close()
	return res

if __name__ == '__main__':
	print('\tINÍCIO\t',*sorteador.localtime()[:6])
	t = sorteador.time()
	sorteador.notas(fechar())
	t = sorteador.time() - t
	print(t,'segundos gastos\n\tFINAL\t',*sorteador.localtime()[:6])
	input()
'''
for c in turmas:
	for a in turmas[c]:
		for e in turmas[c][a]:
			print(e)
		input()
'''
#sorteador.normalizar(txt.read().splitlines())