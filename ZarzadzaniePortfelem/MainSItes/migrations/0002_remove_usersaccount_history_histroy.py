# Generated by Django 5.1.2 on 2024-10-30 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainSItes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersaccount',
            name='history',
        ),
        migrations.CreateModel(
            name='Histroy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date', models.DateTimeField()),
                ('UserKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainSItes.user')),
            ],
        ),
    ]
