# Generated by Django 3.2.9 on 2021-11-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20211104_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actioncameras',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cameras',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='videocameras',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
