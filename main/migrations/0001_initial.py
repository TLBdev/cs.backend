# Generated by Django 3.0.5 on 2020-04-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('room_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('season_id', models.IntegerField()),
                ('left_id', models.IntegerField()),
                ('right_id', models.IntegerField()),
                ('up_id', models.IntegerField()),
                ('down_id', models.IntegerField()),
                ('outside_id', models.IntegerField()),
                ('inside_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('top_tile', models.IntegerField()),
                ('bottom_tile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_solved', models.IntegerField()),
            ],
        ),
    ]
