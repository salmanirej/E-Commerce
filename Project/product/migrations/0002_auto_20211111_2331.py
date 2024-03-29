# Generated by Django 3.2.8 on 2021-11-11 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDcost',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prodtuct Cost'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDcreated',
            field=models.DateTimeField(verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDdesc',
            field=models.TextField(verbose_name='Prodtuct Descrption'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDname',
            field=models.CharField(max_length=100, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDprice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prodtuct Price'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='product/', verbose_name='Image')),
                ('PRDIProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product')),
            ],
        ),
    ]
