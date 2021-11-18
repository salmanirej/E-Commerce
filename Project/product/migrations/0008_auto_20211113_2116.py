# Generated by Django 3.2.9 on 2021-11-13 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20211113_2104'),
        ('product', '0007_auto_20211113_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='PRDCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
