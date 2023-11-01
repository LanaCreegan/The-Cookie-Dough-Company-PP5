from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'created_on',
        'body',
    )

    ordering = ('-created_on',)
    list_filter = ('product',)


admin.site.register(Review, ReviewAdmin)