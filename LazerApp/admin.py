from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.LaserArea)
class LaserAreaAdmin(admin.ModelAdmin):
    list_display = ["name"]

    fieldsets = (

        ("Information", {"fields": ("name", 'operate_time', 'deadline_reset')}),


    )

    list_filter = ["name", ]


@admin.register(models.LaserAreaInformation)
class LaserAreaInformationAdmin(admin.ModelAdmin):
    list_display = ["id", 'laser']

    fieldsets = (

        ("Information", {"fields": ("id", 'price')}),
        ("Timing", {"fields": ("start_time_int", 'start_time_str', 'end_time_int',
                               'end_time_str')}),
        ("Foreign Key", {"fields": ("laser",)}),

    )

    list_filter = ["id", ]
