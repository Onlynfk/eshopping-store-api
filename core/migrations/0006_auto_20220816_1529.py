# Generated by Django 3.2.9 on 2022-08-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_product_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
