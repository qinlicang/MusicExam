from django.contrib import admin
from exam.models import Paper

class PaperAdmin(admin.ModelAdmin):
    list_display = ('paper_id', 'name', 'count')

admin.site.register(Paper, PaperAdmin)
# admin.site.register(Article)