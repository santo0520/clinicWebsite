# Generated by Django 3.2.10 on 2021-12-16 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepagesliderimage1'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepagesliderimage1',
            options={},
        ),
        migrations.RemoveField(
            model_name='homepagesliderimage1',
            name='sort_order',
        ),
    ]
