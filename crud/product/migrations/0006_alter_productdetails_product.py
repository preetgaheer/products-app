# Generated by Django 4.1.1 on 2022-09-18 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productdetails_retervails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='retervails_date', to='product.productapi'),
        ),
    ]
