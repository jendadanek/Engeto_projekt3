import requests
from bs4 import BeautifulSoup as BS
import csv

def hlavni(URL,nazev_souboru):
    Zlínský = []
    for císlo in range(1, 5):
        Zlínský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=720" + str(císlo))

    Moravskoslezký = []
    for císlo in range(1, 7):
        Moravskoslezký.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=810" + str(císlo))

    Olomoucký = []
    for císlo in range(1, 6):
        Olomoucký.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=710" + str(císlo))

    Jihomoravský = []
    for císlo in range(1, 8):
        Jihomoravský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=620" + str(císlo))

    Vysočina = []
    for císlo in range(1, 6):
        Vysočina.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=610" + str(císlo))

    Pardubický = []
    for císlo in range(1, 5):
        Pardubický.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=530" + str(císlo))

    Kralovehradecký = []
    for císlo in range(1, 6):
        Kralovehradecký.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=520" + str(císlo))

    Liberecký = []
    for císlo in range(1, 5):
        Liberecký.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=510" + str(císlo))

    Ústecký = []
    for císlo in range(1, 8):
        Ústecký.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=420" + str(císlo))

    Karlovarský = []
    for císlo in range(1, 4):
        Karlovarský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=410" + str(císlo))

    Plzenský = []
    for císlo in range(1,8):
        Plzenský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=320" + str(císlo))

    Jihočeský = []
    for císlo in range(1, 8):
        Jihočeský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=310" + str(císlo))

    Středočeský = []
    for císlo in range(1, 10):
        Středočeský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=210" + str(císlo))

    for císlo in range(0,3):
        Středočeský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=211" + str(císlo))

    Praha = ["https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100"]

    kraje = [Zlínský,Moravskoslezký,Olomoucký,Jihomoravský,Vysočina,Pardubický,Kralovehradecký,Liberecký,Ústecký,Karlovarský,Plzenský,Jihočeský,Středočeský,Praha]
    Mozne_adresy = []
    for kraj in kraje:
        for l in kraj:
            Mozne_adresy.append(l)

    if URL not in Mozne_adresy:
        print("Neplatná adresa. Ukončuji program")
        exit()

    odpoved = requests.get(URL)
    naparsovano = BS(odpoved.text, "html.parser")
    bunky = naparsovano.find_all("td")
    tabulka = []
    kody = []
    mesta = []
    ziskej_kody_a_mesta(bunky,tabulka, kody, mesta)

    adresy_kratke = []
    seznam_adres = []

    volici_v_seznamu = []
    vydane_obalky = []
    platne_hlasy = []

    Občanská_demokratická_strana = []
    Řád_národa = []
    CESTA_ODPOVĚDNÉ_SPOLEČNOSTI = []
    ČSSD = []
    Radostné_Česko = []
    Cibulka = []
    STAN = []
    KSČM = []
    Strana_zelených = []
    ROZUMNÍ = []
    Údolí = []
    Strana_svobodných_občanů = []
    Blok_proti_islamu = []
    ODA = []
    Piráti = []
    OBČANÉ_2011 = []
    HAVEL = []
    Národní_fronta = []
    Referendum_o_EU = []
    TOP09 =  []
    ANO = []
    Dobrá_volba = []
    Narodní_socialisté = []
    Republikáni = []
    KDU_ČSL = []
    Realisté = []
    SPORTOVCI = []
    DSSS = []
    SPD = []
    SPO = []
    Narod_sobě = []

    ziskej_udaje_z_obci(URL,Zlínský,Moravskoslezký,Olomoucký,Jihomoravský,Vysočina,Pardubický,Kralovehradecký,Liberecký,Ústecký,Karlovarský,
                        Plzenský,Jihočeský,Středočeský,Praha, naparsovano, adresy_kratke, seznam_adres, volici_v_seznamu,vydane_obalky,
                        platne_hlasy,Občanská_demokratická_strana,Řád_národa, CESTA_ODPOVĚDNÉ_SPOLEČNOSTI,ČSSD, Cibulka,Radostné_Česko,
                        STAN,KSČM,Strana_zelených,ROZUMNÍ,Údolí,Strana_svobodných_občanů,Blok_proti_islamu,ODA,Piráti,OBČANÉ_2011,HAVEL,
                        Národní_fronta,Referendum_o_EU,TOP09,ANO,Dobrá_volba,Narodní_socialisté,Republikáni,KDU_ČSL,Realisté,SPORTOVCI,DSSS,SPD,SPO,Narod_sobě)

    list_slovniku = []
    vytvor_list_slovniku(kody,mesta,volici_v_seznamu,vydane_obalky,platne_hlasy,Občanská_demokratická_strana,
                         Řád_národa,CESTA_ODPOVĚDNÉ_SPOLEČNOSTI, ČSSD, Cibulka, Radostné_Česko, STAN, KSČM,Strana_zelených,
                         ROZUMNÍ, Údolí,Strana_svobodných_občanů,Blok_proti_islamu,ODA,Piráti,OBČANÉ_2011,HAVEL,Národní_fronta,
                         Referendum_o_EU,TOP09,ANO,Dobrá_volba,Narodní_socialisté,Republikáni,KDU_ČSL,Realisté,SPORTOVCI,DSSS,SPD,SPO,
                         Narod_sobě,list_slovniku)

    zapis_do_SCV(nazev_souboru,list_slovniku)


