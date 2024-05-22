from django.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.IndexView.as_view(), name='index'),
    path(r'^(?P<pk>[-\w]+)/$', views.PageDetailView.as_view(), name='page_detail'),
]
