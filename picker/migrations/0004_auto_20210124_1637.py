# Generated by Django 3.1.5 on 2021-01-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picker', '0003_auto_20210124_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='letters_drawn',
            field=models.CharField(default='', max_length=100),
        ),
    ]
