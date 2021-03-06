# Generated by Django 3.1.7 on 2021-03-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20210320_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonemodel',
            name='aciklama',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='açıklama'),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='bellek',
            field=models.CharField(choices=[('2 gb', '2 gb'), ('4 gb', '4 gb'), ('6 gb', '6 gb'), ('8 gb', '8 gb'), ('12 gb', '12 gb'), ('16 gb', '16 gb'), ('32 gb', '32 gb')], default=1, max_length=20, verbose_name='rem'),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='hafıza',
            field=models.CharField(choices=[('16 gb', '16 gb'), ('32 gb', '32 gb'), ('64 gb', '64 gb'), ('128 gb', '128 gb '), ('256 gb', '256 gb'), ('512 gb', '512 gb')], default=1, max_length=20, verbose_name='hafıza'),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='kamera',
            field=models.CharField(choices=[('12 px', '12 px'), ('16 px', '16 px'), ('32 px', '32 px'), ('64 px', '64 px'), ('128 px', '128 px')], default=1, max_length=20, verbose_name='MegaPixel'),
        ),
        migrations.AlterField(
            model_name='phonemodel',
            name='renk',
            field=models.CharField(choices=[('Siyah', 'Siyah'), ('Beyaz', 'Beyaz'), ('Gold', 'Gold'), ('Gri', 'Gri'), ('Kırmızı', 'Kırmızı'), ('Gümüş', 'Gümüş'), ('Grafit', 'Grafit'), ('Pasifik Mavisi', 'Pasifik Mavisi'), ('Yeşil', 'Yeşil'), ('Mavi', 'Mavi'), ('Uzay Grisi', 'Uzay Grisi'), ('Gece Yeşili', 'Gece Yeşili'), ('Mor', 'Mor'), ('Sarı', 'Sarı'), ('Rose Gold', 'Rose Gold'), ('Pembe', 'Pembe')], default=1, max_length=100, verbose_name='renk'),
        ),
    ]
