from django.db import models


class BasePage(models.Model):
    title = models.CharField(max_length=70, blank=True, verbose_name=u"Название")
    price = models.CharField(max_length=25, blank=True, verbose_name=u"Цена")
    slug = models.SlugField(unique=True, blank=True, verbose_name=u"Артикул")
    body = models.TextField(max_length=150, blank=True, verbose_name=u"Аннотация")
    drop_body = models.TextField(max_length=350, blank=True, verbose_name=u"Описание")
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары на главной станице'


    def __str__(self):
        return self.title

