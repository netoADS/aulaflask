t = 0
while t < 3:
    s = input('Digite a senha: ')
    if s == 'senha123':
        print('Acesso concedido!')
        break
    else:
        print('Senha incorreta. Tente novamente.')
        t += 1
else:
    print('Você excedeu o numero maximo de tentativas.')