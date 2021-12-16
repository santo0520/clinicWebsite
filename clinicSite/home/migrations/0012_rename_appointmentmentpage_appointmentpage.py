# Generated by Django 3.2.10 on 2021-12-16 10:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('home', '0011_appointmentmentpage_blogpage_contactpage_departmentspage_doctorspage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppointmentmentPage',
            new_name='AppointmentPage',
        ),
    ]
