# Generated by Django 5.1.1 on 2024-09-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('offline', 'Offline'), ('online', 'Online'), ('solo', 'Solo'), ('lobby', 'Lobby'), ('ingame', 'In Game')], default='offline', max_length=7)),
            ],
        ),
    ]
