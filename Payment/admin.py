from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["id", 'user', 'price']

    fieldsets = (

        ("Information", {"fields": ("id", 'price', 'payment_type')}),
        ("Timing", {"fields": ("payment_time_int", 'payment_time_str')}),
        ("Foreign Key", {"fields": ("user", 'reserve')}),

    )

    list_filter = ["id", ]


@admin.register(models.OffCode)
class OffCodeAdmin(admin.ModelAdmin):
    list_display = ["code", 'amount', 'used']

    fieldsets = (

        ("Information", {"fields": ("code", 'amount', 'used')}),

    )

    list_filter = ["code", ]
