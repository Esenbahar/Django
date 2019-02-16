from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Author
from django.http import Http404
# Create your views here.

#Kullanıcı request gönderir yani bir istek gönderir bu istekleri burada gerçekleştireceğiz.bunun için kütüphane ekleriz.
#from django.http import HttpResponse


def index(request):
    return HttpResponse("Anasayfa")  #index sayfasına bir request istek gelirse yanıt olarak Anasayfa dönsün.
#şimdi indexi kabul eetiğimizi belirttiğimiz bir url e ihtiyacımız var.bunun için urls.py dosyası oluştururuz.
def authors(request):
    template = loader.get_template('authors.html')
    context = {
        'authors_list' : Author.objects.all()
    }
    return  HttpResponse(template.render(context,request))
def books(request):
    return  HttpResponse("Kitaplar")    

def authorDetails(request,authorId ):
    try :
            context = {
                'author_detail' : Author.objects.get(pk=authorId)
            }
    except Author.DoesNotExist:
        raise Http404("Yazar bulunamadı")
    template = loader.get_template('authorDetail.html')
    return  HttpResponse(template.render(context,request))
