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
