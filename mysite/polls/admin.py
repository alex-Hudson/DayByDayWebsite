from django.contrib import admin

from .models import Choice, Question, Series
import nested_admin



class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 1

class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]

class SeriesAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        (None,               {'fields': ['series_title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [QuestionInline]
    list_display = ('series_title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['series_title']

admin.site.register(Series, SeriesAdmin)
