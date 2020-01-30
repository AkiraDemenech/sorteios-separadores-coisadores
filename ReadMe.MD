
     sorteio de Equipes e do Apadrinhamento

este é um daqueles programas que a gente faz por preguiça de executar tarefas manuais. No fim da história demoramos talvez até mais que as tais tarefas manuais demorariam, porém terminamos com algo que faz pela gente

Nem sempre é garantido que esse algo consiga fazer depois sem destruir metade do processamento da máquina ou zoar metade dos arquivos relacionados a o que quer que saia do processo, ou que depois de engavetado por anos volte a funcionar sem depender de alguma configuração esquisita ou de ser refeito.

>    este programinha está já na sua 3ª “reencarnação”/codificação. 
<br>
<br> A vida realmente não é fácil para _scripts_ de pessoas inexperientes

   aqui vão algumas coisas sobre usar essa coisa aí
=
* Das equipes:

As equipes denominadas pelas cores eram necessárias para um ou dois dias de gincana de recepção e é chato sorteá-las com listas em papel....

* Do apadrinhamento:

O apadrinhamento foi como chamamos a (não tão exclusiva assim) organização de estudantes ingressantes terem ajuda _default_ e orientação por veteranas(os)

Quando pela primeira vez feito num mesmo início de ano em que houve também gincana, a independência entre essas duas coisas trouxe reclamações quando estudantes ingressantes não se achavam nas mesmas equipes que quem lhes apadrinhara, aí o uso de um programa foi interessante, finalmente...

* da Recepção

Automatizado o sistema, o que já havia sido reprogramado antes foi então complementado com esse terceiro _script_ que oportunizou que a organização dos dois esquemas se integrou.

A partir do momento que se segue os padrões que a leitura dos arquivos espera, o processo pode se dar sem complicações muito maiores que um grupo de pessoas com tesouras

 #  Padrões e Arquivos:
 
 >> Todas as quantidades, nomes e extenções podem ser alterados(as) nas variáveis que as armazenam nos códigos ou nos argumentos na chamada das funções.

> >>Será criado em branco qualquer arquivo logo que não for encontrado.




<br>
 
        _monitoria_.txt
onde em cada linha se escreve Curso, número de Matrícula e Nome completo (respectivamente separados por _tab_) para retirada de estudantes do sorteio das equipes que, contudo, poderão apadrinhar.
- Somente utilizado em [\_\_recepção__.py](https://github.com/AkiraDemenech/sorteio-EquipesApadrinhamento/blob/master/__recep%C3%A7%C3%A3o__.py) ao chamar  [\_\_equipes__.__separar__](https://github.com/AkiraDemenech/sorteio-EquipesApadrinhamento/blob/master/__recep%C3%A7%C3%A3o__.py#L45) (de novo);

<br>
 
        _apadrinhamento_.txt
onde se escreve uma lista/tupla com os nomes dos arquivos (_strings_) de estudantes que participarão do apadrinhamento.

- O nome dos arquivos (até o primeiro ponto) será considerado o curso de estudantes ali presentes no formato Matrícula\tNome\n
- Linhas de estudantes sem matrícula serão consideradas de ingressantes (turma padrão);

    /* aplicam-se também às leituras relacionadas ao próximo arquivo */

<br>
 
        _cursos_.txt
onde se escreve uma lista/tupla com os nomes dos arquivos (_strings_) de estudantes que participarão das equipes.

<br>

        _cores_.txt
onde se escreve uma lista/tupla com os nomes das equipes (_strings_). 
- Serão utilizadas em ordem alfabética e se insuficientes levarão a resmungos programados

mas, no fim das contas, pode ser que sequer funcione __*\\ :*__
-