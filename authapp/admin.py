from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authapp.models import ShopUser
# Register your models here.


@admin.register(ShopUser)
class ShopUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'in_groups',
    )
    model = ShopUser
    fieldsets = UserAdmin.fieldsets + (
        (
            'Extra', {
                'fields': ('avatar', 'age', 'phone')
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Extra', {
                'classes': ('wide',),
                'fields': ('avatar', 'age', 'phone')
            }
        ),
    )

    def in_groups(self, obj):
        return '\n'.join([g.name for g in obj.groups.all()])

    in_groups.short_description = 'Groups'
