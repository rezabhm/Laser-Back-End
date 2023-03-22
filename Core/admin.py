from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "name", ]

    fieldsets = (

        ("Information", {"fields": ("username", "name", 'last_name', 'phone_number', 'user_type')}),
        ("Security Information", {"fields": ("password", )}),

    )

    list_filter = ["username", ]


@admin.register(models.Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ["token_code", "token_create_time_str", 'token_expire_time_str', 'user']

    fieldsets = (

        ("Information", {"fields": ("token_code", )}),
        ("Timing", {"fields": ("token_create_time_int", 'token_create_time_str', 'token_expire_time_int',
                               'token_expire_time_str')}),
        ("Foreign Key", {"fields": ("user",)}),

    )

    list_filter = ["token_code", ]


@admin.register(models.ForgotPassword)
class ForgotPasswordAdmin(admin.ModelAdmin):
    list_display = ["code", 'code_generate', 'user']

    fieldsets = (

        ("Information", {"fields": ("code", 'code_generate', 'proved', 'used')}),
        ("Timing", {"fields": ("expire_time",)}),
        ("Foreign Key", {"fields": ("user",)}),

    )

    list_filter = ["code", ]


@admin.register(models.EmployeeEnterExit)
class EmployeeEnterExitAdmin(admin.ModelAdmin):
    list_display = ["id", 'user']

    fieldsets = (

        ("Information", {"fields": ("id", 'exited')}),
        ("Timing", {"fields": ("enter_time_int", 'enter_time_str', 'exit_time_int', 'exit_time_str')}),
        ("Foreign Key", {"fields": ("user",)}),

    )

    list_filter = ["id", ]


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["national_code", 'address', 'house_number']

    fieldsets = (

        ("Information", {"fields": ("national_code", 'address', 'house_number')}),
        ("Medical History", {"fields": ("drug_hist", 'decease_hist', 'doctor', 'charge', 'offline_num')}),
        ("Foreign Key", {"fields": ("user",)}),

    )

    list_filter = ["national_code", ]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", 'user']

    fieldsets = (

        ("Information", {"fields": ("id", 'comment_text', 'seen')}),
        ("Timing", {"fields": ("create_time_int", 'create_time_str')}),
        ("Foreign Key", {"fields": ("user",)}),

    )

    list_filter = ["id", ]

