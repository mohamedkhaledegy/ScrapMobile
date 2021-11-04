from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as soup
import lxml
import re

# Create your views here.

def index(request):
    url = 'https://www.olx.com.eg/en/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    s = requests.Session()
    s.headers.update(headers)

    r = s.get(url)
    return render(request,'index.html',{'new':'new'})