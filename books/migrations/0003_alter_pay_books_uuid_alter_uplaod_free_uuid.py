# Generated by Django 4.2.4 on 2023-08-31 23:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_pay_books_uuid_alter_uplaod_free_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay_books',
            name='uuid',
            field=models.CharField(default=uuid.UUID('19b04f58-4855-11ee-a160-3c970e3383cc'), max_length=200),
        ),
        migrations.AlterField(
            model_name='uplaod_free',
            name='uuid',
            field=models.CharField(default=uuid.UUID('19b0284f-4855-11ee-b21e-3c970e3383cc'), max_length=200),
        ),
    ]
