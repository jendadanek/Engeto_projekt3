import requests
from bs4 import BeautifulSoup as BS
import csv
from typing import List

URL = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204"
def hlavni() -> None:
    odpoved = ziskej_odpoved()
    naparsovano = vytahni_udaje(odpoved)
    tabulka = hledej_tabulku(naparsovano)
    konecne_udaje = (hledej_tabulku(naparsovano) for row in tabulka)
    uloz_csv(list(konecne_udaje))

    adresy_kratke = []
    ziskej_adresy(naparsovano, adresy_kratke)
    seznam_adres = []
    získej_odkazy(adresy_kratke, seznam_adres)
    print(seznam_adres)

def ziskej_odpoved():
    return requests.get(URL)


def vytahni_udaje(odpoved):
    return BS(odpoved.text, "html.parser")

def hledej_tabulku(naparsovano):
    for table in naparsovano.find_all("table"):
        for tr in table.find_all("tr"):
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
def ziskej_adresy(naparsovano, adresy_kratke):
    for adresa in naparsovano.find_all("a")[5:-2]:
        adresy_kratke.append(adresa.get("href"))


def získej_odkazy(adresy_kratke,seznam_adres):
    for adresa in adresy_kratke:
        seznam_adres.append("https://volby.cz/pls/ps2017nss/" + adresa)


hlavni()




