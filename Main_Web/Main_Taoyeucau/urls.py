from django.conf.urls import url
from Main_Taoyeucau import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

    url(r'^yeucaucanduyet.html$',views.yeucauApi),
]