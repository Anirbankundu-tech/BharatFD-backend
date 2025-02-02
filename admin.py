from django.contrib import admin
from .Models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'language')
    search_fields = ('question',)