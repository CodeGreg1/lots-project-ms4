# Generated by Django 4.1.5 on 2023-03-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_remove_order_country_alter_order_membership_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='membership_num',
            field=models.CharField(max_length=20),
        ),
    ]