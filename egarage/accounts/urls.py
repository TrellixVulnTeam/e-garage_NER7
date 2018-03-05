from django.conf.urls import url

from . import views

from django.contrib.auth import  views as auth_views

#we imported the views ad auth_views to avoid clashing with .views
#we use .as_view() to mean that it's a class based view which is more flexible
#if we don't use template_name in our login url, django will assume our login.html is under the
#path registratin/login.html


urlpatterns=[
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url('^login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'))

]
