# Generated by Django 3.0.4 on 2020-04-22 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20200422_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'permissions': [('can_write_blog', 'can_annihilate_blog')]},
        ),
    ]