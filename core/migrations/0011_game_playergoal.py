# Generated by Django 3.2 on 2023-03-08 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20230309_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_point', models.PositiveSmallIntegerField(default=0, verbose_name='Счет хозяев')),
                ('guest_point', models.PositiveSmallIntegerField(default=0, verbose_name='Счет гостей')),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('home_red_card', models.PositiveSmallIntegerField(default=0)),
                ('guest_red_card', models.PositiveSmallIntegerField(default=0)),
                ('home_yellow_card', models.PositiveSmallIntegerField(default=0)),
                ('guest_yellow_card', models.PositiveSmallIntegerField(default=0)),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='core.tour')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Имя игрока')),
                ('time', models.PositiveSmallIntegerField(default=0, verbose_name='Время гола')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.game')),
            ],
        ),
    ]
