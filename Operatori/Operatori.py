import random

'''1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.'''
#if reprezinta o splituire a codului pentru rularea unor comenzi in functie de o conditie

#2. Verifică și afișează dacă x este număr natural sau nu.
x = int(input('Introduceti un numar: '))
if x >= 0:
    print('Numar natural')
else:
    print('Numarul nu este natural')

#3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x > 0:
    print('Numarul este pozitiv')
elif x == 0:
    print('Numarul este neutru')
else:
    print('Numarul este negativ')

#4. Verifică și afișează dacă x este între -2 și 13.
if x > -2 and x < 13:
    print('Numarul este intre -2 si 13')

#5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
y = int(input('5. Introduceti inca un numar: '))
if x - y < 5:
    print('Diferenta dintre x si y este mai mica decat 5')

#6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
if not(x > 5 and x < 27):
    print('X nu este intre 5 si 27')

'''7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.'''
if x == y:
    print('x este egal cu y')
elif x > y:
    print(str(x)+' este mai mare(x)')
else:
    print(str(y)+' este mai mare(y)')

'''8.
x, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.'''
z = int(input('8. Introduceti inca un numar: '))
if x <= 0 or y <= 0 or x <= 0:
    print('Valori invalide pentru constructia unui triunghi (valoare negativa, egala cu 0)')
elif x == y == z:
    print('Tringhiul este echilateral')
elif (x == y or y == z or x == z):
    print('Triunghiul este isoscel')
else:
    print('Tringhiul este unul oarecare')

'''9. Citește o literă de la tastatură.
Verifică și afișează dacă este vocală sau nu'''
litera = input('Introduceti o litera: ')
if litera in ('a','e','i','o','u','ă','î','â'):
    print('Litera '+ litera + ' este o vocala')
else:
    print('Litera '+ litera + ' este o consoana')

'''10.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F'''
if x > 10:
    print('Nota prea mare, peste 10')
elif x <=10 and x > 9:
    print('A')
elif x <= 9 and x > 8:
    print('B')
elif x <= 8 and x > 7:
    print('C')
elif x <= 7 and x > 6:
    print('D')
elif x <= 6 and x > 4:
    print('E')
elif x <= 4 and x >= 0:
    print('F')
else:
    print('Nota invalida, nota negativa')

'''11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)'''
x = int(input('Introduceti un numar: '))
if len(str(abs(x))) >= 4:
    print(str(x)+ ' are minim 4 cifre')
else:
    print(str(x)+ ' nu are minim 4 cifre')

#12.Verifică dacă x are exact 6 cifre.
if len(str(abs(x))) == 6:
    print(str(x)+' are 6 cifre')
else:
    print(str(x)+' nu are 6 cifre')

#13.Verifică dacă x este număr par sau impar (x e int).
if x % 2 == 0:
    print(str(x)+' este numar par')
else:
    print(str(x)+' este numar impar')

'''14. x, y, z (int)
Afișează care este cel mai mare dintre ele?'''
y = int(input('4. Introduceti inca un numar: '))
z = int(input('4. Introduceti inca un numar: '))
if x > y and x > z:
    print(str(x)+' este cel mai mare numar')
elif y > x and y > z:
    print(str(y)+' este cel mai mare numar')
else:
    print(str(z)+' este cel mai mare numar')

'''15.
x, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.'''
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print('Tringhiul este valid')
else:
    print('Triunghiul nu este valid')

'''16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citiți de la tastatură un int x
● Afișează stringul fără ultimele x caractere
Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'''
x = int(input('6. Introduceti un numar: '))
text = 'Coral is either the stupidest animal or the smartest rock'
marime_text = len(text)
if x < 0 or x > marime_text:
    print('Numarul este negativ sau prea mare de '+str(marime_text)+' de caractere folosite in propozitie')
else:
    rezultat = text[0:marime_text-x]
    print(rezultat)

'''17.Același string. Declară un string nou care să fie format din primele 5 caractere
+ ultimele 5'''
rezultat7 = text[0:5]+text[marime_text-5:marime_text]
print(rezultat7)

'''18. Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest '''
rock = text.find('rock')
text_pana_la_rock = slice(rock)
print(text[text_pana_la_rock])

