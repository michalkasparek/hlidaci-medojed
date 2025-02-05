Knihobotí Hlídací pes nehlídá. Místo toho pravidelně štěkne v osm večer, kdy už je poptávaná kniha dávno fuč. Naštěstí je tu Hlídací medojed. [Honey badger don't give a shit](https://www.youtube.com/watch?v=4r7wHMg5Yjg): nastavte si ho jako cron job se spuštěním třeba co pět minut a nechejte si posílat alerty Telegramem.

Jde vlastně o skripty dva:

- ```medojed.py``` načte stránky ze souboru ```config/odkazy.json``` a zkontroluje dostupnost knih. Informace uloží do nového inkrementálně očíslovaného jsonu do složky ```data```.
- ```medojedka.py``` pošle zprávu Telegramem, kdykoliv se v posledních dvou jsonech změní u knihy ```false``` na ```true```.

Funkcionalita je takhle rozdělená proto, aby vám zůstala svoboda ve druhém kroku. Můžete si klidně doprogramovat pingnutí jiným kanálem nebo přímé objednání.

## Jak na to:

- stáhněte si repozitář,
- přejmenuje složku ```config_sample``` na ```sample```,
- do souboru ```odkazy.json``` vložte odkazy na sledované knihy,
- nastavte na skript ```medojed.py``` cron job nebo jiný mechanismus pravidelného spouštění.

### Pokud chcete dostávat zprávy z Telegramu:

- nainstalujte knihovnu: ```pip install python-telegram-bot --upgrade```,
- [vytvořte si na Telegramu bota](https://core.telegram.org/bots#how-do-i-create-a-bot), 
- do souboru ```telegram.json``` uložte botův token,
- najděte si na svém účtu bota a pošlete mu zprávu,
- do souboru ```telegram.json``` uložte [id konverzace](https://gist.github.com/nafiesl/4ad622f344cd1dc3bb1ecbe468ff9f8a),
- nastavte na skript ```medojedka.py``` cron job nebo jiný mechanismus pravidelného spouštění.

Část s Telegramem jde asi udělat i přímočařeji, ale byl to můj první bot.

## Todo:

- Možnost přidat custom e-shopy prostřednictvím druhého jsonu; teď jsou parametry pro hledání skladem/neskladem natvrdo uložené v ```ksefty.json```.
- Možnost multiplikace konfiguračních souborů: hlídám knihy sobě, zároveň jiné knihy kamarádovi…
- Hlídání ceny, např. pro slevy běžeckých bot. (Což už ale bude chtít BeautifulSoup, takže to bude pomalejší a obecně komplikovanjěší.)

Všechny budoucí úpravy rozbijí zpětnou kompatibilitu. Byli jste varováni.