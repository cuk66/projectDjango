# Generated by Django 5.0.1 on 2024-01-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='graph_skills',
            field=models.ImageField(upload_to='image/', verbose_name='График по скиллам'),
        ),
    ]