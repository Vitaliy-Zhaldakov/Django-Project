# Generated by Django 3.2.9 on 2021-11-03 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaxResolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VideoCameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=100)),
                ('maxResolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.maxresolution')),
            ],
        ),
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=100)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.type')),
            ],
        ),
        migrations.CreateModel(
            name='ActionCameras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=100)),
                ('maxResolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.maxresolution')),
            ],
        ),
    ]
