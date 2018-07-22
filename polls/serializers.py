from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Questionnaire

class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    question_set = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='question_text'
    )
    class Meta:
        model = Questionnaire
        fields = ('id', 'questionnaire_name', 'detail_info', 'pub_date', 'question_set')