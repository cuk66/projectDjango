from django.db import models


# Create your models here.
class ImageUpload(models.Model):
    image = models.ImageField(upload_to='img', blank=False, verbose_name='Изображение')


class Relevance(ImageUpload, models.Model):
    graph_salary_level = models.ImageField(blank=False, verbose_name='График уровень зарплат по годам')
    graph_num_vacancy = models.ImageField(blank=False, verbose_name='График количество вакансий по годам')
    table = models.TextField(blank=False, verbose_name='Таблица')


