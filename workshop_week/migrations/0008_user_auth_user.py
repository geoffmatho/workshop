# Generated by Django 2.2.4 on 2019-09-16 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshop_week', '0007_workshop_attendees'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
