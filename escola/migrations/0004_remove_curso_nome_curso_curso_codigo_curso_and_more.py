# Generated by Django 5.0.4 on 2024-04-06 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_remove_curso_codigo_curso_curso_nome_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='nome_curso',
        ),
        migrations.AddField(
            model_name='curso',
            name='codigo_curso',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]
