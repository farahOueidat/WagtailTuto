from django.contrib import admin

# Register your models here.
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import subscribers


class SubscriberAdmin(ModelAdmin):
    """Subscriber admin"""
    model = subscribers
    menu_label = "Subscribers"
    menu_icon = "placeholder"
    menu_order=290
    add_to_setting_menu = False
    exclude_from_explorer = False
    list_display = ("email", "full_name",)
    Search_fields = ("email", "full_name",)

modeladmin_register(SubscriberAdmin)