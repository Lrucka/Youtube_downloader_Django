#CS_verze

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



#EN_version


# Youtube_downloader_Django

## Django project - YouTube downloader

This application allows users to download videos from YouTube and convert them to MP3 directly from a web interface. The application is built on Django and uses yt-dlp for downloading and converting videos.

## Features

- Download videos from YouTube
- Convert videos to MP3
- Enter video URL via web form
- Download MP3 file directly to the user's device

## Requirements

- Python 3.6 or newer
- Django
- yt-dlp

## Installation

1. Clone this repository to your local environment:
    ```bash
    git clone https://github.com/Lrucka/Youtube_downloader_Django.git
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Run the database migrations:
    ```bash
    python manage.py migrate
    ```

2. Start the Django server:
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

3. Open a web browser and visit `http://localhost:8000`.

## Usage

1. Enter the YouTube video URL in the form on the main page.
2. Click the "Download" button.
3. The MP3 file will be converted and offered for download directly to your device.

## Issues

If you encounter any issues or errors, please open a new issue in this repository or contact Lukáš Ručka at [rucka@it-rucka.eu].

## Contributing

Contributions to this project are welcome. Please open pull requests with detailed descriptions of the changes.

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for more information.



