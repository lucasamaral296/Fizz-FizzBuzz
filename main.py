""" Escreva um programa que imprima os números inteiros de 1 a 50. 
Para multiplos de três imprima 'Fizz' na frente do número, e para
os múltiplos de cinco imprima 'Buzz'. Para os números que são múltiplos 
de três e cinco imprima 'fizzBuzz'  """


for i in range(1,51):   # range de 1 a 50 
    if i % 3 == 0 and i % 5 == 0:  # se o resto da divisao for zero, significa que é multiplo.
        print(i, '- FizzBuzz')
    elif i % 3 == 0:
        print(i, '- Fizz')
    elif i % 5 == 0:
        print(i, '- Buzz')