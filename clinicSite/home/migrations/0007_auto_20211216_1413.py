# Generated by Django 3.2.10 on 2021-12-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211216_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepagesliderimage1',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='homepagesliderimage1',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
