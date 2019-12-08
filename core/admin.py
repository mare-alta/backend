from django.contrib import admin

from .models import Level, Complaint


class LevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'desc']


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_hash', 'level']


admin.site.register(Level, LevelAdmin)
admin.site.register(Complaint, ComplaintAdmin)
