#Armazene o nome de uma pessoa em uma variável e apresente com uma mensagem. PG61
Nome = 'Mikael'
Mensagem = ' Seja bem vindo de volta ao Python!'
print(Nome + Mensagem)

#Mostrar o nome em minusculo e maiusculo
print('\nSeu nome maiusculo: {}'.format(Nome.upper()))
print('Seu nome em minusculo é {}'.format(Nome.lower()))

#Citação famosa
citação = '\nNão deixem fazerem pensar que você não é capaz de fazer algo só por que essa pessoa não conseguiu, se quer algo, lute por isso e ponto final \n~A procura da felicidade.'
print(citação)

#Remover os caracteres em branco.
nomeEspaçado = '    Mikael    '
print('\nSeu nome com a função strip() fica: {}.'.format(nomeEspaçado.strip()))
print('Seu nome com a função lstrip() fica: {}.'.format(nomeEspaçado.lstrip()))
print('Seu nome com a função rstrip() fica: {}.'.format(nomeEspaçado.rstrip()))

#FIM