# Generated by Django 3.1.7 on 2021-03-21 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50, verbose_name='isim')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('konu', models.CharField(max_length=100, verbose_name='konu')),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]