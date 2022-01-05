# Generated by Django 3.2.10 on 2022-01-03 11:40

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_banner_cta'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add your title', max_length=40, required=True)), ('button_url', wagtail.core.blocks.URLBlock(required=False))]))], blank=True, null=True),
        ),
    ]
