from django.contrib import admin
from.models import Message

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at')  # Specify fields to display in the list view

admin.site.register(Message, MessageAdmin)