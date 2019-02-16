
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name='index'), # anasayfaya istek gelirse indexi aç.
   #buradan sonra ana url de bunları işle. 
    path('books',views.books, name='books'),
    path('authors',views.authors, name='authors'),
    path('authordetails/<int:authorId>',views.authorDetails, name='authordetails')

]