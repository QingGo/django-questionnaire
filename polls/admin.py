from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Questionnaire


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'choice_text', 'votes')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('questionnaire_id', 'question_text')
    fieldsets = [
        (None, {'fields': ['questionnaire', 'question_text']}),
    ]
    inlines = [ChoiceInline]

class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('questionnaire_name', 'detail_info', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    fieldsets = [
        (None, {'fields': ['questionnaire_name', 'detail_info']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [QuestionInline]



admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)