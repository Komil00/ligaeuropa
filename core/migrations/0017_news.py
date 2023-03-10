# Generated by Django 3.2 on 2023-03-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_matches_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/images/')),
                ('title', models.CharField(max_length=500)),
                ('info', models.TextField()),
                ('interview_author', models.CharField(max_length=300)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
