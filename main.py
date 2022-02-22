import requests
from bs4 import BeautifulSoup as BS
import csv
from typing import List


def hlavni(URL,nazev_souboru):
    odpoved = ziskej_odpoved(URL)
    naparsovano = vytahni_udaje(odpoved)


    konecne_udaje = (tabulka_info(row) for row in odpoved)
    uloz_csv(list(konecne_udaje), nazev_souboru)

    adresy_kratke = []
    ziskej_adresy(naparsovano, adresy_kratke)
    seznam_adres = []
    získej_odkazy(adresy_kratke, seznam_adres)

def ziskej_odpoved(URL):
    return requests.get(URL)

def vytahni_udaje(odpoved):
    return BS(odpoved.text, "html.parser")


def tabulka_info(tr) -> dict:
    try:
        kod = tr.find_all("td", {"class": "cislo"}).text
        mesto = tr.find_all("td", {"class": "overflow_name"}).text
        return {"kod": kod, "mesto": mesto}

    except AttributeError:
        print("Indexy u jednotlivych bunek v radku nejsou v poradku")

def uloz_csv(data: List[dict],nazev_souboru):
    with open(nazev_souboru + ".csv", "a", newline="") as csv_soubor:
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



hlavni("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204", "Okres_Zlín")




