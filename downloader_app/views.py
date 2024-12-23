import os
from yt_dlp import YoutubeDL
from django.shortcuts import render
from django.http import HttpResponse, Http404
from pathlib import Path
from django.views.decorators.csrf import csrf_exempt
from wsgiref.util import FileWrapper

def download_and_convert(video_url, download_folder):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url)
        file_title = ydl.prepare_filename(info_dict)
        return file_title.replace('.webm', '.mp3')

@csrf_exempt
def download_view(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')

        # Cesta k dočasné složce na serveru
        download_folder = os.path.join(Path.home(), "tmp_downloads")
        os.makedirs(download_folder, exist_ok=True)
        
        # Stahování a konverze videa
        mp3_file_path = download_and_convert(video_url, download_folder)
        
        # Odeslání souboru ke stažení uživateli
        if os.path.exists(mp3_file_path):
            with open(mp3_file_path, 'rb') as mp3_file:
                response = HttpResponse(FileWrapper(mp3_file), content_type='application/octet-stream')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(mp3_file_path)}"'
                return response
        else:
            raise Http404("Soubor nebyl nalezen.")

    return render(request, 'downloader_app/index.html')
