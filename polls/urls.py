from django.urls import path, include
from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^register/$', views.register, name='register'),
    path('', views.index, name='index'),
   ]

# urlpatterns = patterns('',
#     url(r'^register/$', views.RegisterFormView.as_view()),
# )