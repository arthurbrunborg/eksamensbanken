'''
Skriv funksjonen les_meteoritter(filnavn)


Funksjonen tar inn et filnavn, og returnerer en
todimensjonal liste med delvis tolkede verdier
basert på linjene i filen.



csv-filen er på UTF-8-format, separatoren er komma, ',' og starter slik:
name,id,class,mass,year,latitude,longitude
Aachen,1,L5,21.0,1880,50.775,6.08333
Aarhus,2,H6,720.0,1951,56.18333,10.23333
Abee,6,EH4,107000.0,1952,54.21667,-113.0
Acapulco,10,Acapulcoite,1914.0,1976,16.88333,-99.9
...

Vi har noen krav til tolkningen:

Massen skal tolkes som en flyttall.
Det finnes nedslag der masse ikke er registrert. Her skal massen
settes til 0.
Nedslagsår skal tolkes som heltall.
Problemet er at enkelte meteorittyper også har komma ibetegnelsen, som på følgende linje:
Akyumak,433,"Iron, IVA",50000.0,1981,39.91667,42.81667
Alle disse spesialtilfellene er jernmeteoritter. Vi løser
dette ved å erstatte alle disse variantene (Iron Iva" med strengen 'Iron'.
'''
def les_meteoritter(filnavn):
    ut = []
    with open(filnavn,'r', encoding="utf8") as f:
        f.readline()
        for nedslag in f.readlines():
            splitt = nedslag.split(",")
            splitt[-1] = splitt[-1].strip()
            if len(splitt) == 8:
                splitt[2:4] = ["Iron"]
            if splitt[3]:
                splitt[3] = float(splitt[3])
            else:
                splitt[3] = 0
            splitt[4] = int(splitt[4])
            ut.append(splitt)
    return ut

# def les_meteoritter(filnavn):
#     with open(filnavn, 'r') as f:
#         return [[splitt[-1].strip(),"Iron" if len(splitt) == 8 else splitt[2:4],float(splitt[3]) if splitt[3] else 0,int(splitt[4]),] for nedslag in f.readlines() for splitt in nedslag.split(",")]
    
'''
Skriv metoden sorter_masse(nedslag, kolonne)
- nedslag er den todimensjonale listen som kommer fra funksjonen les_meteoritter.
- kolonne er et heltall som indikerer kolonnen i hvert nedslag som skal fungere som nøkkel.
Funksjonen skal returnere en dictionary der de ulike nedslagenes verdi
i den gitte kolonnen skal brukes som nøkkel. Bak denne nøkkelen skal så
alle massene for disse 'like' nedslagene summeres.
Eksempel:
> m = les_meteoritter("meteoritter.csv")
> d = sorter_masse(m,2) # sorter på type (kolonne 2)
> print(d)
{'L5': 16500.0, 'H6': 20000.0, '...

'''
def sorter_masse(nedslag, kolonne):
    hvor = ['name','id','class','mass','year','latitude','longitude'].index(kolonne)
    d = {}
    for n in nedslag:
        d[n[hvor]] = d.get(hvor,0) + n[3]
    return d

def sorter_masse2(nedslag, kolonne):
    hvor = {
        'name': 0,
        'id': 1,
        'class': 2,
        'mass': 3,
        'year': 4,
        'latitude': 5,
        'longitude': 6
    }
    hvor_index = hvor.get(kolonne, -1)
    d = {}
    for n in nedslag:
        d[n[hvor_index]] = d.get(hvor_index,0) + n[3]
    return d
'''
Skriv funksjonene lagre_sorterte_nedslag(sortert) og hent_sorterte_nedslag(sortert).
Disse skal henholdsvis lagre og hente inn samlingen sortert (en dictionary) til/fra en fil.
Du velger selv hvordan du gjør det, og hva filen skal hete.
'''
import pickle
def lagre_sorterte_nedslag(sortert):
    with open("sortert.pickle",'wb') as f:
        pickle.dump(sortert,f)
        
def hent_sorterte_nedslag():
    with open("sortert.pickle",'rb') as f:
        return pickle.load(f)
        
        


'''
Skriv ut hvilket år det ble registrert størst total nedslagsmasse.
Hvis flere år har samme høyeste masse registrert kan du skrive ut alle.
Du trenger ikke skrive denne koden som en funksjon, men det
er lurt å bruke funksjonene som er spesifisert over. Du
kan forvente at de fungerer slik som spesifisert, selv om
du ikke har klart å løse dem.
Filen har navn 'meteoritter.csv'
'''
n = les_meteoritter('meteoritter.csv')
d = sorter_masse2(n,'year')
maks = max(d.values())
for k, v in d.items():
    if v == maks:
        print(k)
        
lagre_sorterte_nedslag(d)
d = hent_sorterte_nedslag()

