# Generated by Django 4.2.4 on 2023-08-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0006_alter_theme_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='pub_date',
            field=models.DateTimeField(default='1970-01-01', verbose_name='date published'),
        ),
    ]
