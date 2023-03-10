# Generated by Django 4.1.7 on 2023-03-11 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(verbose_name='Время гола')),
                ('goal_point', models.IntegerField(blank=True, null=True)),
                ('red_card', models.IntegerField(blank=True, null=True)),
                ('yellow_card', models.IntegerField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infomatch_game', to='core.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infomatch_player', to='core.player')),
            ],
        ),
        migrations.DeleteModel(
            name='PlayerGoal',
        ),
    ]
