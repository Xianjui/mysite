from django.contrib import admin

from .models import Question, Choice

# Register your models here.

# admin.site.register(Question)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
