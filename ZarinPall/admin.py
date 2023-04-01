from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.ZarinPall)
class ZarinPallAdmin(admin.ModelAdmin):
    list_display = ["authority", 'amount', 'ref_id', "status"]

    fieldsets = (

        ("Information", {"fields": ("authority", 'amount', 'ref_id', "status")}),
        ("Foreign Key", {"fields": ('reserve',)}),

    )

    list_filter = ["authority", ]