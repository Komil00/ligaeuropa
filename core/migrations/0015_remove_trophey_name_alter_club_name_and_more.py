# Generated by Django 4.1.7 on 2023-04-26 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_year_alter_club_name_alter_trophey_name_seazon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trophey',
            name='name',
        ),
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name='Клуб'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='club',
            name='trophey',
        ),
        migrations.DeleteModel(
            name='Seazon',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
        migrations.AddField(
            model_name='club',
            name='trophey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.trophey'),
        ),
    ]