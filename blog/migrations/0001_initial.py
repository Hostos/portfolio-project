# Generated by Django 2.0.2 on 2018-10-07 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]