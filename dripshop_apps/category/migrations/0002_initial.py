# Generated by Django 4.2.4 on 2023-12-27 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='featured_products',
            field=models.ManyToManyField(blank=True, related_name='category_featured_products', to='product.product', verbose_name='Featured Products'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories', to='category.category'),
        ),
    ]
