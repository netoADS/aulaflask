idade = int(input("Digite a sua idade: "))
dinheiro = int(input("Digite a quantidade de dinheiro que você tem: "))
carteira = input("Você tem carteira de motorista?(s/n) ")

if (idade >= 18 and dinheiro >= 50) or carteira == "s":
    print("Você pode alugar um carro.")
else:
    print("Você não pode alugar um carro.")