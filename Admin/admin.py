from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.OperatorProgram)
class OperatorProgramAdmin(admin.ModelAdmin):
    list_display = ["id", "date_str", ]

    fieldsets = (

        ("information", {"fields": ("id", "date_int", 'date_str', 'program_turn', 'operator_name', 'operator')}),

    )

    list_filter = ["id", ]


@admin.register(models.CancelTime)
class CancelTimeAdmin(admin.ModelAdmin):
    list_display = ["id", "start_time_str", 'end_time_str']

    fieldsets = (

        ("information", {"fields": ("id", "start_time_int", 'start_time_str', 'end_time_str', 'end_time_int')}),

    )

    list_filter = ["id", ]
