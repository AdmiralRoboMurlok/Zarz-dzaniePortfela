# Generated by Django 5.1.2 on 2024-11-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSItes', '0005_rename_user_frbs_remove_histroy_userkey_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='bank',
            name='loans',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='frbs',
            name='pin',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usersaccount',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='usersaccount',
            name='borrowed',
            field=models.FloatField(default=0),
        ),
    ]
