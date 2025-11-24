import sqlite3


nota_1= int(input('Fale a primeira nota:'))
nota_2= int(input('Fale a segunda nota:'))


soma_nota= nota_1 + nota_2 
media_nota= soma_nota / 2

mensagem_aprovado= f'Parabéns você passou, sua nota é: {media_nota :.2f}'
mensagem_media= f'Parabéns você esta acima da média, sua nota é: {media_nota :.2f} '
mensagem_reprovado= f'Você está de recuperação, sua nota é: {media_nota :.2f}'

if media_nota >= 30: 
    print (f'{mensagem_aprovado}')
 
elif media_nota >= 18: 
    print (f'{mensagem_media}')
else: 
  print (f'{mensagem_reprovado}')

medias = [1, 2]


while True:
    finalizar_tarefa = input('Para finalizar digite "sair": ')
    if finalizar_tarefa == 'sair':
        break
