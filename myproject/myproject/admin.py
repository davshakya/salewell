from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "interest", "created_at")
    search_fields = ("name", "email", "message")
    list_filter = ("interest", "created_at")
    ordering = ("-created_at",)
