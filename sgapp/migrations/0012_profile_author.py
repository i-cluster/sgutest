# Generated by Django 2.1.4 on 2020-02-24 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgapp', '0011_auto_20200224_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='author',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
