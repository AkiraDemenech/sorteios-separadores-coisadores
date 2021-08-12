
'''
import sys
sai = sys.stdout
sys.stderr = sys.stdout = open('chamada.log','w')
'''
 # caractere ou substring separando Nome Completo e as outras informações (utilizado para separar colunas de entrada ou de saída)
sep = '\t'

# os arquivos de registro de presença para serem lidos.
abre = {'presença_01.txt', 'presença_02.txt', 'presença_03.txt', 'presença_04.txt', 'presença_05.txt', 'presença_06.txt'}
min = len(abre) * .75 #	A presença mínima para receber certificado é estar em 75% dos registros.

prefixo = 'controle_'
certificado = prefixo + 'certificado.txt'
parcial = prefixo + 'presença.txt'

ult = lambda l: l[len(l) - 1] # elemento do maior índice

def cert (resultado = certificado, entrada = parcial, separador = sep, freq_min = min):
	n_cert = []

	g = open(resultado,'w',encoding='utf8')
	for p in open(entrada,'r',encoding='utf8').read().splitlines():
		try:
			p = p.split(separador)
			presente = p[1].strip().upper().split() 
			curso = set()
			if len(p) > 1:
				for c in eval(p[2]):				
					curso.add(ult(c.split()).title())
			freq = eval(p[0])			
			if freq < freq_min:
				n_cert.append((-freq,presente,curso))
			else:	
				print(*presente,separador,freq,separador,*curso,file=g)					
		except AttributeError:
			print('problema em\t',p,presente,freq)
			
	print('\nNão obtiveram frequência suficiente:',file=g)		
			
	n_cert.sort()
	for p in n_cert:
		print(*p[1],separador,-p[0],separador,*p[2],file=g)		
	g.close()

 	
	
def chama (arquivos_chamada = abre, resultado_geral = parcial, separador = sep, freq_min = min):

	total = {}
	geral = []

	for a in arquivos_chamada:	
		print(a)
		try:
			for presente in open(a,'r',encoding='utf8').read().splitlines():#type(presentes[c]) == str:		
				presente = presente.split(separador)				
				if len(presente) > 1:
					curso = presente[1]
				else:	
					curso = None
				presente = tuple(presente[0].strip().upper().split())				
				if len(presente):
					if not presente in total:	
						geral.append(presente)
						total[presente] = []
					total[presente].append(curso)														
				else: 	
					print(presente,curso)
		except FileNotFoundError:
			print('\tnão encontrado')
	#	presentes.sort()	
	geral.sort()
	g = open(resultado_geral,'w',encoding='utf8')
	n_cert = []

	for p in geral:
		print(len(total[p]),separador,*p,separador,total[p],file=g)#{ult(c.split()).title() for c in total[p]}
		if freq_min > len(total[p]):
			n_cert.append(p)
	g.close()	
	#print('Sucesso!',len(geral))	
	
	return len(geral),len(n_cert)
	
	
	
if input('F para só finalizar\n').strip().upper()[0] != 'F':		
	input('Sucesso em %d presenças!\nEncontradas %d frequências insuficientes.\tAguardando confirmação para separá-las:' %chama())
cert()	
	

input('Finalizado sem erros?')


#sys.stdout.close()

