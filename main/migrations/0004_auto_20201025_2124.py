# Generated by Django 3.1.2 on 2020-10-26 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201025_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='text',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
