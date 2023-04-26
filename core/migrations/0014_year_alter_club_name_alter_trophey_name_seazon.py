# Generated by Django 4.1.7 on 2023-04-25 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_trophey_name_remove_club_trophey_club_trophey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Клуб'),
        ),
        migrations.AlterField(
            model_name='trophey',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Seazon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.year')),
            ],
        ),
    ]
