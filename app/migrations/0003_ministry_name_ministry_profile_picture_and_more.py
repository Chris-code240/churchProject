# Generated by Django 4.2.6 on 2024-05-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_person_created_at_person_dob_person_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ministry',
            name='name',
            field=models.CharField(default='UNKNOWN', max_length=280),
        ),
        migrations.AddField(
            model_name='ministry',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='ministry_profile_pictures'),
        ),
        migrations.AddField(
            model_name='mustardseed',
            name='location',
            field=models.CharField(default='UNKNOWN', max_length=120),
        ),
        migrations.AddField(
            model_name='mustardseed',
            name='name',
            field=models.CharField(default='UNKNOWN', max_length=280),
        ),
        migrations.AddField(
            model_name='mustardseed',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='mustard_profile_pictures'),
        ),
        migrations.AddField(
            model_name='position',
            name='title',
            field=models.CharField(default='UNKNOWN', max_length=280),
        ),
    ]
