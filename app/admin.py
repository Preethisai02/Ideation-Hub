from django.contrib import admin
from .models import Entry1
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'attachment','author')  # Display these fields in the list view
    list_filter = ('title',)  # Add a filter based on 'created_at' field
    search_fields = ('title', 'description',)  # Enable searching by name and email
admin.site.register(Entry1,MyModelAdmin)