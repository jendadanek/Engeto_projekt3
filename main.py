import requests
from bs4 import BeautifulSoup as BS
import csv
from typing import List

URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204"
def hlavni() -> None:
    odpoved = ziskej_odpoved()
    naparsovano = vytahni_udaje(odpoved)
    tabulka = hledej_tabulku(naparsovano)
    radky = hledej_radky(tabulka)

    konecne_udaje = (tabulka_info(row) for row in radky)
    uloz_csv(list(konecne_udaje))

def ziskej_odpoved():
    return requests.get(URL)


def vytahni_udaje(odpoved):
    return BS(odpoved.text, "html.parser")

def hledej_tabulku(naparsovano):
    return naparsovano.find_all("table")

def hledej_radky(tabulka) -> list:
    return tabulka.find_all("tr")[2:]

def tabulka_info(tr) -> dict:
    try:
        kod = tr.find_all("td")[0].text
        mesto = tr.find_all("td")[1].text
        return {"kod": kod, "mesto": mesto}

    except AttributeError:
        print("Indexy u jednotlivych bunek v radku nejsou v poradku")

def uloz_csv(data: List[dict]):
    with open("mesta.csv", "a", newline="") as csv_soubor:
        zahlavi = ["KOD", "MESTO"]
        writer = csv.DictWriter(csv_soubor, fieldnames=zahlavi)
        writer.writeheader()

        for index, _ in enumerate(data):
            writer.writerow(
                {
                    "KOD": data[index]["kod"],
                    "MESTO": data[index]["mesto"],

                }
            )

hlavni()




