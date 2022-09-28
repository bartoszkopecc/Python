krotka =(2,4,6,16,32,64,128)

print(krotka[0])
print(krotka[6])
print(krotka)

print("Elementów: ",krotka.count(2))
print("Index: ",krotka.index(64))


print("\nWycinki: ")
print(krotka[0:3])
print(krotka[3:5])
print(krotka[3:8])
print(krotka[-4:-2])
print(krotka[0:7:2])
print(krotka[0::2])

print("\nOdwrócona")
print(krotka[::-1])