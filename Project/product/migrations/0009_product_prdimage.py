# Generated by Django 3.2.9 on 2021-11-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20211113_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDImage',
            field=models.ImageField(blank=True, null=True, upload_to='IMAGE', verbose_name='Image'),
        ),
    ]
