'''1.
Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for x in masini:
    print('1. Masina mea preferata este ' + x)

'''2.
Aceeasi lista
Folositi un for
In for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
Printati varianta finala a listei
'''

for x in range(len(masini)):
    if x != 0 and x != len(masini)-1:
        masini[x] = masini[x].upper()
print(masini)

'''3. 
Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam	'''
masina_dorita = 'Mercedes'
for x in masini:
    if x == masina_dorita.upper():
        print('3. Am gasit masina dorita de dvs.')
        break
    else:
        print('3. Am gasit masina ' + x + '. Mai cautam')

'''4.
Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
Printati S-ar putea sa va placa masina x
'''

for x in masini:
    if x == 'TRABANT' or x == 'LASTUN':
        continue
    else:
        print ('4. S-ar putea sa va placa masina ' + x)

'''5. 
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi
Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
'''

masini_vechi=[]
for x in masini:
    if x == 'TRABANT' or x == 'LASTUN':
        masini_vechi.append(x)
        masini[masini.index(x)] = 'Tesla'
print('5. Modele vechi: ' + str(masini_vechi))
print('Modele noi: ' + str(masini))

'''6. 
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
Iterati prin lista
'''
buget = 15000
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

for x,y in pret_masini.items():
    if y < buget:
        #print(pret_masini.items())
        print('6. Pentru un buget de sub '+ str(buget) + ' puteti alege masina ' + x)

'''   7.
Avand lista
numere =  [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
trei = 0
for x in numere:
    if x == 3:
        trei +=1
print('7. Trei apare de ' + str(trei) + ' ori')

'''8. 
Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
'''
suma_numere = 0
for x in numere:
    suma_numere += x
print('8. Suma numerelelor este: ' + str(suma_numere))

'''9. 
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''
y = numere[0]
for x in numere:
    if x > y:
        y = x
print('9. Numarul cel mai mare din lista este: ' + str(y))

'''10.
Aceeasi lista
Iterati prin ea
Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
Ex: daca e 3, sa devina -3
Afisati noua lista
'''

for x in numere:
    if x > 0:
        numere[numere.index(x)] = 0-x
print(numere)

'''c. Optionale (may need google)

11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere 
Populati corect celelalte liste
Afisati cele 4 liste la final
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for x in alte_numere:
    if x%2 == 0:
        if x >= 0:
            numere_pozitive.append(x)
            numere_pare.append(x)
        else:
            numere_negative.append(x)
            numere_pare.append(x)
    else:
        if x < 0:
            numere_negative.append(x)
            numere_impare.append(x)
        else:
            numere_pozitive.append(x)
            numere_impare.append(x)
print('11. Numere pare: ' + str(numere_pare))
print('11. Numere impare: ' + str(numere_impare))
print('11. Numere pozitive: ' + str(numere_pozitive))
print('11. Numere negative: ' + str(numere_negative))

'''12.
Aceeasi lista
Ordonati crescator lista fara sa folositi sort
Va puteti inspira vizual de aici
https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
print(alte_numere)
for x in range(0,len(alte_numere) - 1):
    for y in range (x+1,len(alte_numere)):
        if(alte_numere[x] > alte_numere[y]):
            alte_numere[x], alte_numere[y] = alte_numere[y], alte_numere[x]
print(alte_numere)

'''13.
Ghicitoare de numar
numar_secret = Generati un numar random intre 1 si 30
Numar_ghicit = None
Folosind un while
   User alege un numar
   Programul ii spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitari! Ai ghicit!
'''

import random
numar_secret = random.randint(1,30)
print(numar_secret)
numar_ghicit = int(input('Completati un numar: '))
while numar_ghicit != numar_secret:
    if numar_ghicit < numar_secret:
        print ('Nr secret este mai mare')
    else:
        print ('Nr secret este mai mic')
    numar_ghicit = int(input('Completati un numar: '))
else:
    print('Felicitari! Ai ghicit!')

'''14. 
Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''
numar = int(input('Completati un numar: '))
for x in range(1,numar+1):
    print(x*str(x))

'''15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)
'''

tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for x in tastatura_telefon:
    for y in x:
        print('Cifra curenta este ' + str(y))

'''16. Avand lista 
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel'] 

Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for x in range(0,len(masini)):
    print('[for] Masina mea preferata este ' + masini[x])

for x in masini:
    print(f'[for each] Masina mea preferata este {x}')

x = 0
while x <= len(masini)-1:
    print('[while] Masina mea preferata este ' + masini[x])
    x+=1