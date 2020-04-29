# Generated by Django 3.0.4 on 2020-04-28 19:23

import BlogSite.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogSite', '0003_auto_20200428_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_1',
            field=models.FileField(upload_to='uploads/', validators=[BlogSite.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_2',
            field=models.FileField(upload_to='uploads/', validators=[BlogSite.validators.validate_file_extension]),
        ),
    ]