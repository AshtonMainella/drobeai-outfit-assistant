# Generated by Django 5.1.1 on 2024-11-11 01:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardrobe', '0002_alter_clothingitem_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(
                    default='profile_pictures/blank-profile-picture-973460_1280.jpg', 
                    upload_to='profile_pictures/'
                )),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, 
                    to=settings.AUTH_USER_MODEL
                )),
            ],
        ),
    ]
