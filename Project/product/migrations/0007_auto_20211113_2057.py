# Generated by Django 3.2.9 on 2021-11-13 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_accessories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATMain_Category',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Main category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATimg',
            field=models.ImageField(upload_to='category/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CAtDesc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product_accessories',
            name='PACCAccessories',
            field=models.ManyToManyField(related_name='Accessories_Product', to='product.Product', verbose_name='Accessories'),
        ),
        migrations.AlterField(
            model_name='product_accessories',
            name='PACCProducte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MainAccessories_Product', to='product.product', verbose_name='Producte'),
        ),
        migrations.AlterField(
            model_name='product_alterative',
            name='PALNProducte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Main_Product', to='product.product', verbose_name='Producte'),
        ),
        migrations.AlterField(
            model_name='product_alterative',
            name='PLANAlterative',
            field=models.ManyToManyField(related_name='Alterative_Product', to='product.Product', verbose_name='Alterative'),
        ),
    ]
