# Generated by Django 3.1.7 on 2021-03-20 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_phonemodel_yayinda_mi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='hafıza',
            field=models.CharField(choices=[('16 gb', '16 gb'), ('32 gb', '32'), ('64 gb', '64'), ('128 gb', '128'), ('256 gb', '256')], default=1, max_length=20, verbose_name='hafıza'),
        ),
    ]