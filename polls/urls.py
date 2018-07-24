from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'questionnaires', views.QuestionnaireViewSet, base_name="quertionnaire")

app_name = 'polls'
urlpatterns = [
    # API for VUE pages
    path('api/', include(router.urls)),
    # django templates pages
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:questionnaire_id>/results/', views.results, name='results'),
    path('<int:questionnaire_id>/vote/', views.vote, name='vote'),
]