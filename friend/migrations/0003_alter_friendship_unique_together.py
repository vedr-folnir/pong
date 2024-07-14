# Generated by Django 5.0.7 on 2024-07-12 15:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0002_alter_friendship_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together={('user', 'friend')},
        ),
    ]
