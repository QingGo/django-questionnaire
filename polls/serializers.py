from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Questionnaire, Question, Choice


class QuestionnSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(max_length=200)
    class Meta:
        model = Question
        fields = ('question_text',)

class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    question_set = QuestionnSerializer(many=True, read_only=True)

    pub_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Questionnaire
        fields = ('id', 'questionnaire_name', 'detail_info', 'pub_date', 'question_set')

class ChoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text','votes')

class QuestionnDetailSerializer(serializers.ModelSerializer):
    choice_set = ChoiceDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('question_text','question_type', 'choice_set')

class QuestionnaireDetailSerializer(serializers.HyperlinkedModelSerializer):
    question_set = QuestionnDetailSerializer(many=True, read_only=True)
    pub_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Questionnaire
        fields = ('id', 'questionnaire_name', 'detail_info', 'pub_date', 'question_set')