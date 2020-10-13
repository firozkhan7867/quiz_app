from django.contrib import admin

# Register your models here.
from .models import Questions

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id','Question_var','answer', 'answer_no')
    list_display_links = ('id','Question_var')
    list_filter = ('answer_no',)

admin.site.register(Questions,QuestionsAdmin)
