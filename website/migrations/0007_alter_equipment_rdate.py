# Generated by Django 4.2.5 on 2023-09-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_equipment_licence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='rdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