def ziskej_kody_a_mesta(bunky,tabulka, kody, mesta):
    for prvek in bunky:
        tabulka.append(prvek.text)

    for prvek in tabulka:
        if prvek == "X":
            tabulka.remove(prvek)
        elif prvek == '-':
            tabulka.remove(prvek)

    for prvek in tabulka:
        if prvek.isdigit():
            kody.append(prvek)
        else:
            mesta.append(prvek)


def ziskej_udaje_z_obci(URL,Zlínský,Moravskoslezký,Olomoucký,Jihomoravský,Vysočina,Pardubický,Kralovehradecký,Liberecký,Ústecký,Karlovarský,
                        Plzenský,Jihočeský,Středočeský,Praha, naparsovano, adresy_kratke, seznam_adres, volici_v_seznamu, vydane_obalky,
                        platne_hlasy,Občanská_demokratická_strana,Řád_národa, CESTA_ODPOVĚDNÉ_SPOLEČNOSTI,ČSSD, Cibulka,Radostné_Česko,
                        STAN,KSČM,Strana_zelených,ROZUMNÍ,Údolí,Strana_svobodných_občanů,Blok_proti_islamu,ODA,Piráti,OBČANÉ_2011,HAVEL,
                        Národní_fronta,Referendum_o_EU,TOP09,ANO,Dobrá_volba,Narodní_socialisté,Republikáni,KDU_ČSL,Realisté,SPORTOVCI,DSSS,SPD,SPO,Narod_sobě):
    for adresa in naparsovano.find_all("a")[5:-2]:
            adresy_kratke.append(adresa.get("href"))

    if URL == "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8105":
        adresy_kratke.remove('ps34?xjazyk=CZ&xkraj=14&xobec=505927')
    elif URL == "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106":
        adresy_kratke.remove("ps34?xjazyk=CZ&xkraj=14&xobec=554821")
    elif URL == "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302":
        adresy_kratke.remove("ps34?xjazyk=CZ&xkraj=9&xobec=555134")
    elif URL == "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=5103":
        adresy_kratke.remove("ps34?xjazyk=CZ&xkraj=7&xobec=563889")
    elif URL == "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=4207":
        adresy_kratke.remove("ps34?xjazyk=CZ&xkraj=6&xobec=554804")
    elif URL == "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3203":
        adresy_kratke.remove("ps34?xjazyk=CZ&xkraj=4&xobec=554791")

    for adresa in adresy_kratke[::2]:
        seznam_adres.append("https://volby.cz/pls/ps2017nss/" + adresa)

    for adresa in seznam_adres:
        tabulka2 = []
        odpoved2 = requests.get(adresa)
        naparsovano2 = BS(odpoved2.text, "html.parser")
        bunky2 = naparsovano2.find_all("td")
        for prvek in bunky2:
            tabulka2.append(prvek.text)
        volici_v_seznamu.append(tabulka2[3])
        vydane_obalky.append(tabulka2[4])
        platne_hlasy.append(tabulka2[7])
        if URL in Zlínský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[32])
            STAN.append(tabulka2[37])
            KSČM.append(tabulka2[42])
            Strana_zelených.append(tabulka2[47])
            ROZUMNÍ.append(tabulka2[52])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[57])
            Blok_proti_islamu.append(tabulka2[62])
            ODA.append(tabulka2[67])
            Piráti.append(tabulka2[72])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[77])
            TOP09.append(tabulka2[82])
            ANO.append(tabulka2[87])
            Dobrá_volba.append(tabulka2[92])
            Narodní_socialisté.append("nekandiduje")
            Republikáni.append(tabulka2[97])
            KDU_ČSL.append(tabulka2[102])
            Realisté.append(tabulka2[107])
            SPORTOVCI.append(tabulka2[112])
            DSSS.append(tabulka2[117])
            SPD.append(tabulka2[122])
            SPO.append(tabulka2[127])
            Narod_sobě.append("nekandiduje")

        elif URL in Moravskoslezký:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[32])
            STAN.append(tabulka2[37])
            KSČM.append(tabulka2[42])
            Strana_zelených.append(tabulka2[47])
            ROZUMNÍ.append(tabulka2[52])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[57])
            Blok_proti_islamu.append(tabulka2[62])
            ODA.append(tabulka2[67])
            Piráti.append(tabulka2[72])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append(tabulka2[77])
            Referendum_o_EU.append(tabulka2[82])
            TOP09.append(tabulka2[87])
            ANO.append(tabulka2[92])
            Dobrá_volba.append(tabulka2[97])
            Republikáni.append(tabulka2[102])
            KDU_ČSL.append(tabulka2[107])
            Narodní_socialisté.append(tabulka2[112])
            Realisté.append(tabulka2[117])
            SPORTOVCI.append(tabulka2[122])
            DSSS.append(tabulka2[127])
            SPD.append(tabulka2[132])
            SPO.append(tabulka2[137])
            Narod_sobě.append("nekandiduje")

        elif URL in Olomoucký:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[32])
            STAN.append(tabulka2[37])
            KSČM.append(tabulka2[42])
            Strana_zelených.append(tabulka2[47])
            ROZUMNÍ.append(tabulka2[52])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[57])
            Blok_proti_islamu.append(tabulka2[62])
            ODA.append(tabulka2[67])
            Piráti.append(tabulka2[72])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[77])
            TOP09.append(tabulka2[82])
            ANO.append(tabulka2[87])
            Dobrá_volba.append(tabulka2[92])
            Republikáni.append(tabulka2[97])
            KDU_ČSL.append(tabulka2[102])
            Narodní_socialisté.append(tabulka2[107])
            Realisté.append(tabulka2[112])
            SPORTOVCI.append(tabulka2[117])
            DSSS.append(tabulka2[122])
            SPD.append(tabulka2[127])
            SPO.append(tabulka2[132])
            Narod_sobě.append("nekandiduje")

        elif URL in Jihomoravský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[32])
            STAN.append(tabulka2[37])
            KSČM.append(tabulka2[42])
            Strana_zelených.append(tabulka2[47])
            ROZUMNÍ.append(tabulka2[52])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[57])
            Blok_proti_islamu.append(tabulka2[62])
            ODA.append(tabulka2[67])
            Piráti.append(tabulka2[72])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[77])
            TOP09.append(tabulka2[82])
            ANO.append(tabulka2[87])
            Dobrá_volba.append(tabulka2[92])
            Republikáni.append(tabulka2[97])
            KDU_ČSL.append(tabulka2[102])
            Narodní_socialisté.append(tabulka2[107])
            Realisté.append(tabulka2[112])
            SPORTOVCI.append(tabulka2[117])
            DSSS.append(tabulka2[122])
            SPD.append(tabulka2[127])
            SPO.append(tabulka2[132])
            Narod_sobě.append(tabulka2[137])

        elif URL in Vysočina:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[32])
            STAN.append(tabulka2[37])
            KSČM.append(tabulka2[42])
            Strana_zelených.append(tabulka2[47])
            ROZUMNÍ.append(tabulka2[52])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[57])
            Blok_proti_islamu.append(tabulka2[61])
            ODA.append(tabulka2[67])
            Piráti.append(tabulka2[72])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[77])
            TOP09.append(tabulka2[82])
            ANO.append(tabulka2[87])
            Dobrá_volba.append("nekandiduje")
            Republikáni.append(tabulka2[92])
            KDU_ČSL.append(tabulka2[97])
            Narodní_socialisté.append(tabulka2[102])
            Realisté.append(tabulka2[107])
            SPORTOVCI.append(tabulka2[112])
            DSSS.append(tabulka2[117])
            SPD.append(tabulka2[122])
            SPO.append(tabulka2[127])
            Narod_sobě.append("nekandiduje")

        elif URL in Pardubický or URL in Kralovehradecký:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[32])
            STAN.append(tabulka2[37])
            KSČM.append(tabulka2[42])
            Strana_zelených.append(tabulka2[47])
            ROZUMNÍ.append(tabulka2[52])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[57])
            Blok_proti_islamu.append(tabulka2[62])
            ODA.append(tabulka2[67])
            Piráti.append(tabulka2[72])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[77])
            TOP09.append(tabulka2[82])
            ANO.append(tabulka2[87])
            Dobrá_volba.append(tabulka2[92])
            Republikáni.append(tabulka2[97])
            KDU_ČSL.append(tabulka2[102])
            Narodní_socialisté.append("nekandiduje")
            Realisté.append(tabulka2[107])
            SPORTOVCI.append(tabulka2[112])
            DSSS.append(tabulka2[117])
            SPD.append(tabulka2[122])
            SPO.append(tabulka2[127])
            Narod_sobě.append("nekandiduje")

        elif URL in Liberecký or URL in Ústecký:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append("nekandiduje")
            STAN.append(tabulka2[32])
            KSČM.append(tabulka2[37])
            Strana_zelených.append(tabulka2[42])
            ROZUMNÍ.append(tabulka2[47])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[52])
            Blok_proti_islamu.append(tabulka2[57])
            ODA.append(tabulka2[62])
            Piráti.append(tabulka2[67])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[72])
            TOP09.append(tabulka2[77])
            ANO.append(tabulka2[82])
            Dobrá_volba.append(tabulka2[87])
            Republikáni.append(tabulka2[92])
            KDU_ČSL.append(tabulka2[97])
            Narodní_socialisté.append(tabulka2[102])
            Realisté.append(tabulka2[107])
            SPORTOVCI.append(tabulka2[112])
            DSSS.append(tabulka2[117])
            SPD.append(tabulka2[122])
            SPO.append(tabulka2[127])
            Narod_sobě.append("nekandiduje")

        elif URL in Karlovarský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append("nekandiduje")
            ČSSD.append(tabulka2[22])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append("nekandiduje")
            STAN.append(tabulka2[27])
            KSČM.append(tabulka2[32])
            Strana_zelených.append(tabulka2[37])
            ROZUMNÍ.append(tabulka2[42])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[47])
            Blok_proti_islamu.append(tabulka2[52])
            ODA.append(tabulka2[57])
            Piráti.append(tabulka2[62])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[67])
            TOP09.append(tabulka2[72])
            ANO.append(tabulka2[77])
            Dobrá_volba.append("nekandiduje")
            Republikáni.append(tabulka2[82])
            KDU_ČSL.append(tabulka2[87])
            Narodní_socialisté.append("nekandiduje")
            Realisté.append(tabulka2[92])
            SPORTOVCI.append(tabulka2[97])
            DSSS.append(tabulka2[102])
            SPD.append(tabulka2[107])
            SPO.append(tabulka2[112])
            Narod_sobě.append("nekandiduje")

        elif URL in Plzenský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[32])
            STAN.append(tabulka2[37])
            KSČM.append(tabulka2[42])
            Strana_zelených.append(tabulka2[47])
            ROZUMNÍ.append(tabulka2[52])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[57])
            Blok_proti_islamu.append(tabulka2[62])
            ODA.append(tabulka2[67])
            Piráti.append(tabulka2[72])
            OBČANÉ_2011.append(tabulka2[77])
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[82])
            TOP09.append(tabulka2[87])
            ANO.append(tabulka2[92])
            Dobrá_volba.append("nekandiduje")
            Republikáni.append(tabulka2[97])
            KDU_ČSL.append(tabulka2[102])
            Narodní_socialisté.append(tabulka2[107])
            Realisté.append(tabulka2[112])
            SPORTOVCI.append(tabulka2[117])
            DSSS.append(tabulka2[122])
            SPD.append(tabulka2[127])
            SPO.append(tabulka2[132])
            Narod_sobě.append("nekandiduje")

        elif URL in Jihočeský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[32])
            STAN.append(tabulka2[37])
            KSČM.append(tabulka2[42])
            Strana_zelených.append(tabulka2[47])
            ROZUMNÍ.append(tabulka2[52])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[57])
            Blok_proti_islamu.append(tabulka2[62])
            ODA.append(tabulka2[67])
            Piráti.append(tabulka2[72])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[77])
            TOP09.append(tabulka2[82])
            ANO.append(tabulka2[87])
            Dobrá_volba.append(tabulka2[92])
            Republikáni.append(tabulka2[97])
            KDU_ČSL.append(tabulka2[102])
            Narodní_socialisté.append(tabulka2[107])
            Realisté.append(tabulka2[112])
            SPORTOVCI.append(tabulka2[117])
            DSSS.append(tabulka2[122])
            SPD.append(tabulka2[127])
            SPO.append(tabulka2[132])
            Narod_sobě.append("nekandiduje")

        elif URL in Středočeský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[32])
            STAN.append(tabulka2[37])
            KSČM.append(tabulka2[42])
            Strana_zelených.append(tabulka2[47])
            ROZUMNÍ.append(tabulka2[52])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[57])
            Blok_proti_islamu.append(tabulka2[62])
            ODA.append(tabulka2[67])
            Piráti.append(tabulka2[71])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append(tabulka2[77])
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[82])
            TOP09.append(tabulka2[87])
            ANO.append(tabulka2[92])
            Dobrá_volba.append(tabulka2[97])
            Republikáni.append(tabulka2[102])
            KDU_ČSL.append(tabulka2[107])
            Narodní_socialisté.append(tabulka2[112])
            Realisté.append(tabulka2[117])
            SPORTOVCI.append(tabulka2[122])
            DSSS.append(tabulka2[127])
            SPD.append(tabulka2[132])
            SPO.append(tabulka2[137])
            Narod_sobě.append("nekandiduje")

        elif URL in Praha:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[17])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[22])
            ČSSD.append(tabulka2[27])
            Cibulka.append(tabulka2[32])
            Radostné_Česko.append(tabulka2[37])
            STAN.append(tabulka2[42])
            KSČM.append(tabulka2[47])
            Strana_zelených.append(tabulka2[52])
            ROZUMNÍ.append(tabulka2[57])
            Údolí.append(tabulka2[62])
            Strana_svobodných_občanů.append(tabulka2[67])
            Blok_proti_islamu.append(tabulka2[72])
            ODA.append(tabulka2[77])
            Piráti.append(tabulka2[82])
            OBČANÉ_2011.append(tabulka2[87])
            HAVEL.append(tabulka2[92])
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[97])
            TOP09.append(tabulka2[102])
            ANO.append(tabulka2[107])
            Dobrá_volba.append(tabulka2[112])
            Republikáni.append(tabulka2[117])
            KDU_ČSL.append(tabulka2[122])
            Narodní_socialisté.append(tabulka2[127])
            Realisté.append(tabulka2[132])
            SPORTOVCI.append(tabulka2[137])
            DSSS.append(tabulka2[142])
            SPD.append(tabulka2[147])
            SPO.append(tabulka2[152])
            Narod_sobě.append("nekandiduje")


