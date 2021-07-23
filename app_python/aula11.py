lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[1]
    #x = a
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro au realizar uma operação aritmética!')
except IndexError:
    print ('Erro: índice inválido da lista!')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre nenhuma exceção.')
finally:
    print('Sempre executa!')
    print('Fechando arquivo')
    arquivo.close()
