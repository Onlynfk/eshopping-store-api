# Generated by Django 3.2.9 on 2022-08-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_orderitem_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]