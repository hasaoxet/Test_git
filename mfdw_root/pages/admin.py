from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title','update_date')
    search_fields=('title','bodytext')

admin.site.register(Page,PageAdmin)
