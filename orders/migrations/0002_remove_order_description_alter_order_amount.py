# Generated by Django 4.2.5 on 2023-09-12 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
