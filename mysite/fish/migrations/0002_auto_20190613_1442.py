# Generated by Django 2.2.2 on 2019-06-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fish',
            old_name='months_available',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='fish',
            name='description',
        ),
        migrations.AddField(
            model_name='fish',
            name='time',
            field=models.CharField(default='all day', max_length=255),
        ),
    ]
