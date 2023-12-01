import random


casa=int(input("Digite a quantidade de casas: "))
gato=random.randint(1,casa)
casas=dict.fromkeys(list(range(1,casa+1)),'')
casas[gato]='gato'
while True:
    tentativa=int(input())
    while (
    if (casas[tentativa]=='gato'):
        print('achou')
        break
    else:
        print(casas)
        if (gato==casa):
            casas[gato]=''
            casas[casa-1]='gato'
            gato=casa-1
        elif (gato==1):
            casas[gato]=''
            casas[2]='gato'
            gato=2
        else:
            casas[gato]=''
            gato+=random.choice([-1,1])
            casas[gato]='gato'