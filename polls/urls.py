from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:questionnaire_id>/results/', views.results, name='results'),
    path('<int:questionnaire_id>/vote/', views.vote, name='vote'),
    path('questionnaire/', views.questionnaire_api, name='questionnaire_api'),
]