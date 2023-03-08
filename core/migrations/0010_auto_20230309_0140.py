# Generated by Django 3.2 on 2023-03-08 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20230306_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playergoal',
            name='game',
        ),
        migrations.AddField(
            model_name='player',
            name='dislike',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='like',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='PlayerGoal',
        ),
    ]
