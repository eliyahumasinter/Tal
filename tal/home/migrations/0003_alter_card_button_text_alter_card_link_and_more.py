# Generated by Django 4.1 on 2022-08-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='button_text',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='card',
            name='link',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='card',
            name='subtitle',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]