def vytvor_list_slovniku(kody,mesta,volici_v_seznamu,vydane_obalky,platne_hlasy,Občanská_demokratická_strana,
                         Řád_národa,CESTA_ODPOVĚDNÉ_SPOLEČNOSTI,ČSSD,Cibulka,Radostné_Česko,STAN,KSČM,Strana_zelených,
                         ROZUMNÍ,Údolí,Strana_svobodných_občanů,Blok_proti_islamu,ODA,Piráti,OBČANÉ_2011,HAVEL,Národní_fronta,
                         Referendum_o_EU,TOP09,ANO,Dobrá_volba,Narodní_socialisté,Republikáni,KDU_ČSL,Realisté,SPORTOVCI,DSSS,SPD,SPO,
                         Narod_sobě,list_slovniku):
    for číslo in range(len(kody)):
        slovník = {"kod" : kody[číslo], "město" : mesta[číslo], "volici v seznamu" : volici_v_seznamu[číslo],
                   "vydane obalky" : vydane_obalky[číslo], "platne hlasy" : platne_hlasy[číslo], 'Občanská demokratická strana': Občanská_demokratická_strana[číslo],
                   'Řád národa - Vlastenecká unie' : Řád_národa[číslo], 'CESTA ODPOVĚDNÉ SPOLEČNOSTI' : CESTA_ODPOVĚDNÉ_SPOLEČNOSTI[číslo],
                   "Česká str.sociálně demokrat." : ČSSD[číslo], "Cibulka" : Cibulka[číslo], 'Radostné Česko' : Radostné_Česko[číslo], 'STAROSTOVÉ A NEZÁVISLÍ' : STAN[číslo],
                   'Komunistická str.Čech a Moravy' : KSČM[číslo], 'Strana zelených' : Strana_zelených[číslo], "ROZUMNÍ-stop migraci,diktát.EU" : ROZUMNÍ[číslo],
                   "Společ.proti výst.v Prok.údolí" : Údolí[číslo],'Strana svobodných občanů': Strana_svobodných_občanů[číslo],
                   'Blok proti islam.-Obran.domova' : Blok_proti_islamu[číslo],'Občanská demokratická aliance': ODA[číslo], 'Česká pirátská strana': Piráti[číslo],
                   "OBČANÉ 2011-SPRAVEDL. PRO LIDI" : OBČANÉ_2011[číslo], "Unie H.A.V.E.L." : HAVEL[číslo], "Česká národní fronta" : Národní_fronta[číslo],
                   'Referendum o Evropské unii' :  Referendum_o_EU[číslo],'TOP 09' : TOP09[číslo], 'ANO 2011' : ANO[číslo], 'Dobrá volba 2016' : Dobrá_volba[číslo],
                   "Česká strana národně sociální" : Narodní_socialisté[číslo], 'SPR-Republ.str.Čsl. M.Sládka' : Republikáni[číslo],
                   'Křesť.demokr.unie-Čs.str.lid.' : KDU_ČSL[číslo], 'REALISTÉ' : Realisté[číslo],'SPORTOVCI' : SPORTOVCI[číslo],
                   'Dělnic.str.sociální spravedl.': DSSS[číslo], 'Svob.a př.dem.-T.Okamura (SPD)' : SPD[číslo], 'Strana Práv Občanů' : SPO[číslo],
                   "Narod_sobě" : Narod_sobě[číslo]}
        list_slovniku.append(slovník)


