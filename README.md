# Youtube_downloader_Django

## Django project - YouTube downloader

Tato aplikace umožňuje uživatelům stahovat videa z YouTube a konvertovat je na MP3 přímo z webového rozhraní. Aplikace je postavena na Django a používá yt-dlp pro stahování a konverzi videí.

## Funkce

- Stahování videí z YouTube
- Konverze videí na MP3
- Možnost zadání URL videa přes webový formulář
- Stažení MP3 souboru přímo na zařízení uživatele

## Požadavky

- Python 3.6 nebo novější
- Django
- yt-dlp

## Instalace

1. Klonujte tento repozitář do vašeho lokálního prostředí:
    ```bash
    git clone https://github.com/Lrucka/Youtube_downloader_Django.git
    ```

2. Vytvořte a aktivujte virtuální prostředí:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Nainstalujte potřebné balíčky:
    ```bash
    pip install -r requirements.txt
    ```

## Spuštění aplikace

1. Proveďte migrace databáze:
    ```bash
    python manage.py migrate
    ```

2. Spusťte Django server:
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

3. Otevřete webový prohlížeč a navštivte `http://localhost:8000`.

## Použití

1. Do formuláře na hlavní stránce zadejte URL videa z YouTube.
2. Klikněte na tlačítko "Stáhnout".
3. Soubor MP3 bude převeden a nabídnut ke stažení přímo na vaše zařízení.

## Problémy

Pokud narazíte na jakékoli problémy nebo chyby, prosím, otevřete nový issue v tomto repozitáři nebo kontaktujte Lukáš Ručka na emailu [rucka@it-rucka.eu].

## Přispívání

Přispívání do tohoto projektu je vítáno. Otevřete prosím pull requesty s podrobnými popisy změn.

## Licence

Tento projekt je licencován pod MIT licencí. Viz [LICENSE](./LICENSE) pro více informací.




