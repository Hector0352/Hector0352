#requisitar tamanho da chave e mensagem
chave = int(input('\n'))
mensagem = input()

#base de letras
base = 'abcdefghijklmnopqrstuvwxyz'
crip = ''

for palavra in mensagem:
    if palavra in base:
        palavra_index = base.index(palavra)
        crip += base[(palavra_index + chave) % len(base)]
    else:
        crip += palavra

print(mensagem)
print(crip)