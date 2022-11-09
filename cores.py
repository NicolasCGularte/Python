Cores
no
Terminal
#\033['style';
'text';
'back'
m
'style' = negrito, italico, sublinhado
'text' = cor
do
texto
'back' = cor
do
fundo

EXEMPLO  #
#\033[0;
33;
44
m

#style:
0 - None
1 - Bold(negrito)
4 - Underline(sublinhado)
7 - Negative

#text:
30 - branco
31 - vermelho
32 - verde
33 - amarelo
34 - azul
35 - roxo
36 - azul
bebe
37 - cinza(DEFAULT)

#back:
40 - branco
41 - vermelho
42 - verde
43 - amarelo
44 - azul
45 - roxo
46 - azul
bebe
47 - cinza(DEFAULT)

print('\033[0;30;41mHello, world!\033[m')
print('\033[4;33;44mHello, world!\033[m')
print('\033[1;35;43mHello, world!\033[m')
print('\033[30;42mHello, world!\033[m')
print('\033[mHello, world!\033[m')
print('\033[7;30mHello, world!\033[m')

nome = 'Tauan'
cores = {'limpa': '\033[m', 'azul': '\033[34m'}
print('Muito prazer {}{}{}!'.format(cores['azul'], nome, cores['limpa']))
'''Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Muito
prazer
Tauan!
