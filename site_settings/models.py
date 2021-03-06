from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting

"""decorator"""
@register_setting
class SocialMediaSettings (BaseSetting):
    """Social media settings for our custom website"""

    facebook= models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, null=True, help_text="Youtube URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube")
        ], heading="Social Media Settings")
    ]