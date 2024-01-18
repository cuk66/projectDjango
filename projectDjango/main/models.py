from django.db import models


# Create your models here.
class ImageUpload(models.Model):
    image = models.ImageField(upload_to='img', blank=True, verbose_name='Изображение')


class Relevance(ImageUpload, models.Model):
    graph_salary_level = models.ImageField(upload_to='image/', blank=False, verbose_name='График уровень зарплат по годам')
    graph_num_vacancy = models.ImageField(upload_to='image/', blank=False, verbose_name='График количество вакансий по годам')
    table = models.TextField(blank=False, verbose_name='Таблица')

    def __str__(self):
        return f"{self.graph_salary_level} {self.graph_num_vacancy} {self.table}"


class Skills(models.Model):
    table_name = models.TextField(blank=False, max_length=30, verbose_name='Название таблицы')
    table = models.TextField(blank=False, verbose_name='Таблица')
    graph_skills = models.ImageField(upload_to='image/', blank=False, verbose_name='График по скиллам')

    def __str__(self):
        return f"{self.table_name} {self.table} {self.graph_skills}"


class Geography(models.Model):
    graph_salary_level_by_city = models.ImageField(upload_to='image/', blank=False, verbose_name='График уровень зарплат по городам')
    graph_vacancy_fraction_by_city = models.ImageField(upload_to='image/', blank=False, verbose_name='График доля вакансий по городам')
    table = models.TextField(blank=False, verbose_name='Таблица')

    def __str__(self):
        return f"{self.graph_salary_level_by_city} {self.graph_vacancy_fraction_by_city} {self.table}"
