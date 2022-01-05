""" Flexible page"""
import wagtail.admin.edit_handlers
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel

from streams import blocks


class FlexPage(Page):
        """flexible page class"""
        template = "flex/flex_page.html"

        subtitle = models.CharField(max_length=100, null=True, blank=True )
        content = StreamField([
            ('title_and_text', blocks.TitleAndBlock()),
            ('full_richtext', blocks.RichtextBlock()),
            ('simple_richtext', blocks.SimpleRichtextBlock()),
            ('cards', blocks.CardBlock()),
            ('cta', blocks.CTABlock()),
            ('button', blocks.ButtonBlock()),
        ],null = True, blank = True)

        content_panels = Page.content_panels + [
                FieldPanel("subtitle"),
            StreamFieldPanel("content")
        ]
        class Meta:
               verbose_name = "Flex Page"
               verbose_name_plural = "Flex Pages"
