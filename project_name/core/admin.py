from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site
from .models import Contact, User
from .forms import UserCreationAdminForm


class UserCustomAdmin(UserAdmin):
    """
    User CMS. We need to change the add form because we use out custom User model.
    """
    add_form = UserCreationAdminForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Lainnya'), {'fields': ('role', 'gender', 'facebook', 'twitter', 'about_me')}),
    )


class ContactAdmin(admin.ModelAdmin):
    model = Contact

    list_display = ['name', 'address', 'telephone', 'email', 'message']

    search_fields = ['name', 'email', 'message']

admin.site.register(User, UserCustomAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Site)
