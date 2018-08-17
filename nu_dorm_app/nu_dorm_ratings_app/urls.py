from django.conf.urls import url

from . import views


app_name = 'nu_dorm_ratings_app'
urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<dorm_id>[0-9]+)/dorm/$', views.dorm, name='dorm'),
    url(r'^rate/(?P<dorm_id>[0-9]+)/$', views.rate, name='rate'),
    url(r'^submit_rating/(?P<dorm_id>[0-9]+)/$', views.submit_rating, name='submit_rating'),
    url(r'^results/$', views.results, name='results'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout')
]
