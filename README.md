# Engeto_projekt3
Instalace balíčků:
1.	Na dolní liště otevřete záložku Python Packages.
2.	Do vyhledavače napište bs4 a na pravém okraji najdete tlačítko install.
3.	Stejný proces zopakujte pro instalaci balíčku requests.

Program:
Výzvy:
1.	Jak vytáhnout údaje z více tabulek.
2.	Jak vytáhnout údaje z obcí v daném okrese.
3.	Jak se vypořádat s faktem, že v každém kraji kandiduje jiná struktura stran.

Struktura programu:
1.	Main
V úvodu si vytvářím adresy jednotlivých okresů a ty přidávám do listu reprezentující kraj.
Ukázka:
Zlínský = []
for číslo in range(1, 5):
    Zlínský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=720" + str(číslo))
['https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7201', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7203', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204']
To použije k vytvoření seznamu adres všech okresů a k řešení třetí výzvy.
Tahle část kódu slouží k vytvoření listu okresů.

kraje = [Zlínský,Moravskoslezký,Olomoucký,Jihomoravský,Vysočina,Pardubický,Kralovehradecký,Liberecký,Ústecký,Karlovarský,Plzenský,Jihočeský,Středočeský,Praha]
Možné_adresy = []
for kraj in kraje:
    for l in kraj:
        Možné_adresy.append(l)


Tahle část kódu má program ukončit, když uživatel zadá URL, které se netýká okresů.

if URL not in Možné_adresy:
    print("Neplatná adresa. Ukončuji program")
    exit()
Tahle část parsuje proměnné.

odpoved = requests.get(URL)
naparsovano = BS(odpoved.text, "html.parser")
bunky = naparsovano.find_all("td")


2.	Získej_kódy_a_mesta

Tahle část kódu dá údaje do listu, z kterého se číselné údaje přidají do listu kódy. Textové údaje se přidají do listu města.


3.	Získej_údaje_z_obcí


Tato část kódu je nejsložitější, protože řeší výzvy 2 a 3.

Tahle část kódu získá „krátké adresy“. Tedy tu část, která se nachází za 

https://volby.cz/pls/ps2017nss/.


for adresa in naparsovano.find_all("a")[5:-2]:
    adresy_kratke.append(adresa.get("href"))

Ukázka:
['ps311?xjazyk=CZ&xkraj=12&xobec=552356&xvyber=7102', 'ps311?xjazyk=CZ&xkraj=12&xobec=552356&xvyber=7102'


Tahle část vychytává adresy, které se týkají měst s odkazem.
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




Tahle část má za úkol obě části spojit.

for adresa in adresy_kratke[::2]:
    seznam_adres.append("https://volby.cz/pls/ps2017nss/" + adresa)



Tahle část získá z každé adresy údaje o voličích a hlasech. Údaje přidá do příslušných seznamů.

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





Tahle část kódu naráží na výzvu číslo 3. Tu jsem vyřešil podmínkovou větví, která rozlišuje, v jakém kraji se nachází URL, kterou uživatel zadal. Pokud zadal Zlínský kraj, tak se aktivuje tahle větev a z tabulky dva se příslušné indexy zapíšou do příslušných listů. Pro URL z jiného kraje se aktivuje jiná větev podmínky.


if URL in Zlínský:
    Občanská_demokratická_strana.append(tabulka2[12])
    Řád_národa.append(tabulka2[16])
    CESTA_ODPOVĚDNÉ_SPOLEČNOSTI.append(tabulka2[21])
    ČSSD.append(tabulka2[26])
    Cibulka.append("nekandiduje")
    Radostné_Česko.append(tabulka2[31])
    STAN.append(tabulka2[36])
    KSČM.append(tabulka2[41])


4.	vytvoř_list_slovníků

For cyklus přiřadí ke klíči příslušnou hodnotu z listu podle jejího indexu. Výsledný slovník přiřadí do listu slovníků a proces opakuje s druhým indexem.

Ukázka:
{'kod': '552356', 'mesto': 'Babice', 'volici v seznamu': '370', 'vydane obalky': '256', 'platne hlasy': '254'


5.	zapis_do_SCV(nazev_souboru,list_slovniku)

Funkce vytváří řádky, které následně zapisuje do souboru typu SCV.

