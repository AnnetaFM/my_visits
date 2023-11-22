from django.db import models


class Worker(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя пользователя',
        )
    telephone_number = models.CharField(
        max_length=255,
        verbose_name='Номер телефона',
        )

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name


class SalePoint(models.Model):
    name = models.TextField(verbose_name='Название торговой точки',)
    worker = models.ForeignKey(
        Worker,
        related_name='visiter',
        verbose_name='Имя работника',
        blank=False,
        on_delete=models.CASCADE
        )

    class Meta:
        verbose_name = 'Точка продаж'
        verbose_name_plural = 'Точки продаж'

    def __str__(self):
        return self.name


class Visit(models.Model):
    visit_datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата/время посещения'
        )
    shop = models.ForeignKey(
        SalePoint,
        related_name='store',
        verbose_name='Точка визита',
        on_delete=models.CASCADE,
        )
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Визит'
        verbose_name_plural = 'Визиты'

    def __str__(self):
        return f'Посещение {self.shop.name} в {self.visit_datetime}'
