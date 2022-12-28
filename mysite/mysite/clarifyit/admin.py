from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created")
    list_filter = ("author", "created")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "created"
    ordering = (
        "author",
        "created",
    )
