# Generated by Django 4.2.5 on 2023-10-20 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_useradditionalinfo_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
