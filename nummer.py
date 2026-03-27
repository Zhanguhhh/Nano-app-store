import random

def genereer_getal(moeilijkheid):
    if moeilijkheid == 1:
        return random.randint(1, 10)
    elif moeilijkheid == 2:
        return random.randint(1, 50)
    elif moeilijkheid == 3:
        return random.randint(1, 100)
    return None

def max_pogingen(moeilijkheid):
    if moeilijkheid == 1:
        return 5
    elif moeilijkheid == 2:
        return 7
    elif moeilijkheid == 3:
        return 10
    return None

def score(moeilijkheid, aantal_pogingen):
    return (max_pogingen(moeilijkheid) - aantal_pogingen) * moeilijkheid

def advies_moeilijkheidsgraad(score):
    if score < 5:
        return "probeer een lagere moeilijkheidsgraad"
    elif 5 <= score <= 12:
        return "houd deze moeilijkheidsgraad aan"
    else:
        return "je kunt een hogere moeilijkheidsgraad aan"

def raad_het_nummer():
    print("--- Raad het nummer ---")

    naam = input("Wat is je naam: ").strip()
    if naam == "":
        print("Bye!")
        return

    print("Kies een moeilijkheidsgraad:")
    print("1 = makkelijk (1-10, 5 pogingen)")
    print("2 = normaal   (1-50, 7 pogingen)")
    print("3 = moeilijk  (1-100, 10 pogingen)")

    while True:
        keuze = input("Jouw keuze: ").strip()
        if keuze == "":
            print("Bye!")
            return
        try:
            moeilijkheid = int(keuze)
            if moeilijkheid in (1, 2, 3):
                break
            else:
                print("Ongeldige keuze. Kies 1, 2 of 3.")
        except ValueError:
            print("Ongeldige invoer. Voer een getal in (1, 2 of 3).")

    getal = genereer_getal(moeilijkheid)
    max_pog = max_pogingen(moeilijkheid)
    gevonden = False
    aantal_pogingen = 0

    poging = 1
    while poging <= max_pog and not gevonden:
        rest = max_pog - poging + 1
        huidige_score = rest * moeilijkheid

        print(f"Je hebt nog {rest} pogingen.")
        print(f"Je huidige score is: {huidige_score}")

        gok_input = input("Doe een gok (of enter om te stoppen): ").strip()
        if gok_input == "":
            print("Bye!")
            return

        try:
            gok = int(gok_input)
        except ValueError:
            print("Ongeldige invoer. Voer een geheel getal in.")
            continue

        aantal_pogingen = poging
        if gok == getal:
            print("Gevonden!")
            gevonden = True
            break
        elif abs(gok - getal) <= 2:
            print("Dichtbij!")
        elif gok < getal:
            print("Hoger!")
        else:
            print("Lager!")

        poging += 1

    eindscore = score(moeilijkheid, aantal_pogingen)
    if gevonden:
        print(f"Je score deze sessie: {eindscore}")
    else:
        print(f"Jammer, je hebt het niet kunnen raden, het juiste getal was {getal}")
        print(f"Je score deze sessie: {eindscore}")

    print(f"Advies: {advies_moeilijkheidsgraad(eindscore)}")
    print("Bye!")
