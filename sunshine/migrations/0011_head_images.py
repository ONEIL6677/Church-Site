# Generated by Django 2.0 on 2019-11-13 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunshine', '0010_remove_head_pastor'),
    ]

    operations = [
        migrations.AddField(
            model_name='head',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
