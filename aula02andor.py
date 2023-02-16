idade = int(input("Digite a sua idade: "))
dinheiro = int(input("Digite a quantidade de dinheiro que você tem: "))

if idade >= 18 or dinheiro >= 50:
    print("Você pode entrar na festa.")
else:
    print("Você não pode entrar na festa.")