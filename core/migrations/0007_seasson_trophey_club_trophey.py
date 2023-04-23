# Generated by Django 4.1.7 on 2023-04-23 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_question_subject_test_useranswer_testresult_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seasson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chempionat', models.IntegerField()),
                ('kubok', models.CharField(choices=[('1/8', '1/8'), ('1/4', '1/4'), ('1/2', '1/2'), ('champion', 'champion')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Trophey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seasson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.seasson')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='trophey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.trophey'),
        ),
    ]