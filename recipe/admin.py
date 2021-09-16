from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class AdminForRecipe(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    # prepopulated_fields = {
    #     "slug": ("title",),
    # }


# admin.site.register(AnotherModel)
