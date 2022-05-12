def Szambekeres():
    hiba = True
    while hiba:
        hiba = False
        try:
            szam = int(input("Kérek egy pozitív egész számot: "))
            if szam >= 0:
                return szam
        except:
            pass
        hiba = True

def Osszeg(Szamok):
    return sum(Szamok)

def Atlag(Szamok):
    return sum(Szamok) / len(Szamok)

szamok = []
bekertszam = Szambekeres()

while bekertszam != 0:
    szamok.append(bekertszam)
    bekertszam = Szambekeres()

print("5. feladat:")
print("Számok", szamok)

print("6. feladat:")
print("A számok összege:", Osszeg(szamok))
print("A számok átlaga:", Atlag(szamok))

parosszamok = []
paratlanszamok = []

for elem in szamok:
    if elem % 2 == 0:
        parosszamok.append(elem)
    else:
        paratlanszamok.append(elem)
parosszamok.sort()

print("7. feladat:")
print("Legkisebb páros szám:", min(parosszamok))
print("Legnagyobb páros szám:", max(parosszamok))
print("Páros számok száma:", len(parosszamok))
print("Páros számok növekvő sorrendben:", parosszamok)

print("8. feladat:")
print("Legkisebb páratalan szám:", min(paratlanszamok))
print("Legnagyobb páratalan szám:", max(paratlanszamok))
print("Páratalan számok száma:", len(paratlanszamok))
print("páratalan számok:", paratlanszamok)