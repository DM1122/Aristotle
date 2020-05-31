# Generated by Django 3.0.6 on 2020-05-31 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0005_auto_20200530_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.TextField()),
                ('timestamp', models.IntegerField(default=0)),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
                ('key', models.IntegerField(max_length=1)),
                ('option1_redirect', models.URLField()),
                ('option2_redirect', models.URLField()),
                ('option3_redirect', models.URLField()),
                ('option4_redirect', models.URLField()),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Video')),
            ],
        ),
    ]
