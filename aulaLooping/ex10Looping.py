#up = usuario_palavra
#psv - palavras_sem_vogais

psv = ''
up = input("Entre com uma palavra: ")
up = up.upper()

for letra in up:
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        psv += letra
        
print(psv)