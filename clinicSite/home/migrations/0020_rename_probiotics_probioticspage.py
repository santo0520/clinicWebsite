# Generated by Django 3.2.10 on 2022-01-05 12:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('home', '0019_ivsupplementspage_menshealthpage_probiotics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Probiotics',
            new_name='ProbioticsPage',
        ),
    ]