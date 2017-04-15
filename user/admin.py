from django.contrib import admin
from .models import User, Address
from django.contrib.auth.admin import UserAdmin

class AddressInline(admin.StackedInline):
    fields = ('name', 'address')
    model = Address
    extra = 1

class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('gender', 'avatar')}),
    )
    inlines = (AddressInline,)

admin.site.register(User, MyUserAdmin)
