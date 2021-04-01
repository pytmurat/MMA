# Generated by Django 3.1.7 on 2021-03-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslık', models.CharField(max_length=50, verbose_name='baslık')),
                ('acıklama', models.TextField(verbose_name='acıklama')),
                ('adres', models.CharField(max_length=100, verbose_name='adres')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
                ('telefon', models.CharField(max_length=20, verbose_name='telefon')),
            ],
        ),
    ]
