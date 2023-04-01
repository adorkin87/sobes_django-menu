from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя меню')

    def __str__(self):
        return self.name


class ItemMenu(models.Model):
    menu = models.ForeignKey('Menu',
                             on_delete=models.PROTECT,
                             verbose_name='Имя меню')
    name = models.CharField(max_length=50, verbose_name='Имя пункта меню')
    parent = models.ForeignKey('self',
                                null=True,
                                blank=True,
                                on_delete=models.PROTECT,
                                verbose_name='Родительский пункт меню')
    url = models.SlugField(max_length=255,
                           unique=True,
                           verbose_name='URL')

    def __str__(self):
        return self.name
