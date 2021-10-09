from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email')


@admin.register(Company)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', )


@admin.register(Application)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', )


@admin.register(Tag)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', )


@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', )


@admin.register(Dataset)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', )


@admin.register(Role)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', )