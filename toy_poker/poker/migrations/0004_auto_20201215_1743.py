# Generated by Django 3.1.2 on 2020-12-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0003_userinfo_bot_deck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='bot_deck',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='deck',
            field=models.CharField(max_length=300),
        ),
    ]
