# Generated by Django 4.2.4 on 2023-08-10 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='', max_length=25),
        ),
    ]