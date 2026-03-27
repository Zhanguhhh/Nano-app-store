import random

def lees_woorden(bestandsnaam):
    woorden_dict = {}
    with open(bestandsnaam, "r") as bestand:
        for regel in bestand:
            woord = regel.strip()
            if woord:
                woorden_dict[woord] = bepaal_moeilijkheid(woord)
    return woorden_dict

def bepaal_moeilijkheid(woord):
    lengte = len(woord)
    if lengte <= 6:
        return 1
    elif lengte <= 11:
        return 2
    else:
        return 3

def sla_woorden_op(bestandsnaam, woorden_dict):
    with open(bestandsnaam, "w") as bestand:
        for woord in woorden_dict.keys():
            bestand.write(woord + "\n")

def bereken_score(aantal_levens_over, moeilijkheid):
    return aantal_levens_over * moeilijkheid

def voeg_score_toe(naam, woord, score):
    with open("score.txt", "a") as bestand:
        bestand.write(f"{naam},{woord},{score}\n")

def toon_tussenstand(woord, geraden_letters):
    weergave = []
    for letter in woord:
        if letter in geraden_letters:
            weergave.append(letter.upper())
        else:
            weergave.append("_")
    return " ".join(weergave)

def kies_woord(woorden_dict, moeilijkheidsgraad):
    mogelijke_woorden = [w for w, m in woorden_dict.items() if m == moeilijkheidsgraad]
    if not mogelijke_woorden:
        return None
    return random.choice(mogelijke_woorden)

def speel_sessie(woorden_dict):
    print("--- Nieuwe sessie ---")
    naam = input("Je naam: ").strip()
    if naam == "":
        print("Sessie afgebroken.")
        return

    while True:
        try:
            moeilijkheid = int(input("Kies een moeilijkheid (1=makkelijk, 2=normaal, 3=moeilijk): ").strip())
            if moeilijkheid in (1, 2, 3):
                break
            else:
                print("Ongeldige keuze. Kies 1, 2 of 3.")
        except ValueError:
            print("Ongeldige invoer. Voer een getal in.")

    woord = kies_woord(woorden_dict, moeilijkheid)
    if woord is None:
        print(f"Geen woorden beschikbaar voor moeilijkheidsgraad {moeilijkheid}.")
        return

    if moeilijkheid == 1:
        levens = 10
    elif moeilijkheid == 2:
        levens = 8
    else:
        levens = 6

    geraden_letters = set()
    foute_letters = set()
    woord_letters = set(woord.lower())

    while levens > 0:
        print("\n" + toon_tussenstand(woord, geraden_letters))
        if foute_letters:
            print(f"Fout geraden: {', '.join(sorted(foute_letters))}")
        print(f"Levens over: {levens}")

        invoer = input("Raad een letter (Enter om te stoppen): ").strip().lower()
        if invoer == "":
            print("Sessie afgebroken.")
            return

        if len(invoer) != 1 or not invoer.isalpha():
            print("Voer één letter in a.u.b.")
            continue

        if invoer in geraden_letters or invoer in foute_letters:
            print("Die letter heb je al geraden.")
            continue

        if invoer in woord_letters:
            geraden_letters.add(invoer)
            print("Goed!")
            if woord_letters.issubset(geraden_letters):
                print("\n" + toon_tussenstand(woord, geraden_letters))
                print(f"Gefeliciteerd! Je hebt het woord '{woord.upper()}' geraden!")
                break
        else:
            foute_letters.add(invoer)
            levens -= 1
            print("Mis!")
            if levens == 0:
                print(f"Je hebt verloren. Het woord was '{woord.upper()}'.")

    if levens > 0:
        score = bereken_score(levens, moeilijkheid)
    else:
        score = 0
    voeg_score_toe(naam, woord, score)

    print("--- Sessie resultaat ---")
    print(f"Woord: {woord.upper()} | Resultaat: {'WIN' if levens > 0 else 'VERLOREN'}")
    print(f"Levens over: {levens}")
    print(f"Score: {score}")

def verwijder_woord(woorden_dict):
    if not woorden_dict:
        print("Er zijn nog geen woorden in de lijst.")
        return
    print("--- Woord verwijderen ---")
    woord = input("Voer het woord in dat je wilt verwijderen: ").strip().lower()
    if woord in woorden_dict:
        del woorden_dict[woord]
        sla_woorden_op("woordenlijst.txt", woorden_dict)
        print(f"'{woord}' is verwijderd.")
    else:
        print(f"'{woord}' staat niet in de woordenlijst.")

def voeg_woord_toe(woorden_dict):
    print("--- Woord toevoegen ---")
    woord = input("Voer het nieuwe woord in: ").strip().lower()
    if not woord:
        print("Geen geldig woord ingevoerd.")
        return
    if woord in woorden_dict:
        print(f"'{woord}' staat al in de woordenlijst.")
        return
    if not woord.isalpha():
        print("Alleen letters zijn toegestaan.")
        return
    woorden_dict[woord] = bepaal_moeilijkheid(woord)
    sla_woorden_op("woordenlijst.txt", woorden_dict)
    print(f"'{woord}' is toegevoegd.")

def toon_aantal_woorden(woorden_dict):
    totaal = len(woorden_dict)
    print(f"Aantal woorden in woordenbestand: {totaal}")

def menu():
    woorden_dict = lees_woorden("woordenlijst.txt")
    while True:
        print("=== Galgje Controller ===")
        print("Kies een optie:")
        print("1. Speel galgje")
        print("2. Verwijder een woord uit de woordenlijst")
        print("3. Voeg woord toe aan de woordenlijst")
        print("4. Toon aantal woorden in de woordenlijst")
        print("5. Stoppen")

        keuze = input(">> ").strip()
        if keuze == "":
            continue

        if keuze == "1":
            speel_sessie(woorden_dict)
        elif keuze == "2":
            verwijder_woord(woorden_dict)
        elif keuze == "3":
            voeg_woord_toe(woorden_dict)
        elif keuze == "4":
            toon_aantal_woorden(woorden_dict)
        elif keuze == "5":
            print("Tot de volgende keer! bye")
            break
        else:
            print("Ongeldige keuze. Kies 1 t/m 5.")
