# Generated by Django 4.0.1 on 2023-08-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0009_remove_usersubscription_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='expiry_date',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
