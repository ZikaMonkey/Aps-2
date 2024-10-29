import pickle

cidades = []
pop = []
ext = []
limite = 100

cidades = pickle.load(open("cidades.dat", "rb"))
pop = pickle.load(open("populacao.dat", "rb"))
ext = pickle.load(open("extensao.dat", "rb"))

print('1. Adicionar novas cidades')
print('2. Ver lista de cidades completa')
print('3. Deletar uma cidade da lista')
print('4. Se informar de uma cidade especifica')
print('5. Qual é a cidade mais extensa')
print('6. Qual é a cidade mais populosa')
resp = int(input('O que deseja fazer (use os números para escolher): '))
if (resp == 1):
    quant = int(input('Digite a quantidade de cidades que quer adicionar: '))
    if quant > 100:
        print('Você só pode adicionar o máximo de 100 cidades')
    for i in range(quant):
        cidades.append((input)('Digite o nome da cidade: '))
        pop.append(int(input('Digite a população da cidade: ')))
        ext.append(float(input('Digite a extensão da cidade em km²: ')))
        pickle.dump(cidades, open("cidades.dat", "wb"))
        pickle.dump(pop, open("populacao.dat", "wb"))
        pickle.dump(ext, open("extensao.dat", "wb"))

if (resp == 2):
    cidadeslimit = cidades[:limite]
    for number, name in enumerate(cidadeslimit,0):
        print(str(number)+'.', name)

if (resp == 3):
    for number, name in enumerate(cidades,0):
        print(str(number)+'.', name)
    delc = int(input('Qual cidade deseja deletar? (Use os números): '))
    del(cidades[delc])
    del(pop[delc])
    del(ext[delc])
    pickle.dump(cidades, open("cidades.dat", "wb"))
    pickle.dump(pop, open("populacao.dat", "wb"))
    pickle.dump(ext, open("extensao.dat", "wb"))

if (resp == 4):
    cidadeslimit = cidades[:limite]
    for number, name in enumerate(cidadeslimit,0):
        print(str(number)+'.', name)
    info = int(input('Digite a cidade que quer obter as informações (Use os números): '))
    print(cidades[info],'tem a população de', pop[info],'pessoas e a extensão territorial de', ext[info],'km²')

if (resp == 5):
    maxext = ext.index(max(ext))
    print('A cidade mais extensa é: ', cidades[maxext],'com',max(ext),'km²')


if (resp == 6):
    maxpop = pop.index(max(pop))
    print('A cidade mais populosa é:', cidades[maxpop],'com',max(pop),'pessoas')



