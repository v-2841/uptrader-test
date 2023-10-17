from django.db import models


class MenuItem(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Текст меню',
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='Предыдущий узел',
    )
    url = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='URL',
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return self.title
