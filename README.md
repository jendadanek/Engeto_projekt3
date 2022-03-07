Instalace bal��k�:
1. Na doln� li�t� otev�ete z�lo�ku Python Packages.
2. Do vyhledava�e napi�te bs4 a na prav�m okraji najdete tla��tko install.
3. Stejn� proces zopakujte pro instalaci bal��ku requests.

Program:
V�zvy:
1. Jak vyt�hnout �daje z�v�ce tabulek.
2. Jak vyt�hnout �daje z�obc� v�dan�m okrese.
3. Jak se vypo��dat s�faktem, �e v�ka�d�m kraji kandiduje jin� struktura stran.

Struktura programu:
1. Main
V��vodu si vytv���m adresy jednotliv�ch okres� a ty p�id�v�m do listu reprezentuj�c� kraj.
   
Uk�zka:
Zl�nsk� = []
for ��slo in range(1, 5):
    Zl�nsk�.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=720" + str(��slo))
['https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7201', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7203', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204']

To pou�iji k�vytvo�en� seznamu adres v�ech okres� a k��e�en� t�et� v�zvy.



Tahle ��st k�du slou�� k�vytvo�en� listu okres�.

kraje = [Zl�nsk�,Moravskoslezk�,Olomouck�,Jihomoravsk�,Vyso�ina,Pardubick�,Kralovehradeck�,Libereck�,�steck�,Karlovarsk�,Plzensk�,Jiho�esk�,St�edo�esk�,Praha]

Mo�n�_adresy = []

for kraj in kraje:

    for l in kraj:

        Mo�n�_adresy.append(l)


Tahle ��st k�du m� program ukon�it, kdy� u�ivatel zad� URL, kter� se net�k� okres�.

if URL not in Mo�n�_adresy:

    print("Neplatn� adresa. Ukon�uji program")

    exit()






Tahle ��st parsuje prom�nn�.

odpoved = requests.get(URL)

naparsovano = BS(odpoved.text, "html.parser")

bunky = naparsovano.find_all("td")


2. Z�skej_k�dy_a_mesta

Tahle ��st k�du d� �daje do listu, z�kter�ho se ��seln� �daje p�idaj� do listu k�dy. Textov� �daje se p�idaj� do listu m�sta.


3. Z�skej_�daje_z_obc�


Tato ��st k�du je nejslo�it�j��, proto�e �e�� v�zvy 2 a 3.

Tahle ��st k�du z�sk� �kr�tk� adresy�. Tedy tu ��st, kter� se nach�z� za 

https://volby.cz/pls/ps2017nss/.


for adresa in naparsovano.find_all("a")[5:-2]:

    adresy_kratke.append(adresa.get("href"))

Uk�zka:
['ps311?xjazyk=CZ&xkraj=12&xobec=552356&xvyber=7102', 'ps311?xjazyk=CZ&xkraj=12&xobec=552356&xvyber=7102'


Tahle ��st vychyt�v� adresy, kter� se t�kaj� m�st s�odkazem.

if URL == "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xnumnuts=8105":
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




Tahle ��st m� za �kol ob� ��sti spojit.

for adresa in adresy_kratke[::2]:

    seznam_adres.append("https://volby.cz/pls/ps2017nss/" + adresa)



Tahle ��st z�sk� z�ka�d� adresy �daje o voli��ch a hlasech. �daje p�id� do p��slu�n�ch seznam�.

for adresa in seznam_adres:

    tabulka2 = []

    odpoved2 = requests.get(adresa)

    naparsovano2 = BS(odpoved2.text, "html.parser")

    bunky2 = naparsovano2.find_all("td")

    for prvek in bunky2:

        tabulka2.append(prvek.text)

    tabulka2.remove("X")

    voli�i_v_seznamu.append(tabulka2[3])

    vydane_obalky.append(tabulka2[4])

    platne_hlasy.append(tabulka2[7])





Tahle ��st k�du nar�� na v�zvu ��slo 3. Tu jsem vy�e�il podm�nkovou v�tv�, kter� rozli�uje, v�jak�m kraji se nach�z� URL, kterou u�ivatel zadal. Pokud zadal Zl�nsk� kraj, tak se aktivuje tahle v�tev a z�tabulky dva se p��slu�n� indexy zap�ou do p��slu�n�ch list�. Pro URL z�jin�ho kraje se aktivuje jin� v�tev podm�nky.


if URL in Zl�nsk�:

    Ob�ansk�_demokratick�_strana.append(tabulka2[12])

    ��d_n�roda.append(tabulka2[16])

    CESTA_ODPOV�DN�_SPOLE�NOSTI.append(tabulka2[21])

    �SSD.append(tabulka2[26])

    Cibulka.append("nekandiduje")

    Radostn�_�esko.append(tabulka2[31])

    STAN.append(tabulka2[36])

    KS�M.append(tabulka2[41])


4. vytvo�_list_slovn�k�

For cyklus p�i�ad� ke kl��i p��slu�nou hodnotu z�listu podle jej�ho indexu. V�sledn� slovn�k p�i�ad� do listu slovn�k� a proces opakuje s�druh�m indexem.

Uk�zka:
{'kod': '552356', 'mesto': 'Babice', 'volici v seznamu': '370', 'vydane obalky': '256', 'platne hlasy': '254'


5. zapis_do_SCV(nazev_souboru,list_slovniku)

Funkce vytv��� ��dky, kter� n�sledn� zapisuje do souboru typu SCV.

