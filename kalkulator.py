def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"

# Przykładowe użycie:
print(dodaj(5, 3))
print(odejmij(5, 3))
print(pomnoz(5, 3))
print(podziel(5, 3))
