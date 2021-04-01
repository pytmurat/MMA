# Generated by Django 3.1.7 on 2021-03-26 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0011_phonemodel_stok'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.phonemodel')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
