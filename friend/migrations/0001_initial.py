# Generated by Django 5.0.7 on 2024-07-12 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('blocked', 'Blocked')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_player', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_user1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'friend')},
            },
        ),
    ]
