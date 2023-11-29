from premia import ustalPremie
from wynagrodzenie import ustalWynagrodzenie

sprzedaz = float(input("Podaj wartość sprzedaży"))
zaliczka = float(input("Podaj warość zaliczki"))
premia = ustalPremie(sprzedaz)
wynagrodzenie = ustalWynagrodzenie(sprzedaz, premia, zaliczka)
print("Wynagrodzenie wynosi: ", wynagrodzenie)