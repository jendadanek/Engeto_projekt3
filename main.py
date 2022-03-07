import requests
from bs4 import BeautifulSoup as BS
import csv

def hlavni(URL,nazev_souboru):
    Zlínský = []
    for číslo in range(1, 5):
        Zlínský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=720" + str(číslo))


    Moravskoslezký = []
    for číslo in range(1, 7):
        Moravskoslezký.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=810" + str(číslo))

    Olomoucký = []
    for číslo in range(1, 6):
        Olomoucký.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=710" + str(číslo))

    Jihomoravský = []
    for číslo in range(1, 8):
        Jihomoravský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=620" + str(číslo))

    Vysočina = []
    for číslo in range(1, 6):
        Vysočina.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=610" + str(číslo))

    Pardubický = []
    for číslo in range(1, 5):
        Pardubický.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=530" + str(číslo))

    Kralovehradecký = []
    for číslo in range(1, 6):
        Kralovehradecký.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=520" + str(číslo))

    Liberecký = []
    for číslo in range(1, 5):
        Liberecký.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=7&xnumnuts=510" + str(číslo))

    Ústecký = []
    for číslo in range(1, 8):
        Ústecký.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=6&xnumnuts=420" + str(číslo))

    Karlovarský = []
    for číslo in range(1, 4):
        Karlovarský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=5&xnumnuts=410" + str(číslo))

    Plzenský = []
    for číslo in range(1, 8):
        Plzenský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=320" + str(číslo))

    Jihočeský = []
    for číslo in range(1, 7):
        Jihočeský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=310" + str(číslo))

    Středočeský = []
    for číslo in range(1, 13):
        Středočeský.append("hhttps://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=211" + str(číslo))

    Praha = ["https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100"]

    kraje = [Zlínský,Moravskoslezký,Olomoucký,Jihomoravský,Vysočina,Pardubický,Kralovehradecký,Liberecký,Ústecký,Karlovarský,Plzenský,Jihočeský,Středočeský,Praha]
    Možné_adresy = []
    for kraj in kraje:
        for l in kraj:
            Možné_adresy.append(l)

    if URL not in Možné_adresy:
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

    voliči_v_seznamu = []
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
                        Plzenský,Jihočeský,Středočeský,Praha, naparsovano, adresy_kratke, seznam_adres, voliči_v_seznamu,vydane_obalky,
                        platne_hlasy,Občanská_demokratická_strana,Řád_národa, CESTA_ODPOVĚDNÉ_SPOLEČNOSTI,ČSSD, Cibulka,Radostné_Česko,
                        STAN,KSČM,Strana_zelených,ROZUMNÍ,Údolí,Strana_svobodných_občanů,Blok_proti_islamu,ODA,Piráti,OBČANÉ_2011,HAVEL,
                        Národní_fronta,Referendum_o_EU,TOP09,ANO,Dobrá_volba,Narodní_socialisté,Republikáni,KDU_ČSL,Realisté,SPORTOVCI,DSSS,SPD,SPO,Narod_sobě)



    list_slovniku = []
    vytvoř_list_slovniků(kody,mesta,voliči_v_seznamu,vydane_obalky,platne_hlasy,Občanská_demokratická_strana,
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

    for prvek in tabulka[:-3]:
        if prvek.isdigit():
            kody.append(prvek)
        else:
            mesta.append(prvek)


def ziskej_udaje_z_obci(URL,Zlínský,Moravskoslezký,Olomoucký,Jihomoravský,Vysočina,Pardubický,Kralovehradecký,Liberecký,Ústecký,Karlovarský,
                        Plzenský,Jihočeský,Středočeský,Praha, naparsovano, adresy_kratke, seznam_adres, voliči_v_seznamu,vydane_obalky,
                        platne_hlasy,Občanská_demokratická_strana,Řád_národa, CESTA_ODPOVĚDNÉ_SPOLEČNOSTI,ČSSD, Cibulka,Radostné_Česko,
                        STAN,KSČM,Strana_zelených,ROZUMNÍ,Údolí,Strana_svobodných_občanů,Blok_proti_islamu,ODA,Piráti,OBČANÉ_2011,HAVEL,
                        Národní_fronta,Referendum_o_EU,TOP09,ANO,Dobrá_volba,Narodní_socialisté,Republikáni,KDU_ČSL,Realisté,SPORTOVCI,DSSS,SPD,SPO,Narod_sobě):
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
        if URL in Zlínský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[31])
            STAN.append(tabulka2[36])
            KSČM.append(tabulka2[41])
            Strana_zelených.append(tabulka2[46])
            ROZUMNÍ.append(tabulka2[51])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[56])
            Blok_proti_islamu.append(tabulka2[61])
            ODA.append(tabulka2[66])
            Piráti.append(tabulka2[71])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[76])
            TOP09.append(tabulka2[81])
            ANO.append(tabulka2[86])
            Dobrá_volba.append(tabulka2[91])
            Narodní_socialisté.append("nekandiduje")
            Republikáni.append(tabulka2[96])
            KDU_ČSL.append(tabulka2[101])
            Realisté.append(tabulka2[106])
            SPORTOVCI.append(tabulka2[111])
            DSSS.append(tabulka2[116])
            SPD.append(tabulka2[121])
            SPO.append(tabulka2[126])
            Narod_sobě.append("nekandiduje")


        elif URL in Moravskoslezký:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[31])
            STAN.append(tabulka2[36])
            KSČM.append(tabulka2[41])
            Strana_zelených.append(tabulka2[46])
            ROZUMNÍ.append(tabulka2[51])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[56])
            Blok_proti_islamu.append(tabulka2[61])
            ODA.append(tabulka2[66])
            Piráti.append(tabulka2[71])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append(tabulka2[76])
            Referendum_o_EU.append(tabulka2[81])
            TOP09.append(tabulka2[86])
            ANO.append(tabulka2[91])
            Dobrá_volba.append(tabulka2[96])
            Republikáni.append(tabulka2[101])
            KDU_ČSL.append(tabulka2[106])
            Narodní_socialisté.append(tabulka2[111])
            Realisté.append(tabulka2[116])
            SPORTOVCI.append(tabulka2[121])
            DSSS.append(tabulka2[126])
            SPD.append(tabulka2[131])
            SPO.append(tabulka2[136])
            Narod_sobě.append("nekandiduje")



        elif URL in Olomoucký:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[31])
            STAN.append(tabulka2[36])
            KSČM.append(tabulka2[41])
            Strana_zelených.append(tabulka2[46])
            ROZUMNÍ.append(tabulka2[51])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[56])
            Blok_proti_islamu.append(tabulka2[61])
            ODA.append(tabulka2[66])
            Piráti.append(tabulka2[71])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[76])
            TOP09.append(tabulka2[81])
            ANO.append(tabulka2[86])
            Dobrá_volba.append(tabulka2[91])
            Republikáni.append(tabulka2[96])
            KDU_ČSL.append(tabulka2[101])
            Narodní_socialisté.append(tabulka2[106])
            Realisté.append(tabulka2[111])
            SPORTOVCI.append(tabulka2[116])
            DSSS.append(tabulka2[121])
            SPD.append(tabulka2[126])
            SPO.append(tabulka2[131])
            Narod_sobě.append("nekandiduje")



        elif URL in Jihomoravský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[31])
            STAN.append(tabulka2[36])
            KSČM.append(tabulka2[41])
            Strana_zelených.append(tabulka2[46])
            ROZUMNÍ.append(tabulka2[51])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[56])
            Blok_proti_islamu.append(tabulka2[61])
            ODA.append(tabulka2[66])
            Piráti.append(tabulka2[71])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[76])
            TOP09.append(tabulka2[81])
            ANO.append(tabulka2[86])
            Dobrá_volba.append(tabulka2[91])
            Republikáni.append(tabulka2[96])
            KDU_ČSL.append(tabulka2[101])
            Narodní_socialisté.append(tabulka2[106])
            Realisté.append(tabulka2[111])
            SPORTOVCI.append(tabulka2[116])
            DSSS.append(tabulka2[121])
            SPD.append(tabulka2[126])
            SPO.append(tabulka2[131])
            Narod_sobě.append(tabulka2[136])


        elif URL in Vysočina:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[31])
            STAN.append(tabulka2[36])
            KSČM.append(tabulka2[41])
            Strana_zelených.append(tabulka2[46])
            ROZUMNÍ.append(tabulka2[51])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[56])
            Blok_proti_islamu.append(tabulka2[61])
            ODA.append(tabulka2[66])
            Piráti.append(tabulka2[71])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[76])
            TOP09.append(tabulka2[81])
            ANO.append(tabulka2[86])
            Dobrá_volba.append("nekandiduje")
            Republikáni.append(tabulka2[91])
            KDU_ČSL.append(tabulka2[96])
            Narodní_socialisté.append(tabulka2[101])
            Realisté.append(tabulka2[106])
            SPORTOVCI.append(tabulka2[111])
            DSSS.append(tabulka2[116])
            SPD.append(tabulka2[121])
            SPO.append(tabulka2[126])
            Narod_sobě.append("nekandiduje")



        elif URL in Pardubický or URL in Kralovehradecký:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[31])
            STAN.append(tabulka2[36])
            KSČM.append(tabulka2[41])
            Strana_zelených.append(tabulka2[46])
            ROZUMNÍ.append(tabulka2[51])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[56])
            Blok_proti_islamu.append(tabulka2[61])
            ODA.append(tabulka2[66])
            Piráti.append(tabulka2[71])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[76])
            TOP09.append(tabulka2[81])
            ANO.append(tabulka2[86])
            Dobrá_volba.append(tabulka2[91])
            Republikáni.append(tabulka2[96])
            KDU_ČSL.append(tabulka2[101])
            Narodní_socialisté.append("nekandiduje")
            Realisté.append(tabulka2[106])
            SPORTOVCI.append(tabulka2[111])
            DSSS.append(tabulka2[116])
            SPD.append(tabulka2[121])
            SPO.append(tabulka2[126])
            Narod_sobě.append("nekandiduje")



        elif URL in Liberecký or URL in Ústecký:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append("nekandiduje")
            STAN.append(tabulka2[31])
            KSČM.append(tabulka2[36])
            Strana_zelených.append(tabulka2[41])
            ROZUMNÍ.append(tabulka2[46])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[51])
            Blok_proti_islamu.append(tabulka2[56])
            ODA.append(tabulka2[61])
            Piráti.append(tabulka2[66])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[71])
            TOP09.append(tabulka2[76])
            ANO.append(tabulka2[81])
            Dobrá_volba.append(tabulka2[86])
            Republikáni.append(tabulka2[91])
            KDU_ČSL.append(tabulka2[96])
            Narodní_socialisté.append(tabulka2[101])
            Realisté.append(tabulka2[106])
            SPORTOVCI.append(tabulka2[111])
            DSSS.append(tabulka2[116])
            SPD.append(tabulka2[121])
            SPO.append(tabulka2[126])
            Narod_sobě.append("nekandiduje")



        elif URL in Karlovarský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[26])
            STAN.append(tabulka2[26])
            KSČM.append(tabulka2[31])
            Strana_zelených.append(tabulka2[36])
            ROZUMNÍ.append(tabulka2[41])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[46])
            Blok_proti_islamu.append(tabulka2[51])
            ODA.append(tabulka2[56])
            Piráti.append(tabulka2[61])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[66])
            TOP09.append(tabulka2[71])
            ANO.append(tabulka2[76])
            Dobrá_volba.append("nekandiduje")
            Republikáni.append(tabulka2[81])
            KDU_ČSL.append(tabulka2[86])
            Narodní_socialisté.append("nekandiduje")
            Realisté.append(tabulka2[91])
            SPORTOVCI.append(tabulka2[96])
            DSSS.append(tabulka2[101])
            SPD.append(tabulka2[106])
            SPO.append(tabulka2[111])
            Narod_sobě.append("nekandiduje")



        elif URL in Plzenský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append("nekandiduje")
            ČSSD.append(tabulka2[21])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[26])
            STAN.append(tabulka2[31])
            KSČM.append(tabulka2[36])
            Strana_zelených.append(tabulka2[41])
            ROZUMNÍ.append(tabulka2[46])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[51])
            Blok_proti_islamu.append(tabulka2[56])
            ODA.append(tabulka2[61])
            Piráti.append(tabulka2[66])
            OBČANÉ_2011.append(tabulka2[71])
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[76])
            TOP09.append(tabulka2[81])
            ANO.append(tabulka2[86])
            Dobrá_volba.append("nekandiduje")
            Republikáni.append(tabulka2[91])
            KDU_ČSL.append(tabulka2[96])
            Narodní_socialisté.append(tabulka2[101])
            Realisté.append(tabulka2[106])
            SPORTOVCI.append(tabulka2[111])
            DSSS.append(tabulka2[116])
            SPD.append(tabulka2[121])
            SPO.append(tabulka2[126])
            Narod_sobě.append("nekandiduje")


        elif URL in Jihočeský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[31])
            STAN.append(tabulka2[36])
            KSČM.append(tabulka2[41])
            Strana_zelených.append(tabulka2[46])
            ROZUMNÍ.append(tabulka2[51])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[56])
            Blok_proti_islamu.append(tabulka2[61])
            ODA.append(tabulka2[66])
            Piráti.append(tabulka2[71])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append("nekandiduje")
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[76])
            TOP09.append(tabulka2[81])
            ANO.append(tabulka2[86])
            Dobrá_volba.append(tabulka2[91])
            Republikáni.append(tabulka2[96])
            KDU_ČSL.append(tabulka2[101])
            Narodní_socialisté.append(tabulka2[106])
            Realisté.append(tabulka2[111])
            SPORTOVCI.append(tabulka2[116])
            DSSS.append(tabulka2[121])
            SPD.append(tabulka2[126])
            SPO.append(tabulka2[131])
            Narod_sobě.append("nekandiduje")



        elif URL in Středočeský:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append("nekandiduje")
            Radostné_Česko.append(tabulka2[31])
            STAN.append(tabulka2[36])
            KSČM.append(tabulka2[41])
            Strana_zelených.append(tabulka2[46])
            ROZUMNÍ.append(tabulka2[51])
            Údolí.append("nekandiduje")
            Strana_svobodných_občanů.append(tabulka2[56])
            Blok_proti_islamu.append(tabulka2[61])
            ODA.append(tabulka2[66])
            Piráti.append(tabulka2[71])
            OBČANÉ_2011.append("nekandiduje")
            HAVEL.append(tabulka2[76])
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[81])
            TOP09.append(tabulka2[86])
            ANO.append(tabulka2[91])
            Dobrá_volba.append(tabulka2[96])
            Republikáni.append(tabulka2[101])
            KDU_ČSL.append(tabulka2[106])
            Narodní_socialisté.append(tabulka2[111])
            Realisté.append(tabulka2[116])
            SPORTOVCI.append(tabulka2[121])
            DSSS.append(tabulka2[126])
            SPD.append(tabulka2[131])
            SPO.append(tabulka2[136])
            Narod_sobě.append("nekandiduje")


        elif URL in Praha:
            Občanská_demokratická_strana.append(tabulka2[12])
            Řád_národa.append(tabulka2[16])
            CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
            ČSSD.append(tabulka2[26])
            Cibulka.append(tabulka2[31])
            Radostné_Česko.append(tabulka2[36])
            STAN.append(tabulka2[41])
            KSČM.append(tabulka2[46])
            Strana_zelených.append(tabulka2[51])
            ROZUMNÍ.append(tabulka2[56])
            Údolí.append(tabulka2[61])
            Strana_svobodných_občanů.append(tabulka2[66])
            Blok_proti_islamu.append(tabulka2[71])
            ODA.append(tabulka2[76])
            Piráti.append(tabulka2[81])
            OBČANÉ_2011.append(tabulka2[86])
            HAVEL.append(tabulka2[91])
            Národní_fronta.append("nekandiduje")
            Referendum_o_EU.append(tabulka2[96])
            TOP09.append(tabulka2[101])
            ANO.append(tabulka2[106])
            Dobrá_volba.append(tabulka2[111])
            Republikáni.append(tabulka2[116])
            KDU_ČSL.append(tabulka2[121])
            Narodní_socialisté.append(tabulka2[126])
            Realisté.append(tabulka2[131])
            SPORTOVCI.append(tabulka2[136])
            DSSS.append(tabulka2[141])
            SPD.append(tabulka2[146])
            SPO.append(tabulka2[151])
            Narod_sobě.append("nekandiduje")


