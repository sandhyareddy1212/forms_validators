# Generated by Django 4.2.1 on 2023-07-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentform',
            fields=[
                ('sname', models.IntegerField(primary_key=True, serialize=False)),
                ('sage', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]