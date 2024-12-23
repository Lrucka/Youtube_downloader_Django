from django import forms

class DownloadForm(forms.Form):
    video_url = forms.URLField(label='URL videa z YouTube')
