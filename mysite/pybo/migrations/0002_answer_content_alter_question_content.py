# Generated by Django 4.2.2 on 2023-06-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='content',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(default='', null=True),
        ),
    ]
