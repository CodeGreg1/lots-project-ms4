# Generated by Django 4.1.5 on 2023-03-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_order_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.AlterField(
            model_name='order',
            name='membership_num',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
