# Generated by Django 2.2.3 on 2019-08-14 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190813_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cart',
            new_name='carts',
        ),
    ]
