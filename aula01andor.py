x = int(input("Digite o primeiro numero: "))
y = int(input("Digite o segundo numero: "))
z = int(input("Digite o terceiro numero: "))

if x>y and x>z:
    result = "x é o número maior"
elif y>x and y>z:
    result = "y é o número maior"
elif z>x and z>y:
    result = "z é o número maior"
else:
    result = "ha numeros iguais"
    
print(result)