# Generated by Django 4.2.7 on 2023-11-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='berth_choice',
            field=models.CharField(choices=[('lower', 'lower'), ('upper', 'upper')], max_length=255, verbose_name='berthchoices'),
        ),
    ]
