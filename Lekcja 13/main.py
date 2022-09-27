def dzielenie(x,y):
    assert y!=0, "Y==0"

    if y==0:
        raise ZeroDivisionError("Dzielenie przez 0")

    print(x/y)
try:
    dzielenie(2,4)

except ZeroDivisionError:
    print("Błąd!")
    raise

