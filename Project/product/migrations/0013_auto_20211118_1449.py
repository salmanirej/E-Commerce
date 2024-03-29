# Generated by Django 3.2.8 on 2021-11-18 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20211113_2104'),
        ('product', '0012_auto_20211117_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDname',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
    ]
