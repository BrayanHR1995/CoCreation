from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^signup', RegistroEmprendimiento.as_view(), name="signup"),
]