lista=list(range(10))

print(lista)

nowa=[i*2 for i in lista]
nowa2=[i+2 for i in lista if i %2==0]

print(lista)
print(nowa)
print(nowa2)


#Formatowanie String

argumetny=["Sebastian",24]
tekst="Cześć mam na imie {imie} i mam {wiek} lat. {imie}".format(imie=argumetny[0],wiek=argumetny[1])
print(tekst)
