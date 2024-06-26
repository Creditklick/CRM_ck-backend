# Generated by Django 5.0.4 on 2024-04-18 12:22

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0003_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Phone',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
