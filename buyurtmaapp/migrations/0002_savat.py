# Generated by Django 4.1.2 on 2022-10-26 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiyapp', '0003_alter_rasm_mahsulot'),
        ('userapp', '0001_initial'),
        ('buyurtmaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveSmallIntegerField(default=1)),
                ('umumiy', models.PositiveIntegerField()),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiyapp.mahsulot')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
            ],
        ),
    ]
