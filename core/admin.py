from django.contrib import admin

from .models import *


class LevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'desc']


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_hash', 'level']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'complaint', 'verified', 'insert_date']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'complaint', 'appropriate', 'insert_date']


admin.site.register(Level, LevelAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Image, ImageAdmin)
