from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
# configration the ia
from internetarchive import configure
configure('bookhope.com@gmail.com', 'Hamza@2020') 
from internetarchive import get_files


# Create your views here.
def get_data(request):
    # Initialize an empty list to store item IDs
    item_ids = []
    # Specify the path to the text file containing item IDs
    file_path = 'item_ids.txt'
    # Open the file and read item IDs line by line
    with open(file_path, 'r') as file:
        for line in file:
            item_id = line.strip()  # Remove leading/trailing whitespace and newline characters
            item_ids.append(item_id)
            
            fnames  = get_files(identifier='2_20201027' )
    
    
    
    
    
    return HttpResponse('<a href="https://archive.org/download/<identifier>/<filename>">dokwnload</a>')
