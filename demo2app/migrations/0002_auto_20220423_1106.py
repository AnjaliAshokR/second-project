# Generated by Django 3.2.12 on 2022-04-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo2app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pictures')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='courses',
        ),
    ]
