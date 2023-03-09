t = input('Digite o tipo de numero que deseja imprimir (par ou impar): ')
for i in range(1, 11):
    if t == "par" and i % 2 == 0:
        print(i)
    elif t == "impar" and i % 2 != 0:
        print(i)