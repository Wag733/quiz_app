# Generated by Django 5.0.1 on 2024-07-04 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_quiz_assigned_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_options',
            field=models.ManyToManyField(related_name='correct_questions', to='admins.choice'),
        ),
        migrations.AddField(
            model_name='question',
            name='option_1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='option_2',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='option_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]