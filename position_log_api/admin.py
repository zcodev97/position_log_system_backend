from django.contrib import admin

from .models import CheckIn,CheckOut,Session,User,Position,UserType,CustomUser


@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CheckIn._meta.fields]

@admin.register(CheckOut)
class CheckOutAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CheckOut._meta.fields]

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Session._meta.fields]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Position._meta.fields]


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserType._meta.fields]

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]

