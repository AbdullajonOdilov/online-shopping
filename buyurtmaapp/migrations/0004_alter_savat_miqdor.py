# Generated by Django 4.1.2 on 2022-10-26 05:36

import buyurtmaapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtmaapp', '0003_alter_savat_miqdor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savat',
            name='miqdor',
            field=models.PositiveIntegerField(default=1, validators=[buyurtmaapp.models.validate_miqdor]),
        ),
    ]
