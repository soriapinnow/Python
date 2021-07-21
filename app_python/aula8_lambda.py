contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a+b
subtracao = lambda a, b: a - b
print(soma(5 ,10))
print(subtracao(10,5))

calculadora = {
    'soma' : lambda a ,b: a + b,
    'subtracao' : lambda a,b: a - b,
    'multiplicacao' : lambda a, b: a * b,
    'divisao' : lambda a, b: a / b,
}
print(type(calculadora))
soma = calculadora['soma']
#soma = lambda a, b: a + b
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora ['divisao']
print('A Soma é: {}'.format(soma(10,5)))
print('A Subtração é : {}'.format(subtracao(10,2)))
print('A multiplicação é : {}'.format(multiplicacao(10,2)))
print('A Divisão é : {}'.format(int(divisao(10,2))))