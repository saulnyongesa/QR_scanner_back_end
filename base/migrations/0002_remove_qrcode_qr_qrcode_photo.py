# Generated by Django 5.0.4 on 2024-04-27 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcode',
            name='qr',
        ),
        migrations.AddField(
            model_name='qrcode',
            name='photo',
            field=models.ImageField(null=True, upload_to='qr_codes/'),
        ),
    ]
