from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def home(request):
    return render(request, 'movie/home.html')

def search(request, query: str =""):
    if not query:
        return render(request, 'movie/search.html')
    url = "https://api.themoviedb.org/3/movie/550?api_key={api_key}&callback=test" % query
    resp = requests.get(url).json()
    if not resp:
        return render(request, 'movie/search.html', {'query': query})
    else:
        for each in resp:
            if each["show"]["summary"]:
                each["show"]["summary"] = BeautifulSoup(each["show"]["summary"], "lxml").text
            if not each["show"]["image"]:
                each["show"]["image"] = {"original":"/static/movie/tv/default.png"}

        context = {
            'results' : resp,
            'query' : query
        }
        return render(request, 'movie/search.html', context)
