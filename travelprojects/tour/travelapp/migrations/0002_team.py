# Generated by Django 3.2.13 on 2022-05-30 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=200)),
                ('img1', models.ImageField(upload_to='pics')),
                ('desc1', models.TextField()),
            ],
        ),
    ]
