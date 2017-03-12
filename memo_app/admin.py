from django.contrib import admin
# Register your models here.
from memo_app.models import Memos

class MemosAdmin(admin.ModelAdmin):
    list_display = ('name_id', 'title', 'update_date')
    search_fields = ['text']


admin.site.register(Memos, MemosAdmin)
