# Generated by Django 3.2.4 on 2021-06-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20210609_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]