# Generated by Django 2.1.5 on 2020-11-14 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListaDeTarefas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('data', models.DateField()),
            ],
        ),
    ]
