# Generated by Django 4.0.1 on 2023-08-05 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0005_usersubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='expiry_date',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
