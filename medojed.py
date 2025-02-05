import os
import time
import json
import requests


def medojed(vypis=True):

    def kelisova(odkaz):

        r = requests.get(odkaz)
        je = None
        for kseft, dalsi_udaje in ksefty.items():
            if kseft in odkaz.split("/")[2]:
                je = dalsi_udaje["je"]
                neni = dalsi_udaje["neni"]
        if not je:
            print("Tento web neznám, přeskakuji.")
            return None
        if je in r.text:
            return True
        elif neni in r.text:
            return False
        else:
            return None

    try:
        with open(os.path.join("config", "odkazy.json"), "r") as f:
            seznam = json.loads(f.read())
        with open(os.path.join("ksefty.json"), "r") as f:
            ksefty = json.loads(f.read())
    except Exception as e:
        print(
            "Chybí některý z konfiguračních souborů. Viz následující chybové hlášení a soubor README.md."
        )
        print(e)
        quit()

    vysledky = {}
    pocitadlo = 0

    seznam = list(set(seznam))

    for odkaz in seznam:
        try:
            dostupnost = kelisova(odkaz)
            vysledky[odkaz] = dostupnost
            if vypis:
                pocitadlo += 1
                print(f"{pocitadlo}/{len(seznam)}: {odkaz} {dostupnost}")
        except Exception as e:
            print(e)

    os.makedirs("data", exist_ok=True)

    with open(
        os.path.join("data", f"{int(time.time())}.json"), "w+", encoding="utf-8"
    ) as f:
        f.write(json.dumps(vysledky))


if __name__ == "__main__":
    medojed()
