things = {
    'toalettsaker' : ['tannbørste', 'tannkrem'],
    'ytterklær': ['jakke',"bukse"],
    'isolasjon' : ['stillongs', 'ulltrøye'],
    'mat': ['brød', 'melk', 'ost'],
    'verktøy': ['hammer', 'skrutrekker', 'tannbørste']
}

packed = [['Børge', 'tannbørste', 'ost', 'bukse'],
           ['Anna', 'tannkrem', 'brød', 'jakke'],
           ['Ole', 'stillongs', 'melk', 'hammer'],
           ['Emma', 'skrutrekker', 'tang', 'jakke']]

# Husk å skrive inn at hvis du ikke har løst, så kan du bruke som om...

''' Hvem er med på tur! 
    Returner en liste over alle som skal være med på turen '''
def participants(packed:list) -> list:
    out = []
    for person in packed:
        out.append(person[0])
    return out


''' Hva har én person pakket: '''
def has_brought(name:str, packed:list) -> list:
    for person in packed:
        if person[0] == name:
            return person[1:]
    return []


print("Børge:", has_brought("Børge", packed))
print("Ole:", has_brought("Ole", packed))
print("Skybert:", has_brought("Skybert", packed))


'''Alle unike ting man trenger: Noe kan være flere typer, som en tannbørste
   som er både et verktøy og en toalettsak. '''
def all_items(thingies: dict) -> list:
    out = []
    for hva in thingies.values():
        out += hva
    return list(set(out))

print("Alle unike ting: "+", ".join(all_items(things)))



''' Returnere om en ting er på listen over mulige ting eller ikke'''
def item_allowed(item:str, thingies:dict) -> bool:
    return item in all_items(thingies)


''' Person pakker ting. Skal ikke endre den listen som kommer inn! 
    - Man får ikke lov til å pakke ting som ikke er definert som ting (i spec)
      Hvis timen ikke er blant tillatte ting skal den ikke legges til.
      spec er ikke med som parameter, hmm... Du kan forutsette at funksjonen ser den!
    - Hvis tingen finnes i listen fra før skal den legges til én gang til,
      det er jo lov til å pakke to bukser...
    - Det er ikke viktig at personene kommer i den nye listen kommer i samme
      rekkefølge som listen en får inn i funksjonen.
    - Alle andre personers pakkeliste skal være uendret.
'''
def pack_item(name: str, item:str, packed:list) -> list:
    if item not in all_items(things): return []+packed
    out = []
    for person in packed:
        if person[0] != name:
            out.append(person)
        else:
            new_person = [name]
            new_person += has_brought(name, packed)
            new_person.append(item)
            out.append(new_person)
            print(new_person)
    return out

packed2 = pack_item("Børge", "bukse", packed)

# print("Packed:",packed,"\n", "packed2",packed2)
# print("Børge har pakket:",has_brought("Børge", packed2))
assert has_brought("Børge", packed).count('bukse') == 1, "packed er endret. Fy!"
assert has_brought("Børge", packed2).count('bukse') == 2, "Ikke pakket ekstra par bukser."

''' Hva mangler for å kunne dra på tur...
    - Vi definerer at vi er klare for å dra på tur hvis minst én person har pakket
    minst én av hver ting.
    - Returner en liste med de tingene som mangler for at vi er klare for å dra på tur. 
    '''
def what_is_missing(thingies: dict, packed: list) -> list:
    items = all_items(thingies)
    persons = participants(packed)
    for name in persons:
        for person_packed_item in has_brought(name, packed):
            if person_packed_item in items:
                items.remove(person_packed_item)
    return items

print("Mangler:",what_is_missing(things, packed))

''' Legg til mange ting på én gang 
    - Tolk innholdet i filen "pakkeliste.txt".
    - All informasjon som skal tolkes befinner seg på linje to i filen.
    - Linjen har format navn1:ting1,ting2,navn2:ting1,navn3:ting1
    - Det kan ha sneket seg inn ting som ikke er lov til å ha med på listen. Disse skal ikke lagres.
    - Returner den oppdaterte listen packed.
'''

# Endre til les fra fil...
# def add_all(already_packed:list) -> list:
    # Her kan en spare en god del hvis en kommer på at man ikke får til å legge
    # inn ting som ikke er tillatt. Dermed slipper en å surre med masse spesialsjekker
    # for om en har med navn å gjøre.
    # Du kan forvente at ingen heter noe som skal være med av ting.
def add_all(already_packed:list) -> list:
    with open("pakkeliste.txt", encoding="utf-8") as f:
        string = f.readlines()[1]
        person_split = string.split(":")
        for i in range(len(person_split) - 1):
            name = person_split[i].split(",")[-1]
            stuff = person_split[i+1].split(",")
            for item in stuff:
                already_packed = pack_item(name, item, already_packed) 
    return already_packed

    print("Etter å ha lest filen og lagt til:", add_all(packed))
            

print("Etter å ha lest filen og lagt til:",add_all(packed))