from django.urls import path
from .views import home,doctor

app_name='tss1'
urlpatterns=[
    path('',home,name="home"),
    path('doctor/',doctor,name="doctor")
]