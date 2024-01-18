# Generated by Django 5.0.1 on 2024-01-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_geography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='relevance',
            name='graph_num_vacancy',
            field=models.ImageField(upload_to='image/', verbose_name='График количество вакансий по годам'),
        ),
        migrations.AlterField(
            model_name='relevance',
            name='graph_salary_level',
            field=models.ImageField(upload_to='image/', verbose_name='График уровень зарплат по годам'),
        ),
    ]
