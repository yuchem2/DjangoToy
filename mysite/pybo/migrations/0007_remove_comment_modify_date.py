# Generated by Django 4.2.2 on 2023-07-19 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_comment_answer_comments_question_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='modify_date',
        ),
    ]
