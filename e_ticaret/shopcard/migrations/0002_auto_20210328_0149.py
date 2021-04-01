# Generated by Django 3.1.7 on 2021-03-27 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_phonemodel_stok'),
        ('shopcard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcardmodel',
            name='product',
        ),
        migrations.AddField(
            model_name='shopcardmodel',
            name='status',
            field=models.CharField(choices=[('waiting', 'beklemede'), ('deleted', 'silindi')], default='waiting', max_length=30),
        ),
        migrations.AddField(
            model_name='shopcardmodel',
            name='totalprice',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ShopCard_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('productd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.phonemodel')),
            ],
        ),
        migrations.AddField(
            model_name='shopcardmodel',
            name='items',
            field=models.ManyToManyField(blank=True, to='shopcard.ShopCard_item'),
        ),
    ]