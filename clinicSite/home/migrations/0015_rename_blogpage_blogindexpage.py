# Generated by Django 3.2.10 on 2021-12-23 13:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0014_radiopage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPage',
            new_name='BlogIndexPage',
        ),
    ]
