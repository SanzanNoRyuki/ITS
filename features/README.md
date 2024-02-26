# Popis testovaných vlastností
**Autor: Roman Fulla <xfulla00>**

## Úvod
Tento dokument obsahuje zoznam testovacích plánov pre internetový obchod.
Rozhodol som sa zamerať na testovanie vlasností spojených s registráciou
a používaním účtu. Názov súboru, v ktorom sa konkrétny testovací plán
vyskytuje sa nachádza v zátvorke za jeho názvom. V odrážkach sú popisy
jednotlivých testovacích scenárov.

## Testovacie plány
* #### Proces registrácie (registration.feature)
    * Prístup do menu "Môj účet"
    * Prístup k registračnému formuláru
    * Nekompletná žiadosť o registráciu
    * Žiadosť o registráciu z nevalidnou hodnotou
    * Úspešná registrácia
    * Pokus o registráciu s už registrovaným e-mailom
* #### Prihlasovanie a odhlasovanie (login.feature)
    * Prístup na stránku prihlásenia
    * Nesprávne vstupné údaje
    * Úspešné prihlásenie
    * Úspešné odhlásenie
* #### Zoznam prianí (wishlist.feature)
    * Prístup k zoznamu prianí
    * Pridanie predstavovaného produktu do zoznamu prianí
    * Odstránenie predstavovaného produktu zo zoznamu prianí
    * Pridanie produktu zo zoznamu prianí do košíka
* #### Automatické doplnenie adresy (autofill.feature)
    * Automatické doplnenie platobných údajov
* #### Úprava účtu (edit.feature)
    * Prístup k úprave účtu
    * Zmena e-mailovej adresy
    * Prihlasovanie starou e-mailovou adresou
* #### História objednávok (orders.feature)
    * Pridanie objednávky do histórie
    * Zobrazenie informácií o objednávke

## Použité nástroje
* [Behave](https://github.com/behave/behave)
* [Python](https://www.python.org/)
