from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('github', views.external_url_github, name="github"),
    path('linkedin', views.external_url_linkedin, name="linkedin"),

]