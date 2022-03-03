import requests
from bs4 import BeautifulSoup as BS
import csv
from typing import List


def hlavni(URL,nazev_souboru):
    odpoved = requests.get(URL)
    naparsovano = BS(odpoved.text, "html.parser")
    bunky = naparsovano.find_all("td")
    tabulka = []
    kody = []
    mesta = []

    adresy_kratke = []
    seznam_adres = []

    list_slovniku = []


    voliči_v_seznamu = []
    vydane_obalky = []
    platne_hlasy = []

    Občanská_demokratická_strana = []
    Řád_národa = []
    CESTA_ODPOVĚDNÉ_SPOLEČNOSTI = []
    ČSSD = []
    Radostné_Česko = []
    STAN = []
    KSČM = []
    Strana_zelených = []
    ROZUMNÍ = []
    Strana_svobodných_občanů = []
    Blok_proti_islamu = []
    ODA = []
    Piráti = []
    Referendum_o_EU = []
    TOP09 =  []
    ANO = []
    Dobrá_volba = []
    Republikáni = []
    KDU_ČSL = []
    Realisté = []
    SPORTOVCI = []
    DSSS = []
    SPD = []
    SPO = []



    for prvek in bunky:
        tabulka.append(prvek.text)

    for prvek in tabulka:
        if prvek == "X":
            tabulka.remove(prvek)

    for prvek in tabulka[:-3]:
        if prvek.isdigit():
            kody.append(prvek)
        else:
            mesta.append(prvek)



    for adresa in naparsovano.find_all("a")[5:-2]:
        adresy_kratke.append(adresa.get("href"))

    for adresa in adresy_kratke[::2]:
        seznam_adres.append("https://volby.cz/pls/ps2017nss/" + adresa)



    for adresa in seznam_adres:
        tabulka2 = []
        odpoved2 = requests.get(adresa)
        naparsovano2 = BS(odpoved2.text, "html.parser")
        bunky2 = naparsovano2.find_all("td")
        for prvek in bunky2:
            tabulka2.append(prvek.text)
        tabulka2.remove("X")
        voliči_v_seznamu.append(tabulka2[3])
        vydane_obalky.append(tabulka2[4])
        platne_hlasy.append(tabulka2[7])
        Občanská_demokratická_strana.append(tabulka2[12])
        Řád_národa.append(tabulka2[16])
        CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
        ČSSD.append(tabulka2[26])
        Radostné_Česko.append(tabulka2[31])
        STAN.append(tabulka2[36])
        KSČM.append(tabulka2[41])
        Strana_zelených.append(tabulka2[46])
        ROZUMNÍ.append(tabulka2[51])
        Strana_svobodných_občanů.append(tabulka2[56])
        Blok_proti_islamu.append(tabulka2[61])
        ODA.append(tabulka2[66])
        Piráti.append(tabulka2[71])
        Referendum_o_EU.append(tabulka2[76])
        TOP09.append(tabulka2[81])
        ANO.append(tabulka2[86])
        Dobrá_volba.append(tabulka2[91])
        Republikáni.append(tabulka2[96])
        KDU_ČSL.append(tabulka2[101])
        Realisté.append(tabulka2[106])
        SPORTOVCI.append(tabulka2[111])
        DSSS.append(tabulka2[116])
        SPD.append(tabulka2[121])
        SPO .append(tabulka2[126])






    for číslo in range(len(kody)):
        slovník = {"kod" : kody[číslo], "mesto" : mesta[číslo], "volici v seznamu" : voliči_v_seznamu[číslo],
                   "vydane obalky" : vydane_obalky[číslo], "platne hlasy" : platne_hlasy[číslo], 'Občanská demokratická strana': Občanská_demokratická_strana[číslo],
                   'Řád národa - Vlastenecká unie' : Řád_národa[číslo], 'CESTA ODPOVĚDNÉ SPOLEČNOSTI' : CESTA_ODPOVĚDNÉ_SPOLEČNOSTI[číslo],
                   "Česká str.sociálně demokrat." : ČSSD[číslo], 'Radostné Česko' : Radostné_Česko[číslo], 'STAROSTOVÉ A NEZÁVISLÍ' : STAN[číslo],
                   'Komunistická str.Čech a Moravy' : KSČM[číslo], 'Strana zelených' : Strana_zelených[číslo], "ROZUMNÍ-stop migraci,diktát.EU" : ROZUMNÍ[číslo],
                   'Strana svobodných občanů': Strana_svobodných_občanů[číslo], 'Blok proti islam.-Obran.domova' : Blok_proti_islamu[číslo],
                   'Občanská demokratická aliance': ODA[číslo], 'Česká pirátská strana': Piráti[číslo], 'Referendum o Evropské unii' :  Referendum_o_EU[číslo],
                   'TOP 09' : TOP09[číslo], 'ANO 2011' : ANO[číslo], 'Dobrá volba 2016' : Dobrá_volba[číslo], 'SPR-Republ.str.Čsl. M.Sládka' : Republikáni[číslo],
                   'Křesť.demokr.unie-Čs.str.lid.' : KDU_ČSL[číslo], 'REALISTÉ' : Realisté[číslo], 'SPORTOVCI' : SPORTOVCI[číslo],
                   'Dělnic.str.sociální spravedl.': DSSS[číslo], 'Svob.a př.dem.-T.Okamura (SPD)' : SPD[číslo], 'Strana Práv Občanů' : SPO[číslo]  }
        list_slovniku.append(slovník)






    with open(f"{nazev_souboru}.csv", "a", newline="") as csv_soubor:
        zahlavi = ["KOD", "MESTO", "VOLICI V SEZNAMU", "VYDANE OBALKY","PLATNE HLASY", 'Občanská demokratická strana v %', 'Řád národa - Vlastenecká unie v %',
                   'CESTA ODPOVĚDNÉ SPOLEČNOSTI v %', "Česká str.sociálně demokratická v %", 'Radostné Česko v %', 'STAROSTOVÉ A NEZÁVISLÍ v %',
                   'Komunistická str.Čech a Moravy v %','Strana zelených v %', "ROZUMNÍ-stop migraci,diktát.EU v %", 'Strana svobodných občanů v %',
                   'Blok proti islam.-Obran.domova v %','Občanská demokratická aliance v %','Česká pirátská strana v %', 'Referendum o Evropské unii v %',
                   'TOP 09 v %', 'ANO 2011 v %', 'Dobrá volba 2016 v %', 'SPR-Republ.str.Čsl. M.Sládka v %', 'Křesť.demokr.unie-Čs.str.lid. v %', 'REALISTÉ v %', 'SPORTOVCI v %',
                   'Dělnic.str.sociální spravedl. v %','Svob.a př.dem.-T.Okamura (SPD) v %', 'Strana Práv Občanů v %' ]
        writer = csv.DictWriter(csv_soubor, fieldnames=zahlavi)
        writer.writeheader()
        for index, _ in enumerate(list_slovniku):
            writer.writerow(
                {
                    "KOD": list_slovniku[index]["kod"],
                    "MESTO": list_slovniku[index]["mesto"],
                    "VOLICI V SEZNAMU" : list_slovniku[index]["volici v seznamu"],
                    "VYDANE OBALKY" : list_slovniku[index]["vydane obalky"],
                    "PLATNE HLASY" : list_slovniku[index]["platne hlasy"],
                    'Občanská demokratická strana v %' : list_slovniku[index]["Občanská demokratická strana"],
                    'Řád národa - Vlastenecká unie v %' : list_slovniku[index]["Řád národa - Vlastenecká unie"],
                    'CESTA ODPOVĚDNÉ SPOLEČNOSTI v %' : list_slovniku[index]["CESTA ODPOVĚDNÉ SPOLEČNOSTI"],
                    "Česká str.sociálně demokratická v %" : list_slovniku[index]["Česká str.sociálně demokrat."],
                    'Radostné Česko v %' : list_slovniku[index]["Radostné Česko"],
                    'STAROSTOVÉ A NEZÁVISLÍ v %' : list_slovniku[index]["STAROSTOVÉ A NEZÁVISLÍ"],
                    'Komunistická str.Čech a Moravy v %' : list_slovniku[index]["Komunistická str.Čech a Moravy"],
                    'Strana zelených v %' : list_slovniku[index]["Strana zelených"],
                    "ROZUMNÍ-stop migraci,diktát.EU v %" :  list_slovniku[index]["ROZUMNÍ-stop migraci,diktát.EU"],
                    'Strana svobodných občanů v %' : list_slovniku[index]["Strana svobodných občanů"],
                    'Blok proti islam.-Obran.domova v %' : list_slovniku[index]["Blok proti islam.-Obran.domova"],
                    'Občanská demokratická aliance v %': list_slovniku[index]["Občanská demokratická aliance"],
                    'Česká pirátská strana v %' : list_slovniku[index]["Česká pirátská strana"],
                    'Referendum o Evropské unii v %' : list_slovniku[index]["Referendum o Evropské unii"],
                    'TOP 09 v %' :  list_slovniku[index]["TOP 09"],
                    'ANO 2011 v %' :  list_slovniku[index]["ANO 2011"],
                    'Dobrá volba 2016 v %' :  list_slovniku[index]["Dobrá volba 2016"],
                    'SPR-Republ.str.Čsl. M.Sládka v %' : list_slovniku[index]["SPR-Republ.str.Čsl. M.Sládka"],
                    'Křesť.demokr.unie-Čs.str.lid. v %' :  list_slovniku[index]["Křesť.demokr.unie-Čs.str.lid."],
                    'REALISTÉ v %' : list_slovniku[index]["REALISTÉ"],
                    'SPORTOVCI v %' : list_slovniku[index]["SPORTOVCI"],
                    'Dělnic.str.sociální spravedl. v %' : list_slovniku[index]["Dělnic.str.sociální spravedl."],
                    'Svob.a př.dem.-T.Okamura (SPD) v %' : list_slovniku[index]["Svob.a př.dem.-T.Okamura (SPD)"],
                    'Strana Práv Občanů v %' :  list_slovniku[index]["Strana Práv Občanů"]




                })



hlavni("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204", "Okres_Zlín")








