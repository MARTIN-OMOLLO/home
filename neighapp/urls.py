from django.conf.urls import include,url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'register/', views.register, name='registration'),
    url(r'login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'profile/', views.profile, name='profile'),
    url(r'createHood/', views.create_neighbourhood, name='createHood'),
    url(r'joinhood/', views.join_neighbourhood, name='joinhood'),
    url(r'leavehood/<id>/', views.leave_neighbourhood, name='leavehood'),
    url(r'singleHood/<hood_id>/', views.single_neighbourhood, name='singleHood'),
    url(r'<hood_id>/post/', views.create_post, name='post'),
    url(r'<hood_id>/business/', views.add_business, name='business'),
    url(r'^searchbusiness/', views.search_business, name='search'),

]