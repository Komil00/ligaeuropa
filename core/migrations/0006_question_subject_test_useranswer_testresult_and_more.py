# Generated by Django 4.1.7 on 2023-04-09 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_remove_player_dislike_alter_player_club_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Question text')),
                ('question_number', models.PositiveIntegerField(verbose_name='Question number')),
                ('opt1', models.CharField(max_length=255, verbose_name='Option 1')),
                ('opt2', models.CharField(max_length=255, verbose_name='Option 2')),
                ('opt3', models.CharField(max_length=255, verbose_name='Option 3')),
                ('opt4', models.CharField(max_length=255, verbose_name='Option 4')),
                ('correct_answer', models.CharField(choices=[('opt1', 'Option 1'), ('opt2', 'Option 2'), ('opt3', 'Option 3'), ('opt4', 'Option 4')], max_length=255, verbose_name='Correct option')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ('question_number',),
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Subject name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Test name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('language', models.CharField(choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')], max_length=7, verbose_name='Language')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('opt1', 'Option 1'), ('opt2', 'Option 2'), ('opt3', 'Option 3'), ('opt4', 'Option 4')], max_length=255, verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is correct')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question', verbose_name='Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Answer',
                'verbose_name_plural': 'User Answers',
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answers', models.PositiveIntegerField(default=0, verbose_name='Correct answers')),
                ('incorrect_answers', models.PositiveIntegerField(default=0, verbose_name='Incorrect answers')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.test', verbose_name='Test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Test Result',
                'verbose_name_plural': 'Test Results',
            },
        ),
        migrations.CreateModel(
            name='TestBought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_bought', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bought_by', to='core.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Test Bought',
                'verbose_name_plural': 'Tests Bought',
            },
        ),
        migrations.AddField(
            model_name='test',
            name='bought',
            field=models.ManyToManyField(related_name='bought_tests', through='core.TestBought', to=settings.AUTH_USER_MODEL, verbose_name='Bought'),
        ),
        migrations.AddField(
            model_name='test',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject', verbose_name='Subject'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.test', verbose_name='Test'),
        ),
    ]