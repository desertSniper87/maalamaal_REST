# Generated by Django 2.2.3 on 2019-08-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20190811_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
