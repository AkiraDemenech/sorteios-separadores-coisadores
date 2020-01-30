
import __apadrinhamento__ as sorteador

if __name__ == '__main__':
	print('\tINÍCIO\t',*sorteador.sorteador.localtime()[:6])
	t = sorteador.sorteador.time()
	try:
		for curso in eval(sorteador.sorteador.ler(sorteador.sorteador.listagem+sorteador.sorteador.tipo)):
			if '.' in curso:
#				d = sorteador.sorteador.ler(curso+sorteador.sorteador.tipo)
#				if not ('.' in d or '-' in d or '/' in d):
#					c = True
#					for a in '0123456789':
#						if a in d:
#							c = False
#					if c:		
#						continue
				d = sorteador.sorteador.normalizar(sorteador.sorteador.ler(curso+sorteador.sorteador.tipo).splitlines())
				c = sorteador.sorteador.abrir(curso+sorteador.sorteador.tipo,'w')
				for linha in d:
					if len(linha) == 0:
						print('Linha vazia retirada')
					else:
						c.write(linha+'\n')
				c.close()
				print('Normalização de',curso,'concluída')
	except Exception:
		print('Escreva corretamente a lista de cursos em',sorteador.sorteador.listagem+sorteador.sorteador.tipo,'ou altere o endereço para leitura\n\tSintaxe atual:\n'+sorteador.sorteador.ler(sorteador.sorteador.listagem+sorteador.sorteador.tipo))

	#	formar as equipes primeiro somente com quem participará do apadrinhamento
	equipes	= sorteador.sorteador.separar(sorteador.turmas)
	remova	= sorteador.sorteador.deslistar()
	apadrinhamento = {}
	for equipe in equipes:
		equipe_ap = sorteador.separar(equipe) #	Formar os grupos de apadrinhamento
											#	somente com as pessoas de uma mesma equipe
		for curso in equipe_ap:
			try:
				apadrinhamento[curso] = apadrinhamento[curso] + equipe_ap[curso]
			except KeyError:				#	juntando todas essas num único dicionário			
				apadrinhamento[curso] = equipe_ap[curso]
			apadrinhamento[curso].sort()
		
	#	e somente agora adicionar às equipes as pessoas que faltam
	sorteador.sorteador.separar(sorteador.sorteador.separar(extra=sorteador.turmas,menos=remova),extra=equipes,menos=remova)

	#	finalmente registrando e abrindo os arquivos.
	sorteador.sorteador.notas(sorteador.fechar(apadrinhamento))
	sorteador.sorteador.notas(sorteador.sorteador.fechar(equipes))
	
	
#	sorteador.sorteador.notas(sorteador.fechar())
#	sorteador.sorteador.notas(sorteador.sorteador.fechar())
	t = sorteador.sorteador.time() - t
	print(t,'segundos gastos\n\tFINAL\t',*sorteador.sorteador.localtime()[:6])
	input('Enter para continuar....\n')