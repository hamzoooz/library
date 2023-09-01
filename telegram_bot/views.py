from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from telegram import Bot


# Create your views here.
def download_file(request):
    # Replace 'YOUR TOKE With Actual bot token 
    bot = Bot(token="6609369403:AAHSpWWEPSV7PG9JnTkgRpdCMML8YAb3hDs")
    file_id = "FILE_ID"
    
    # 5711019494:AAEzuTDOp53EmlSzKPi22zm0YhpwVRt7AgM
    # 6609369403:AAHSpWWEPSV7PG9JnTkgRpdCMML8YAb3hDs =
    # Get the file object from Telegram
    file = bot.get_file(file_id)
    
    # Generate a direct link for download 
    download_url = f'https://api.telegram.org/file/bot{bot.token}/{file.file_path}'
    
    # Redirect the user to the sownload URL
    return HttpResponse(f'<a href="{download_url}" >{download_url}</a>')
    
    