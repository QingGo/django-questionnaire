from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Questionnaire, VoteRecord

def capitalize_choice(modeladmin, request, queryset):
    print(modeladmin, request, queryset)
    for choice in queryset:
        choice.choice_text = choice.choice_text.capitalize()
        choice.save()
        
capitalize_choice.short_description = "Make the fisrt letter of every word uppercase"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'choice_text', 'votes')
    actions = [capitalize_choice]

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
admin.site.register(VoteRecord)