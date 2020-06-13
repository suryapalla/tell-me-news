from django.shortcuts import render
from . news_api import NewsApi, NewsApiEverything

# Create your views here.
def index(request):
    query = request.GET.get('search')
    if query:
        sources = 'the-times-of-india, the-telegraph, the-hindu, google-news, financial-times, al-zazeera-english, bbc-sport'
        news_obj = NewsApiEverything(query, sources)
    else:
        news_obj = NewsApi('World')
    discription = news_obj.get_description()
    url = news_obj.get_url()
    images = news_obj.get_images()
    title = news_obj.get_title()
    mylist = zip(title, discription, images, url)
    slide_list = zip(images[:3], title[:8], url[:8])
    context = {
        'mylist': mylist,
        'slide_list': slide_list,
    }
    return render(request, 'home.html',context)

def cricket_news(request):
    query = request.GET.get('search')
    if query:
        sources = 'the-times-of-india, the-telegraph, the-hindu, google-news, financial-times, al-zazeera-english, bbc-sport'
        news_obj = NewsApiEverything(query, sources)
    else:
        sources = 'espn-cric-info, fox-sports'
        news_obj = NewsApiEverything('cricket', sources)
    discription = news_obj.get_description()
    url = news_obj.get_url()
    images = news_obj.get_images()
    title = news_obj.get_title()
    mylist = zip(title, discription, images, url)
    context = {
        'mylist': mylist,
    }
    return render(request,'cricket.html',context)

def business_news(request):
    query = request.GET.get('search')
    if query:
        sources = 'the-times-of-india, the-telegraph, the-hindu, google-news, financial-times, al-zazeera-english, bbc-sport'
        news_obj = NewsApiEverything(query, sources)
    else:
        sources = 'business-insider-uk, crypto-coin-news, financial-post, financial-times, the-ecominist, the-times-of-india'
        news_obj = NewsApiEverything('currency And business', sources)
    discription = news_obj.get_description()
    url = news_obj.get_url()
    images = news_obj.get_images()
    title = news_obj.get_title()
    mylist = zip(title, discription, images, url)
    context = {
        'mylist': mylist,
    }
    return render(request,'cricket.html',context)

def progress_view(request):
    return render(request, 'progress.html')
