from django.urls import path
from basicapp import views


urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
]
