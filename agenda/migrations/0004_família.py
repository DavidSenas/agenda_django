# Generated by Django 3.2.8 on 2021-10-30 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_trabalho'),
    ]

    operations = [
        migrations.CreateModel(
            name='Família',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(blank=True, max_length=50)),
                ('Tipo_Parentesco', models.CharField(blank=True, max_length=50)),
                ('Telefone', models.CharField(blank=True, max_length=10)),
                ('Obs', models.TextField(blank=True)),
            ],
        ),
    ]
