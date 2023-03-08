ns = 42
t = 1

while t <= 3:
    p = int(input('Adivinhe o número secreto: '))
    if p == ns:
        print('Parabens, voce acertou! ')
        break
    else:
        if p > ns:
            print('O número secreto é menor do que', p)
        else:
            print('O numero secreto é maior do que', p)
    t += 1
if t > 3:
    print('Suas tentativas acabaram. O numero secreto era', ns)