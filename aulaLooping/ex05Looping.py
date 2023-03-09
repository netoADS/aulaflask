#mn = maior_numero
#n = número

#armazena um número pequeno
mn = -100

#entra com o primeiro número
n = int(input('Entre com um número ou digite -1 para parar: '))

#se o numero não for igual a -1 continua
while n != -1:
    #o numero é maior que o mn
    if n > mn:
        #sim, atualiza o mn
        mn = n
    # entre com o próximo número.
    n = int(input("Entre com um número ou digite -1 para parar: "))
    
#print the largest number
print("o maior número é: ", mn)