from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^register', views.register),
  url(r'^login', views.login),
  url(r'^dashboard', views.dashboard),
  url(r'^logout', views.logout),
  url(r'^add_quote', views.add_quote),
  url(r'^remove_quote/(?P<quote_id>\d+)$', views.remove_quote),
  url(r'^add_fav/(?P<quote_id>\d+)$', views.add_fav),
  url(r'^user_quotes/(?P<user_id>\d+)$', views.user_quotes),
]