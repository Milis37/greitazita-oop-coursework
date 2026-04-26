GreitaZita – AI Finance Tracker for Beauty Salons
GreitaZita – tai išmanus finansų valdymo asistentas, skirtas grožio salonų savininkams, siekiantiems skaitmenizuoti savo verslo apskaitą. Projektas sukurtas kaip Objektinio programavimo (OOP) kursinis darbas, integruojantis dirbtinį intelektą finansinių duomenų analizei.

🚀 Gyva demonstracija: Verslo vizija paremta poesimus.lt estetika ir poreikiais.

🎯 Verslo koncepcija ir tikslas
Dauguma smulkių grožio salonų vis dar naudoja popierines užrašines arba sudėtingas „Excel“ lenteles. GreitaZita išsprendžia šią problemą:

Natūralios kalbos apdorojimas: Vartotojas gali tiesiog parašyti „Sumokėjau 1200 už nuomą ir gavau 5000 už paslaugas“, o sistema automatiškai suklasifikuoja duomenis.

OOP struktūrizavimas: Kiekviena išlaida ar pajamos yra unikalus objektas su savo savybėmis, užtikrinant duomenų vientisumą.

Momentinė analizė: AI asistentas realiu laiku apskaičiuoja pelną ir pateikia įžvalgas.

🛠️ Techninis įgyvendinimas (OOP reikalavimai)
Projektas griežtai laikosi kursinio apraše nurodytų reikalavimų:

1. 4 OOP principai

Abstrakcija: Naudojama FinancialRecord bazinė klasė su abstrakčiais metodais.

Paveldėjimas: RentExpense ir SupplyExpense paveldi funkcionalumą iš bendros Expense klasės.

Inkapsuliacija: Finansiniai duomenys (pvz., _amount) yra privatūs ir pasiekiami tik per getter/setter metodus.

Polimorfizmas: Kiekviena klasė savaip perrašo get_description() metodą, pateikdama specifinę informaciją.

2. Projektavimo šablonai (Design Patterns) 

Singleton: DatabaseManager užtikrina, kad visoje programoje būtų tik vienas aktyvus ryšys su duomenimis.

Builder: FinancialReportBuilder naudojamas sudėtingoms finansinėms ataskaitoms konstruoti žingsnis po žingsnio.

3. Kompozicija ir Agregacija

Salon klasė agreguoja Expense ir Earning objektų sąrašus, taip suformuodama pilną verslo finansinį vaizdą.

💻 Kaip paleisti programą? 
+1

Reikalavimai

Python 3.9+

Naršyklė (rekomenduojama Chrome arba Brave)

Instaliacija

Klonuokite saugyklą:

Bash
git clone https://github.com/milis37/greitazita.git
Paleiskite API serverį (Backend):

Bash
python3 run_api.py
Atidarykite tests/index.html naudodami Live Server plėtinį per VSCode.

🧪 Testavimas 
+1

Projekto stabilumą užtikrina automatiniai testai (unittest karkasas).
Norėdami paleisti testus, terminale rašykite:

Bash
python3 -m unittest tests/test_greitazita.py -v
Testų apimtis: 4 OOP pilarų patikra, Singleton nuoseklumas, Builder logika ir AI atsakymų validacija.

📈 Ateities perspektyvos 

Automatizuotas kvitų skenavimas: OCR integracija išlaidų fiksavimui iš nuotraukų.

Daugiakalbis palaikymas: Sistemos pritaikymas tarptautinei grožio industrijos rinkai.

Metinė prognozė: AI pagrįstas būsimų pajamų prognozavimas pagal istorinius duomenis.

Autorius: @milis37 | Kursas: Objektinis programavimas 2026 | Vilnius Tech    Activity list
    User accounts
    Money exchange system
    



