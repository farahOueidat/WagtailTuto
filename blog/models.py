from django.db import models

# Create your models here.
from streams import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django.shortcuts import render
from wagtail.snippets.models import register_snippet
class BlogAuthor(models.Model):
    """Blog author for snippets,"""
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    image = models.ForeignKey("wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=False,
                              related_name='+', )
    panels = [
        MultiFieldPanel([
            FieldPanel("name"),
            ImageChooserPanel("image"),
        ],
            heading="Name and Image"
        ),
        MultiFieldPanel([
            FieldPanel("website"),
        ],
            heading="Links"
        ),
    ]

    def __str__(self):
        """String repr of this class"""
        return self.name

    class Meta:
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"


register_snippet(BlogAuthor)


class BlogListingPage(RoutablePageMixin, Page):
    # getting all the blogdetailpages and putting it into it
    # Listing all page detail
    template = "blog/blog_Listing_page.html"
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text='Overrite the default title',
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        "Ading custim stuff to our context."
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()
        return context

    @route(r'^latest/$', name="latest_blog_posts")
    def latest_blog_posts_Only_5(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        # dispay only one post
        context["posts"] = context["posts"][:1]
        context["latest_posts"] = BlogDetailPage.objects.live().public()[:1]
        return render(request, "blog/latest_post.html", context)

    # add the latest page to the sitemap:
    def get_sitemap_urls(self, request):
        # to ha no sitemap for this page
        # return []
        sitemap = super().get_sitemap_urls(request)
        sitemap.append(
            {
                "location": self.full_url + self.reverse_subpage("latest_blog_posts"),
                "lastmod": (self.last_published_at or self.latest_revision_created_at),
                "priority": 0.9,
            }
        )
        return sitemap


class BlogDetailPage(Page):
    template = "blog/blog_detail_page.html"
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title'
    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL
    )
    content = StreamField([
        ('title_and_text', blocks.TitleAndBlock()),
        ('full_richtext', blocks.RichtextBlock()),
        ('simple_richtext', blocks.SimpleRichtextBlock()),
        ('cards', blocks.CardBlock()),
        ('cta', blocks.CTABlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content")
    ]
