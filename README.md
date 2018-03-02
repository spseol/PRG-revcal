# PRG -- Kalkulačka s reverzní polskou notací

Vytvořte kalkulačku s reverzní polskou notací.
 
[Postfixová notace](https://cs.wikipedia.org/wiki/Postfixov%C3%A1_notace)
(též reverzní polská notace, zkráceně jako RPN) je způsob
zápisu matematického výrazu, kde operátor následuje své operandy, přičemž je
odstraněna nutnost používat závorky -- priorita operátorů se vyjadřuje samotným
zápisem výrazu.

Například výraz `5 + ((1 + 2) * 4) − 3` se zapíše jako:

    5 1 2 + 4 * + 3 −


Základní myšlenkou implementace takové kalkulačky je práce se zásobníkem. 
Jestliže se na vstupu nachází číslo přidá ho program do zásobníku.
Jestliže se na vstupu nachází matematická operace nebo funkce, vybera program
ze zásobníku patřičný počet parametrů, provede operaci a výsledek uloží opět
do zásobníku.

Základ pro svůj program najdete v souboru [revcal.py](revcak.py).
Implementujte prosím následující funkcionalitu:

  * základní matematické operace se dvěma operandy (+, -, *, atd...)
  * základní matematické funkce s jením operandem (`sin`, `log`, atd..)
  * matematické konstanty (e, ¶)
  * komplexní čísla
  * některé funkce pro snadnou práci (prohození posledních dvou čísel 
    v zásobníku, vymazání zásobníku nebo posledního čísla, práce s proměnnými
    a zásobníkem, atd...)
