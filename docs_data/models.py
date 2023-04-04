from django.db import models
from django.contrib.auth.models import AbstractUser


class Subdivision(models.Model):
    subdivision_name = models.TextField(verbose_name="Название подразделения")

    def __str__(self):
        return self.subdivision_name

    class Meta:
        ordering = ('subdivision_name',)
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class CustomUser(AbstractUser):
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class CategoryItem(models.Model):
    category_item_name = models.TextField(verbose_name="Название категории, подкатегории")
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.category_item_name

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class DocData(models.Model):
    doc_file = models.FileField(verbose_name="Файл", upload_to='docs')
    category = models.ForeignKey(CategoryItem, on_delete=models.CASCADE, verbose_name="Категория")
    file_name = models.TextField(verbose_name="Название документа")
    description = models.TextField(verbose_name="Описание документа", blank=True, null=True)
    doc_date = models.DateField(verbose_name="Дата документа", blank=True, null=True)

    def __str__(self):
        return self.file_name

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'




