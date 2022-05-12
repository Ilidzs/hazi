helyezesek = []
sportolokszamai = []
sportagoknevei = []
versenyszamoknevei = []

file = open("verseny.txt", encoding="utf-8")
elsosor = file.readline()
sor = file.readline()
while sor != "":
    adatok = sor.split(" ")
    helyezesek.append(int(adatok[0]))
    sportolokszamai.append(int(adatok[1]))
    sportagoknevei.append(adatok[2])
    versenyszamoknevei.append(adatok[3])
    sor = file.readline()
file.close()

sportolokszamaiosszesen = sum(sportolokszamai)
print("3. feladat:")
print("Pontszerző helyez", sportolokszamaiosszesen)

arany = 0
ezust = 0
bronz = 0
osszesen = len(helyezesek)

for i in range(len(helyezesek)):
    if helyezesek[i] == 1:
        arany += 1
    elif helyezesek[i] == 2:
        ezust += 1
    elif helyezesek[i] == 3:
        bronz += 1

print("4. feladat:")
print("Arany:", arany)
print("Ezüst:", ezust)
print("Bronz", bronz)
print("Összessen:", osszesen)

print("5. feladat:")
print("Sportágak:", end=" ")
sportagak = []
for elem in sportagoknevei:
    if not elem in sportagak:
        print(elem, end=" ")
        sportagak.append(elem)
print("")

print("6. feladat:")
versenyszamok = len(sportagak)
print("Versenyszámok:", versenyszamok)