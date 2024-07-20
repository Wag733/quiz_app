# Generated by Django 5.0.1 on 2024-07-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0008_rename_question_text_question_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='question',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='question',
            name='choice1',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='choice2',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='choice3',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='choice4',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]