# Generated by Django 4.2.3 on 2023-12-31 17:56

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_address_mobile2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residence',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='This is the Redidence', null=True),
        ),
    ]
