from django.db import models

# Create your models here.

class Author(models.Model):

    def __str__(self):
        return self.name # ben obje olarak istemiyorum direk olarak yazarın ismini istiyorum demiiş oluyoruz.


    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created')

  # bu yazar tablosunu oluşturdum. bunu veritabanına aktarmak istiyorum.
  #settings.py de Installed_APSS e ekleriz.  'books.apps.BooksConfig' yazarak.

class Book(models.Model):
    def __str__(self):
        return self.name # ben obje olarak istemiyorum direk olarak yazarın ismini istiyorum demiiş oluyoruz.
        
    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created')
    author = models.ForeignKey(Author,on_delete = models.CASCADE) #Olurda bir yazar silinirse o yazarın bütün kütaplarıda veritabanından silinsin.
    price = models.DecimalField(decimal_places=2, max_digits=4, null=True)
 # burada yazar ile kitap arasında bire çok ilişkisi söz konusu.
    