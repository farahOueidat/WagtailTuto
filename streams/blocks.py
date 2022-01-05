from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndBlock(blocks.StructBlock):
    """ title and text nothing else"""
    title = blocks.CharBlock(required=True, help_text='add your title')
    text = blocks.TextBlock(required=True, help_text='add additional text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Represent the cards block list of staff"""
    title = blocks.CharBlock(required=True, help_text='add your title')
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=True)),
            ("title", blocks.CharBlock(required=True, max_length=40)),
            ("text", blocks.RichTextBlock(required=True)),
            ("button_page", blocks.PageChooserBlock(required=False)),
            ("button_url", blocks.URLBlock(required=False))
        ])
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "staff cards"


class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='add your title',max_length=40)
    text = blocks.RichTextBlock(required=True),
    button_page = blocks.PageChooserBlock(required=False),
    button_url = blocks.URLBlock(required=False)

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "call to action"


class RichtextBlock(blocks.RichTextBlock):
    """ rich text with all the features """

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """ rich text without (Limited) all the features """
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"

class LinkStructValue(blocks.StructValue):
    """Additional Logic for our url"""
    def url(self):
        button_page=self.get('button_page')
        button_url=self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url

        return None

   # def latest_posts(self):
        #return  BlogDetailPage.objects.live().public()[:3]

class ButtonBlock(blocks.StructBlock):
    """An external or internal url"""
    button_page = blocks.PageChooserBlock(required=False, help_text='if selected, this url will be used first')
    button_url = blocks.URLBlock(required=False,
                                 help_text='if added, this url will be used secondarily to the button page')

  #  def get_context(self, request, *args, **kwargs):
     #   context = super().get_context(request, *args, **kwargs)
     #   context['latest_posts'] = BlogDetailPage.objects.live().public()[:3]
       # return context

    class Meta:
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Single Button"
        value_class=LinkStructValue




