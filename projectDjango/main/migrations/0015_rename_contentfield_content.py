# Generated by Django 5.0.1 on 2024-01-18 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_contentfield'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContentField',
            new_name='Content',
        ),
    ]