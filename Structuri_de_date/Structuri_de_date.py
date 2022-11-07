'''1. Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face

suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.'''

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)

note_muzicale = note_muzicale[::-1]
print(note_muzicale)

note_muzicale.reverse()
print(note_muzicale)

#2. De câte ori apare ‘do’?

print('Ex.2. Nota do apare de '+ str(note_muzicale.count('do')) + ' ori')

'''3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.'''

l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
lista = l1+l2
l1.extend(l2)
print(l1)
print(lista)

'''4.
● Sortează și afișază lista generată la exercițiul anterior.
● Stergeti numărul 0 folosind o funcție.
● Afișeaza iar lista.'''
lista.sort()
lista.remove(0)
print(lista)

'''5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.'''

if len(lista) == 0:
    print('5. Lista este goala')
else:
    print('5. Lista nu este goala')

#6. Folosește o funcție care să șteargă lista de la exercițiul 3.

lista.clear()

'''7. Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.'''

if len(lista) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

'''8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)'''

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

'''9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie'''

print('Ana a luat nota ' + str(dict1.get('Ana')))
print('Gigel a luat nota ' + str(dict1.get('Gigel')))
print('Dorel a luat nota ' + str(dict1.get('Dorel')))

'''10. Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare'''
dict1['Dorel'] = 6
print('10. Dorel a făcut contestație și a primit ' + str(dict1.get('Dorel')))

'''11. Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi'''

dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

'''12.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zile_sapt ‘luni’
● Afișeaza zile_sapt'''

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

zile_sapt.add('luni')
print(zile_sapt)

'''13.Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămânii.
● Weekend nu este un subset al zilelor din săptămânii.'''


if set(weekend).issubset(set(zile_sapt)):
    print('12. Weekend este un subset al zilelor din săptămânii.')
else:
    print('13. Weekend nu este un subset al zilelor din săptămânii.')

#14. Afișează diferențele dintre aceste 2 seturi.

print(zile_sapt.difference(weekend))

#15. Afișază intersecția elementelor din aceste 2 seturi.

print(zile_sapt.intersection(weekend))

'''1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea

- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori

Google search hint
“how to check if item îs în list python”'''

echipa = ['Sergiu', 'Ovidiu', 'Catalin', 'Bogdan', 'Nicu']
schimbari_efectuate = int(input('Schimbari efectuate: '))
schimbari_max = 3
jucator_schimbat = 'Ovidiu'
jucator_nou = 'Tibi'
if schimbari_efectuate < 0 or schimbari_efectuate > schimbari_max:
    print('Numar schimbari efectuate invalid (negativ sau prea mare)')
elif schimbari_efectuate < schimbari_max:
    if jucator_schimbat in echipa and schimbari_efectuate < schimbari_max:
        echipa.remove(jucator_schimbat)
        echipa.append(jucator_nou)
        schimbari_efectuate = schimbari_efectuate + 1
        print('A intrat ' + jucator_nou + ', a iesit ' + jucator_schimbat + ', mai ai ' + str(schimbari_max-schimbari_efectuate) + ' schimbari')
    else:
        print('Nu se poate efectua schimbarea deoarece jucatorul ' + jucator_schimbat + ' nu e in teren')
else:
    print('Nu mai sunt schimbari disponibile')