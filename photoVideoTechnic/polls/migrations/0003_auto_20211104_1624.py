# Generated by Django 3.2.9 on 2021-11-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='actioncameras',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cameras',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videocameras',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
