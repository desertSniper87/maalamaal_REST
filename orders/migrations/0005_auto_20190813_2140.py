# Generated by Django 2.2.3 on 2019-08-13 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190812_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(blank=True, to='carts.Cart'),
        ),
    ]