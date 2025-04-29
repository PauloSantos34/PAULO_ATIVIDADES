
#entrar com os dados de alunos:
 
input('Informe o nome do Aluno: ')

num = float(input('Informe a média final: '))

if num >= 0:
    if num >= 7:
        print('Aluno Aprovado!')
    elif num >=5:
        print('Aluno em recuperação.')
    else:
        print('Aluno Reprovado.')

else:
    print('Valor inválido')
    

 