def vytvoř_list_slovniků(kody,mesta,voliči_v_seznamu,vydane_obalky,platne_hlasy,Občanská_demokratická_strana,
                         Řád_národa,CESTA_ODPOVĚDNÉ_SPOLEČNOSTI,ČSSD,Cibulka,Radostné_Česko,STAN,KSČM,Strana_zelených,
                         ROZUMNÍ,Údolí,Strana_svobodných_občanů,Blok_proti_islamu,ODA,Piráti,OBČANÉ_2011,HAVEL,Národní_fronta,
                         Referendum_o_EU,TOP09,ANO,Dobrá_volba,Narodní_socialisté,Republikáni,KDU_ČSL,Realisté,SPORTOVCI,DSSS,SPD,SPO,
                         Narod_sobě,list_slovniku):
    for číslo in range(len(kody)):
        slovník = {"kod" : kody[číslo], "mesto" : mesta[číslo], "volici v seznamu" : voliči_v_seznamu[číslo],
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
        zahlavi = ["KOD", "MESTO", "VOLICI V SEZNAMU", "VYDANE OBALKY","PLATNE HLASY", 'Občanská demokratická strana v %', 'Řád národa - Vlastenecká unie v %',
                   'CESTA ODPOVĚDNÉ SPOLEČNOSTI v %', "Česká str.sociálně demokratická v %", "Cibulka v %", 'Radostné Česko v %', 'STAROSTOVÉ A NEZÁVISLÍ v %',
                   'Komunistická str.Čech a Moravy v %','Strana zelených v %', "ROZUMNÍ-stop migraci,diktát.EU v %","Společ.proti výst.v Prok.údolí v %",
                   'Strana svobodných občanů v %','Blok proti islam.-Obran.domova v %','Občanská demokratická aliance v %','Česká pirátská strana v %',
                   "OBČANÉ 2011-SPRAVEDL. PRO LIDI v %","Unie H.A.V.E.L. v %","Česká národní fronta v %", 'Referendum o Evropské unii v %',
                   'TOP 09 v %', 'ANO 2011 v %', 'Dobrá volba 2016 v %', "Česká strana národně sociální v %", 'SPR-Republ.str.Čsl. M.Sládka v %',
                   'Křesť.demokr.unie-Čs.str.lid. v %', 'REALISTÉ v %', 'SPORTOVCI v %','Dělnic.str.sociální spravedl. v %','Svob.a př.dem.-T.Okamura (SPD) v %',
                   'Strana Práv Občanů v %',  "Narod_sobě v %" ]
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
                    "Česká strana národně sociální v %" : list_slovniku[index]["Česká strana národně sociální"],
                    'SPR-Republ.str.Čsl. M.Sládka v %' : list_slovniku[index]["SPR-Republ.str.Čsl. M.Sládka"],
                    'Křesť.demokr.unie-Čs.str.lid. v %' :  list_slovniku[index]["Křesť.demokr.unie-Čs.str.lid."],
                    'REALISTÉ v %' : list_slovniku[index]["REALISTÉ"],
                    'SPORTOVCI v %' : list_slovniku[index]["SPORTOVCI"],
                    'Dělnic.str.sociální spravedl. v %' : list_slovniku[index]["Dělnic.str.sociální spravedl."],
                    'Svob.a př.dem.-T.Okamura (SPD) v %' : list_slovniku[index]["Svob.a př.dem.-T.Okamura (SPD)"],
                    'Strana Práv Občanů v %' :  list_slovniku[index]["Strana Práv Občanů"],
                    "Narod_sobě v %" : list_slovniku[index]["Narod_sobě"],
                })



hlavni("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7102","Okres_Olomouc")








