from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ["id", 'user', 'laser_area', "total_price_amount", 'total_payment_amount']

    fieldsets = (

        ("Information", {"fields": ("id", 'session_number', 'reserve_type')}),
        ("Status", {"fields": ("online_reserve", 'charge', 'payed', 'used_off_code')}),
        ("Price", {"fields": ("total_price_amount", 'total_payment_amount')}),
        ("Timing", {"fields": ("reserve_time_int", 'reserve_time_str', 'request_time_int', 'request_time_str')}),
        ("Foreign Key", {"fields": ("user", 'laser_area', 'laser_area_list', 'laser_area_name', 'off_code', 'time_range')}),

    )

    list_filter = ["id", ]


@admin.register(models.PreReserve)
class PreReserveAdmin(admin.ModelAdmin):
    list_display = ["id", 'reserve_num', 'last_date']

    fieldsets = (

        ("Information", {"fields": ("id", 'reserve_num', 'last_date')}),
        ("Foreign Key", {"fields": ("user", 'laser_area')}),

    )

    list_filter = ["id", ]


@admin.register(models.ReserveSchedule)
class ReserveScheduleAdmin(admin.ModelAdmin):
    list_display = ["id", 'date', 'date_type', "time_range", 'total_reserve_time']

    fieldsets = (

        ("Information", {"fields": ("id",)}),
        ("Price", {"fields": ("total_reserve_time",)}),
        ("Timing", {"fields": ("date", 'date_type', 'time_range',)}),
        ("Foreign Key", {"fields": ("operator",)}),

    )

    list_filter = ["id", ]
