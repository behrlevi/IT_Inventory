# Generated by Django 4.2.5 on 2023-09-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_address_record_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='note',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
