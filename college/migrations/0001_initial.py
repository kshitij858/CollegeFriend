# Generated by Django 3.2.5 on 2021-08-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=10)),
                ('professors', models.ManyToManyField(blank=True, to='college.Professor')),
            ],
        ),
    ]