def zapis_do_SCV(nazev_souboru,list_slovniku):
    with open(f"{nazev_souboru}.csv", "a", newline="") as csv_soubor:
        zahlavi = ["KÓD", "MĚSTO", "VOLIČI V SEZNAMU", "VYDANÉ OBALKY","PLATNÉ HLASY", 'Občanská demokratická strana v %', 'Řád národa - Vlastenecká unie v %',
                   'CESTA ODPOVĚDNÉ SPOLEČNOSTI v %', "Česká str.sociálně demokratická v %", "Cibulka v %", 'Radostné Česko v %', 'STAROSTOVÉ A NEZÁVISLÍ v %',
                   'Komunistická str.Čech a Moravy v %','Strana zelených v %', "ROZUMNÍ-stop migraci,diktát.EU v %","Společ.proti výst.v Prok.údolí v %",
                   'Strana svobodných občanů v %','Blok proti islam.-Obran.domova v %','Občanská demokratická aliance v %','Česká pirátská strana v %',
                   "OBČANÉ 2011-SPRAVEDL. PRO LIDI v %","Unie H.A.V.E.L. v %","Česká národní fronta v %", 'Referendum o Evropské unii v %',
                   'TOP 09 v %', 'ANO 2011 v %', 'Dobrá volba 2016 v %', 'SPR-Republ.str.Čsl. M.Sládka v %', 'Křesť.demokr.unie-Čs.str.lid. v %',
                   "Česká strana národně sociální v %", 'REALISTÉ v %', 'SPORTOVCI v %','Dělnic.str.sociální spravedl. v %','Svob.a př.dem.-T.Okamura (SPD) v %',
                   'Strana Práv Občanů v %',  "Narod_sobě v %" ]
        writer = csv.DictWriter(csv_soubor, fieldnames=zahlavi)
        writer.writeheader()
        for index, _ in enumerate(list_slovniku):
            writer.writerow(
                {
                    "KÓD": list_slovniku[index]["kod"],
                    "MĚSTO": list_slovniku[index]["město"],
                    "VOLIČI V SEZNAMU" : list_slovniku[index]["volici v seznamu"],
                    "VYDANÉ OBALKY" : list_slovniku[index]["vydane obalky"],
                    "PLATNÉ HLASY" : list_slovniku[index]["platne hlasy"],
                    'Občanská demokratická strana v %' : list_slovniku[index]["Občanská demokratická strana"],
                    'Řád národa - Vlastenecká unie v %' : list_slovniku[index]["Řád národa - Vlastenecká unie"],
                    'CESTA ODPOVĚDNÉ SPOLEČNOSTI v %' : list_slovniku[index]["CESTA ODPOVĚDNÉ SPOLEČNOSTI"],
                    "Česká str.sociálně demokratická v %" : list_slovniku[index]["Česká str.sociálně demokrat."],
                    "Cibulka v %" : list_slovniku[index]["Cibulka"],
                    'Radostné Česko v %' : list_slovniku[index]["Radostné Česko"],
                    'STAROSTOVÉ A NEZÁVISLÍ v %' : list_slovniku[index]["STAROSTOVÉ A NEZÁVISLÍ"],
                    'Komunistická str.Čech a Moravy v %' : list_slovniku[index]["Komunistická str.Čech a Moravy"],
                    'Strana zelených v %' : list_slovniku[index]["Strana zelených"],
                    "ROZUMNÍ-stop migraci,diktát.EU v %" :  list_slovniku[index]["ROZUMNÍ-stop migraci,diktát.EU"],
                    "Společ.proti výst.v Prok.údolí v %" : list_slovniku[index]["Společ.proti výst.v Prok.údolí"],
                    'Strana svobodných občanů v %' : list_slovniku[index]["Strana svobodných občanů"],
                    'Blok proti islam.-Obran.domova v %' : list_slovniku[index]["Blok proti islam.-Obran.domova"],
                    'Občanská demokratická aliance v %': list_slovniku[index]["Občanská demokratická aliance"],
                    'Česká pirátská strana v %' : list_slovniku[index]["Česká pirátská strana"],
                    "OBČANÉ 2011-SPRAVEDL. PRO LIDI v %" : list_slovniku[index]["OBČANÉ 2011-SPRAVEDL. PRO LIDI"],
                    "Unie H.A.V.E.L. v %" : list_slovniku[index]["Unie H.A.V.E.L."],
                    "Česká národní fronta v %" : list_slovniku[index]["Česká národní fronta"],
                    'Referendum o Evropské unii v %' : list_slovniku[index]["Referendum o Evropské unii"],
                    'TOP 09 v %' :  list_slovniku[index]["TOP 09"],
                    'ANO 2011 v %' :  list_slovniku[index]["ANO 2011"],
                    'Dobrá volba 2016 v %' :  list_slovniku[index]["Dobrá volba 2016"],
                    'SPR-Republ.str.Čsl. M.Sládka v %' : list_slovniku[index]["SPR-Republ.str.Čsl. M.Sládka"],
                    'Křesť.demokr.unie-Čs.str.lid. v %' :  list_slovniku[index]["Křesť.demokr.unie-Čs.str.lid."],
                    "Česká strana národně sociální v %": list_slovniku[index]["Česká strana národně sociální"],
                    'REALISTÉ v %' : list_slovniku[index]["REALISTÉ"],
                    'SPORTOVCI v %' : list_slovniku[index]["SPORTOVCI"],
                    'Dělnic.str.sociální spravedl. v %' : list_slovniku[index]["Dělnic.str.sociální spravedl."],
                    'Svob.a př.dem.-T.Okamura (SPD) v %' : list_slovniku[index]["Svob.a př.dem.-T.Okamura (SPD)"],
                    'Strana Práv Občanů v %' :  list_slovniku[index]["Strana Práv Občanů"],
                    "Narod_sobě v %" : list_slovniku[index]["Narod_sobě"],
                })

hlavni("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204","Zlín")














