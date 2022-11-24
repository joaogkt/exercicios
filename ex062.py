try:
    a = int(input('Numero: '))
    b = int(input('Numero: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado digitado!')
except ZeroDivisionError:
    print('Uma divisão não pode ser dividida por zero')
except KeyboardInterrupt:
    print('\nO usario preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado')
