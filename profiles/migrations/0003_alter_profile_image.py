# Generated by Django 3.2.17 on 2023-02-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../profile_image', upload_to='images/'),
        ),
    ]
