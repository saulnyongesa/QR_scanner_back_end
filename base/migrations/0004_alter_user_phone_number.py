# Generated by Django 5.0.4 on 2024-04-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_paybill_qrcodeforbuygoods_qrcodeforpaybill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(max_length=14, null=True, unique=True),
        ),
    ]