from random import randint

#for i in range(100):
#    print(randint(1,10))

los= randint(1,10)
odp=-1
i=0

print("Zgdnij liczbę z przedziału 1 do 10")

while odp != los:
    i+=1
    odp=int(input("Podaj liczbę: "))
    if odp> los:
        print("Liczba większa niż los")
    elif odp<los:
        print("Liczba mniejsza niż los")
print("Brawo! Odgadłeś za", i, "razem")

