# Generated by Django 3.2 on 2023-03-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_team_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='numb',
            field=models.PositiveSmallIntegerField(verbose_name='Номер игрока'),
        ),
    ]
