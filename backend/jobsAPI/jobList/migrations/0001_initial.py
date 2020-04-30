# Generated by Django 2.2.12 on 2020-04-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=100)),
                ('jobDescription', models.TextField()),
                ('jobUrl', models.URLField()),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
