# Engeto_projekt3
# Instalace balíèkù:
Na dolní lištì otevøete záložku Python Packages.
Do vyhledavaèe napište bs4 a na pravém okraji najdete tlaèítko install.
Stejný proces zopakujte pro instalaci balíèku requests.

# Program:
## Výzvy:
Jak vytáhnout údaje z více tabulek.
Jak vytáhnout údaje z obcí v daném okrese.
Jak se vypoøádat s faktem, že v každém kraji kandiduje jiná struktura stran.

# Struktura programu:
## hlavni
V úvodu si vytváøím  adresy jednotlivých okresù a ty pøidávám do listu reprezentující kraj.

### Ukázka:
```Zlínský = []
for císlo in range(1, 5):
    Zlínský.append("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=720" + str(císlo)``` 

_['https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7201', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7203', 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204']_

To použiji k vytvoøení seznamu adres všech okresù a k øešení tøetí výzvy.
Tahle èást kódu slouží k vytvoøení listu okresù.

`kraje = [Zlínský,Moravskoslezký,Olomoucký,Jihomoravský,Vysoèina,Pardubický,Kralovehradecký,Liberecký,Ústecký,Karlovarský,Plzenský,Jihoèeský,Støedoèeský,Praha]
Možne_adresy = []
for kraj in kraje:
    for l in kraj:
        Možne_adresy.append(l)`
Tahle èást kódu má program ukonèit, když uživatel zadá URL, které se netýká okresù.


`if URL not in Možne_adresy:
    print("Neplatná adresa. Ukonèuji program")
    exit()`






Tahle èást parsuje promìnné.


`odpoved = requests.get(URL)
naparsovano = BS(odpoved.text, "html.parser")
bunky = naparsovano.find_all("td")`



## Získej_kódy_a_mesta
Tahle èást kódu dá údaje do listu, z kterého se èíselné údaje pøidají do listu kódy. Textové údaje se pøidají do listu mìsta.


## Získej_údaje_z_obcí
Tato èást kódu je nejsložitìjší, protože øeší výzvy 2 a 3.

Tahle èást kódu získá „krátké adresy“. Tedy tu èást, která se nachází za https://volby.cz/pls/ps2017nss/.



`for adresa in naparsovano.find_all("a")[5:-2]:
    adresy_kratke.append(adresa.get("href"))`

### Ukázka:
_['ps311?xjazyk=CZ&xkraj=12&xobec=552356&xvyber=7102', 'ps311?xjazyk=CZ&xkraj=12&xobec=552356&xvyber=7102'_


Tahle èást vychytává adresy, které se týkají mìst s odkazem.



`if URL == "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=14&xnumnuts=8105":
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
    adresy_kratke.remove("ps34?xjazyk=CZ&xkraj=4&xobec=554791")`




Tahle èást má za úkol obì èásti spojit.


`for adresa in adresy_kratke[::2]:
    seznam_adres.append("https://volby.cz/pls/ps2017nss/" + adresa)`




Tahle èást získá z každé adresy údaje o volièích a hlasech. Údaje pøidá do pøíslušných seznamù.


`for adresa in seznam_adres:
    tabulka2 = []
    odpoved2 = requests.get(adresa)
    naparsovano2 = BS(odpoved2.text, "html.parser")
    bunky2 = naparsovano2.find_all("td")
    for prvek in bunky2:
        tabulka2.append(prvek.text)
    volici_v_seznamu.append(tabulka2[3])
    vydane_obalky.append(tabulka2[4])
    platne_hlasy.append(tabulka2[7])`





Tahle èást kódu naráží na výzvu èíslo 3. Tu jsem vyøešil podmínkovou vìtví, která rozlišuje, v jakém kraji se nachází URL, kterou uživatel zadal. Pokud zadal Zlínský kraj, tak se aktivuje tahle vìtev a z tabulky dva se pøíslušné indexy zapíšou do pøíslušných listù. Pro URL z jiného kraje se aktivuje jiná vìtev podmínky. Index první kandidující strany je 12 a u následující kandidující strany je o pìt vìtší.



`if URL in Zlínský:
    Obèanská_demokratická_strana.append(tabulka2[12])
    Øád_národa.append(tabulka2[16])
    CESTA_ODPOVÌDNÉ_SPOLEÈNOSTI.append(tabulka2[21])
    ÈSSD.append(tabulka2[26])
    Cibulka.append("nekandiduje")
    Radostné_Èesko.append(tabulka2[31])
    STAN.append(tabulka2[36])
    KSÈM.append(tabulka2[41])`



## vytvoø_list_slovníkù

For cyklus pøiøadí ke klíèi pøíslušnou hodnotu z listu podle jejího indexu. Výsledný slovník pøiøadí do listu slovníkù a proces opakuje s druhým indexem.

### Ukázka:
_{'kod': '552356', 'mesto': 'Babice', 'volici v seznamu': '370', 'vydane obalky': '256', 'platne hlasy': '254'_


## zapis_do_SCV

Funkce vytváøí øádky, které následnì zapisuje do souboru typu SCV.



# Jazyk
Tam kde se mi to zdá pøíhodné (Kraje, strany) jsem ponechal èeské znaky. Jednak jsou to ustálené výrazy a kód bude asi smìøovat hlavnì na èeské uživatele.


# Spouštìní programu
Na konci je zavolána funkce hlavní. Do jejího prvního indexu vložte string s adresou a do druhého indexu str název souboru ve formì stringu. 

### Ukázka:

`hlavni("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204","Zlín")`



# Zobrazení výsledkù
Doporuèuji si otevøít excel. Nahoøe dát data. Dále tlaèítko Z Text/CSV. Následnì vyberete vygenerovaný soubor a dáte importovat. Vyskoèí vám tabulka, kterou potvrdíte tlaèítkem naèíst. Tím se nám vytvoøí hezká tabulka a zbavíme se pevných mezer. 

