# Generated by Django 3.2.7 on 2021-10-05 02:14

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('imagem', stdimage.models.StdImageField(blank=True, upload_to='perfil', verbose_name='imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Sorteio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias', models.IntegerField(verbose_name='Dias')),
                ('colunas', models.IntegerField(verbose_name='Pessoas/dia')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('pessoas', models.ManyToManyField(to='app1.Pessoa')),
            ],
        ),
    ]