'''19. Citește de la tastatura un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat'''

variabila_string = input('9. Introduceti un string: ')
marime_string = len(variabila_string)
assert variabila_string[0].lower() == variabila_string[marime_string-1].lower()

'''20. Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)'''

string10 = '0123456789'
slice10 = slice(0,10,2)
print(string10[slice10])

'''21.
Verificare imbarcare persoane
Tineti urmatoarele DAte
Varsta
Insotit de mama
Insotit de tata
Pasaport
Act permisiune mama
Act permisiune tata

Conditii de imbarcare
DAca pers are varsta peste 18 ani si are pasaport
DAca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
DAca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte

Aici vreau sa testati codul cu toate variantele posibile
Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results

Ex:
Varsta 19 ani, NU am pasaport => NU ma pot imbarca
Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
Etc
'''

varsta = int(input('Completati varsta: '))
pasaport = input('Specificati prin DA/NU daca detineti pasaport: ')
insotit_mama = ''
insotit_tata = ''
act_permisiune_mama = ''
act_permisiune_tata = ''
if varsta < 0:
    print('Varsta invalida (negativa)')
elif varsta < 18 and pasaport.upper() == 'NU':
    print('Varsta '+str(varsta)+' ani si nu am pasaport => Nu ma pot imbarca')
elif varsta < 18 and pasaport.upper() == 'DA':
    insotit_mama = input('Specificati prin DA/NU daca sunteti insotit de mama: ')
    insotit_tata = input('Specificati prin DA/NU daca sunteti insotit de tata: ')
    if insotit_mama.upper() == 'DA' and insotit_tata.upper() == 'DA':
        print('Varsta '+str(varsta)+' ani, am pasaport, insotit de parinti => Ma pot imbarca')
    elif insotit_mama.upper() == 'DA' and insotit_tata.upper() == 'NU':
        act_permisiune_tata = input('Specificati prin DA/NU daca aveti actul ce atesta permisiunea tatalui: ')
        if act_permisiune_tata.upper() == 'DA':
                print('Varsta '+str(varsta)+' ani, am pasaport, insotit de mama si cu act de permisiune de la tata => Ma pot imbarca')
        else:
                print('Varsta ' + str(varsta) + ' ani, am pasaport, insotit de mama si fara act de permisiune de la tata => Nu ma pot imbarca')
    elif insotit_mama.upper() == 'NU' and insotit_tata.upper() == 'DA':
        act_permisiune_mama = input('Specificati prin DA/NU daca aveti actul ce atesta permisiunea mamei: ')
        if act_permisiune_mama.upper() == 'DA':
                print('Varsta '+str(varsta)+' ani, am pasaport, insotit de tata si cu act de permisiune de la mama => Ma pot imbarca')
        else:
                print('Varsta ' + str(varsta) + ' ani, am pasaport, insotit de tata si fara act de permisiune de la mama => Nu ma pot imbarca')
    else:
        print('Varsta '+str(varsta)+' ani, am pasaport, neinsotit de parinti => Nu ma pot imbarca')
elif varsta >= 18 and pasaport.upper() == 'DA':
    print('Varsta '+str(varsta)+' ani, am pasaport => Ma pot imbarca')
elif varsta >= 18 and pasaport.upper() == 'NU':
    print('Varsta '+str(varsta)+' ani, nu am pasaport => Nu ma pot imbarca')
else:
    print('NU ati completat cu DA sau NU la intrebarile de mai sus')


'''22. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll

Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y'''

dice_roll = random.randint(1,6)
print(dice_roll)
numar = int(input('Introduceti un numar intre 1 si 6: '))
if numar < 0 and numar > 7:
    print('Numarul ales nu este in intervalul 1-6')
elif dice_roll == numar and numar > 0 and numar < 7:
    print('Felicitari! Ai ales '+str(numar)+' si zarul a fost '+str(dice_roll))
elif dice_roll > numar and numar > 0 and numar < 7:
    print('Ai pierdut. Ai ales un numar mai mic. Ai ales '+str(numar)+' dar a fost '+str(dice_roll))
else:
    print('Ai pierdut. Ai ales un numar mai mare. Ai ales '+str(numar)+' dar a fost '+str(dice_roll))
