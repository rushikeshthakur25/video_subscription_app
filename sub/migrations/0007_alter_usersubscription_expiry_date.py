# Generated by Django 4.0.1 on 2023-08-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0006_usersubscription_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='expiry_date',
            field=models.DateTimeField(verbose_name=True),
        ),
    ]
