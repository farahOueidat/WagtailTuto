from django.db import models
from modelcluster.fields import ParentalKey
from django.shortcuts import render
from wagtail.core.fields import StreamField
from wagtail.core.models import Page,Orderable
from wagtail.admin.edit_handlers import FieldPanel, RichTextField, PageChooserPanel, StreamFieldPanel, InlinePanel, \
    MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import  RoutablePageMixin, route
from streams import blocks


class HomePageCarrouselImages(Orderable):
    """Between 1 and 5 images for the home page carrousel"""
    page = ParentalKey("home.HomePage", related_name="carousel_images" )
    carousel = models.ForeignKey(
            'wagtailimages.Image',
            on_delete = models.SET_NULL,
            related_name = '+',
            null=True,
            blank=False
        )
    panels = [
        ImageChooserPanel("carousel"),
    ]



class HomePage(RoutablePageMixin, Page):
    #refer this model to a template
    templates = "home/home_page.html"
    #limit the home page count
    max_count=1
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(blank=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete = models.SET_NULL,
        related_name = '+',
        null=True,
        blank=False
    )

    banner_cta = models.ForeignKey(
        'wagtailcore.page',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True ,
        blank=True
    )

    content = StreamField([
        ('cta', blocks.CTABlock()),
    ], null=True, blank=True)

    #add the new model to the admin form
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cta"),
        ], heading="Banner Options"),
        StreamFieldPanel("content"),
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=5, min_num=1, label="Image"),
        ],heading="Carousel Image")
    ]
   # class Meta:
        #change the name in the admin interface
       # verbose_name = "Home Page"


    #routin override the route
    @route(r'^subscribe/$')
    def the_subscribe_page(self, request, *args, **kwargs):
        context=self.get_context(request, *args, **kwargs)
        context['a_special_test']="Hello word 123123"
        return render(request, "home/subscribe.html", context)
    pass