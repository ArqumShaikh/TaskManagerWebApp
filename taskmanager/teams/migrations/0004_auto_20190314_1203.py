# Generated by Django 2.1.7 on 2019-03-14 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20190314_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]