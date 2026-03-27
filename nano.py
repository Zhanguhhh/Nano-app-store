
import nummer
import weer_api
import galgje

def main():
    while True:
        print("Nano App Store")
        print("1. Raad het nummer")
        print("2. Galgje")
        print("3. Weerbericht")
        print("4. Stoppen")

        keuze = input("Kies een optie: ").strip()
        if keuze == "":
            continue
        if keuze == "1":
            nummer.raad_het_nummer()
        elif keuze == "2":
            galgje.menu()
        elif keuze == "3":
            weer_api.toon_weer()
        elif keuze == "4":
            print("Tot de volgende keer!")
            break
        else:
            print("Ongeldige keuze. Kies 1 t/m 4.")

if __name__ == "__main__":
    main()