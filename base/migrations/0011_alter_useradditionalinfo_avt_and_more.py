# Generated by Django 4.2.5 on 2023-10-21 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useradditionalinfo',
            name='avt',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='useradditionalinfo',
            name='bg',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
