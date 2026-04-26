#  GreitaZita – AI Finance Tracker for Beauty Salons

**GreitaZita** – tai išmanus finansų valdymo asistentas, skirtas grožio salonų savininkams, siekiantiems skaitmenizuoti apskaitą naudojant dirbtinį intelektą ir modernius OOP principus.

### Frontend ir Backend integracija bei duomenų persistencija

Duomenys iš `Front_Endas.html` siunčiami per JavaScript `fetch()` į naują `/add_finance` endpoint'ą (`run_api.py`).  
Endpoint'as apdoroja žinutę per `GreitaZitaAI.process_message()` (išlaikant visus 4 OOP principus ir Builder šabloną), tada naudoja `FinanceFileManager.append_to_csv()` duomenims kaupti faile `salon_1_finance.csv`.

Tai užtikrina:
- Real-time duomenų įvedimą
- Duomenų išsaugojimą net po serverio perkraunimo
- Atitiktį reikalavimui „Reading from file & writing to file“

## 🎯 Tikslas ir Funkcijos
Pagrindinis projekto tikslas – supaprastinti smulkiojo verslo finansų sekimą per interaktyvią sąsają:
* **Finansų sekimas:** Galimybė pridėti/šalinti pajamas bei išlaidas (nuoma, prekės, paslaugos).
* **AI Asistentas:** Natūralios kalbos apdorojimas finansinių duomenų interpretavimui.
* **Real-time Analizė:** Momentinis pelno/nuostolio skaičiavimas vartotojo sąsajoje.

## 🛠️ Techninis Įgyvendinimas (OOP)
Projektas pilnai atitinka „Vilnius Tech“ akademinius reikalavimus:
* **4 OOP Pilarai:** Implementuota Abstrakcija, Paveldėjimas, Polimorfizmas ir Inkapsuliacija (naudojant privačius atributus ir getter/setter metodus).
* **Projektavimo Šablonai:** Naudojami **Singleton** (duomenų bazės valdymui) ir **Builder** (ataskaitų generavimui) šablonai.
* **Ryšiai:** Kodas demonstruoja objektų kompozicijos bei agregacijos principus.

## 🚀 Paleidimas
1.  **Backend:** Terminale paleiskite API serverį:  
    `python3 run_api.py`
2.  **Frontend:** Atidarykite `index.html` (arba `frontend.html`) per VSCode **Live Server**.
3.  **Testai:** Paleiskite automatinius testus logikos patikrai:  
    `python3 tests/test_greitazita.py`

---
**Autorius:** @milis37 | **Kursas:** Objektinis programavimas 2026 | **Vilnius Tech**
