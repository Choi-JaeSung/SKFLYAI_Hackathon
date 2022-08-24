# Generated by Django 4.1 on 2022-08-24 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('userID', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('userPW', models.TextField()),
                ('userName', models.TextField()),
                ('userBirth', models.IntegerField()),
            ],
        ),
    ]
